import cv2
import numpy as np
from tkinter import Tk, Button, Scale, Label, HORIZONTAL, filedialog
from PIL import Image, ImageTk

# Function to open an image file
def open_image():
    global img, edges, photo, edge_photo
    path = filedialog.askopenfilename()  # Opens a dialog to select a file
    if path:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Read the selected image in grayscale
        edges = cv2.Canny(img, lower_threshold.get(), upper_threshold.get())  # Perform initial edge detection
        update_images()  # Update the displayed images

# Function to update the displayed images
def update_images():
    global img, edges, photo, edge_photo
    if img is not None:
        # Convert the OpenCV images to PIL format
        img_pil = Image.fromarray(img)
        edges_pil = Image.fromarray(edges)

        # Convert PIL images to ImageTk format
        photo = ImageTk.PhotoImage(image=img_pil)
        edge_photo = ImageTk.PhotoImage(image=edges_pil)

        # Update the labels with the new images
        original_label.config(image=photo)
        edge_label.config(image=edge_photo)


# Initialize the main window of the application
root = Tk()
root.title("Edge Detection GUI")

# Initialize global variables for the images
img = None
edges = None

# Create and pack the Open Image button
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()


# Create and pack labels for displaying the original and edge-detected images
original_label = Label(root)
original_label.pack(side="left")

edge_label = Label(root)
edge_label.pack(side="right")

# Start the GUI event loop
root.mainloop()
