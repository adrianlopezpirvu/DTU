import cv2
import os
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import csv
from custom_dialog import CustomDialog
import random

# image_directory = r"Photos_of_Faces\frontalimages_spatiallynormalized_part1"
# image_directory = r"Photos_of_Faces\normed_cropped_eq_1-200_a"
image_directory = r"Photos_of_Faces3"

# List of .jpg files
image_names = [f for f in os.listdir(image_directory) if f.endswith('a.jpg')]
random.shuffle(image_names)
root = tk.Tk()

# Canvas to display the image
canvas = tk.Canvas(root, bg='black')
canvas.pack(fill='both', expand=True)  # Configure the canvas to expand and fill both directions
img_obj = None

def update_image_position(event):
    # Update the image position to keep it centered
    global img_obj
    if img_obj is not None:
        canvas.coords(img_obj, event.width // 2, event.height // 2)

# Bind the configure event to the update_image_position function
root.bind('<Configure>', update_image_position)

# Window size = Maximum possible size
root.state('zoomed')

# Create .csv files
base_filename = 'ratings'
i = 0
folder = "data_ratings"  # specify your folder
os.makedirs(folder, exist_ok=True)  # create the folder if it doesn't exist
filename = os.path.join(folder, f"{base_filename}.csv")  # add the folder to your filename

while os.path.isfile(filename):
    i += 1
    filename = os.path.join(folder, f"{base_filename}_{i}.csv")  # add the folder to your filename

# Loop through each image
for image_name in image_names:
    # Open CSV file
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['id', 'image_name', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # From BGR to Tkinter format
        img_bgr = cv2.imread(os.path.join(image_directory, image_name))
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        # Initial window size = image size + margin
        margin = 50
        width = img_pil.width + 2*margin
        height = img_pil.height + 2*margin
        root.geometry(f'{width}x{height}')

        # Minimum window size = Initial window size
        root.minsize(width, height)

        # Add image to canvas
        img_obj = canvas.create_image(root.winfo_width() // 2, root.winfo_height() // 2, image=img_tk)

        # Display image
        root.update()

        # Get rating from user
        dialog = CustomDialog(root, title="Input", message=f"How do you perceive the face in the above photo on a gender continuum?")
        root.wait_window(dialog)
        rating = dialog.result

        # Save rating
        writer.writerow({'id': i, 'image_name': image_name, 'rating': rating})

        # Clear canvas
        canvas.delete('all')
        
        # Close window if image_names is empty
        if not image_names:
            root.destroy()
            
root.destroy()

