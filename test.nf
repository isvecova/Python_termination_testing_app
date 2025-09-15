// Parameters
params.data_dir = "${projectDir}/../../data/"

// Actual workflow
workflow {
    println "hello world"
    // First, let's process the masks by creating a channel for the binary mask files
    // YOUR TURN! Replace the "..." below with your code!
    // Hint: the files are in "${params.data_dir}/raw/BBBC010_v1_foreground_eachworm/" and all have a name that ends with "_ground_truth.png"
    binary_mask_files = Channel.fromPath("${params.data_dir}/raw/BBBC010_v1_foreground_eachworm/*_ground_truth.png")

    // Create (well ID, filename) pairs for each mask file
    // YOUR TURN! Replace the "..." below with your code!
    // Hint: use file.baseName to get each file's name and split() to parse it
    grouped_masks = binary_mask_files.map { file -> 
            tuple(file.baseName.tokenize('_')[1], file)
    }.groupTuple()

    my_name = '1649_1109_0003_Amp5-1_B_20070424_B03_w2_D8E64D34-C9DD-4B3C-ACED-BE514B0F935B.tif'
    println my_name.tokenize('_')[1]

}