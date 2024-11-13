function output = mesh_subtract_testing_python(mesh_data)
    % Define parameters for use in the Python script
    green_threshold = 0.3;
    tolerance = 1e-4;
    distance_threshold = 0.1;

    % Call the Python script with mesh data and parameters
    output = pyrunfile('mesh_subtract_testing_py_script.py', "output", ...
        mesh_data=mesh_data, ...
        green_threshold=green_threshold, ...
        tolerance=tolerance, ...
        distance_threshold=distance_threshold);

end
