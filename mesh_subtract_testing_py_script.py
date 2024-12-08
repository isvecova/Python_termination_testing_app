import numpy as np
import time

print('before import')

import pymeshlab

print('after import')

def to_numpy_array(data, dtype):
    """Ensure data is a NumPy array, converting memoryview if needed."""
    if isinstance(data, memoryview):
        return np.array(data, dtype=dtype)
    return np.asarray(data, dtype=dtype)

def mesh_subtract_and_separate_with_color(mesh_data, green_threshold=0.3, tolerance=1e-4, distance_threshold=0.1):
    """
    Subtracts the second mesh from the first, splits the result into connected components, 
    and identifies vertices for base point calculation based on green color intensity.
    For example, used for spines generation.
    
    Parameters:
        mesh_data (list): List of dictionaries containing 'vertices', 'faces', and optionally 'vertexNormals' and 'faceNormals'.
        green_threshold (int): Threshold for the green component to identify vertices connected to the small mesh.
        tolerance (float): Distance tolerance for proximity checks.
        distance_threshold (float): Threshold for which vertices are considered for calculating base point
            - used if no vertices with green component are found
        
    Returns:
        dict: Contains n_objects, component_data, and base_points for each component.
    """
    ms = pymeshlab.MeshSet()

    # Load meshes and apply distinct colors to each for tracking after boolean operation
    for i, mesh in enumerate(mesh_data[:2]):
        mesh_args = {
            "vertex_matrix": to_numpy_array(mesh['vertices'], dtype=np.float64),
            "face_matrix": to_numpy_array(mesh['faces'], dtype=np.int32)
        }
        if 'vertexNormals' in mesh:
            mesh_args["v_normals_matrix"] = to_numpy_array(mesh['vertexNormals'], dtype=np.float64)
        if 'faceNormals' in mesh:
            mesh_args["f_normals_matrix"] = to_numpy_array(mesh['faceNormals'], dtype=np.float64)

        new_mesh = pymeshlab.Mesh(**mesh_args)
        ms.add_mesh(new_mesh, f"mesh_{i}")


    print('bofore boolean difference')
    time.sleep(20)

    # Perform boolean difference with vertex color transfer
    ms.generate_boolean_difference(first_mesh=0, second_mesh=1)

    print('after boolean difference')

    return {
        "n_objects": 'all good'
    }

# Call the function so that the script can run when called from Matlab
output = mesh_subtract_and_separate_with_color(mesh_data, green_threshold, distance_threshold)
