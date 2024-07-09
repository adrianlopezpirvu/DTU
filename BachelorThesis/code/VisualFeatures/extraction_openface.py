import os
import subprocess

# Set the path to the OpenFace executable
executable_path = "C:/Users/AdrianLopez/OneDrive - Universidad Politécnica de Madrid/Documentos/Semestre7/Project/VisualFeaturesExtraction/OpenFace_2.2.0_win_x64/OpenFace_2.2.0_win_x64/FeatureExtraction.exe"  # Adjust this path

# Input folder containing video files
input_folder = "C:/Users/AdrianLopez/OneDrive - Universidad Politécnica de Madrid/Documentos/Semestre7/Project/VisualFeaturesExtraction/FirstImpression/final_subset"  # Adjust this path

# Output directory
output_dir = "C:/Users/AdrianLopez/OneDrive - Universidad Politécnica de Madrid/Documentos/Semestre7/Project/VisualFeaturesExtraction/Final_Balanced"

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        in_file = os.path.join(input_folder, filename)
        #command = f'"{executable_path}" -f "{in_file}" -out_dir "{output_dir}" -verbose' #original one
        command = f'"{executable_path}" -f "{in_file}" -out_dir "{output_dir}" -au_static true'
        subprocess.run(command, shell=True)

        # Print progress
        print(f"Visual features extracted for {filename}")

print("Visual features extracted and organized successfully!")
