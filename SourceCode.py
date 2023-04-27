from PIL import Image, ImageChops, ImageEnhance, ImageOps
import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        master.title("Image Blender")
        self.source_button = tk.Button(master, text="Select main image", command=self.select_source)
        self.source_button.pack()
        self.multiply_button = tk.Button(master, text="Select Shadow image (press to skip)", command=self.select_multiply)
        self.multiply_button.pack()
        self.screen_button = tk.Button(master, text="Select Highlight image (press to skip)", command=self.select_screen)
        self.screen_button.pack()
        self.blend_button = tk.Button(master, text="Get Output", command=self.blend_images)
        self.blend_button.pack()
        self.status_label = tk.Label(master, text="")
        self.status_label.pack()
        self.sourceImg = None
        self.multiplyImg = None
        self.screenImg = None

    def select_source(self):
        self.sourceImg_path = filedialog.askopenfilename(title="Select main image")
        self.sourceImg = Image.open(self.sourceImg_path)
        self.status_label.config(text=f"Selected main image: {self.sourceImg_path}")

    def select_multiply(self):
        self.multiplyImg_path = filedialog.askopenfilename(title="Select Shadow image (press cancel to skip)", defaultextension=".png")
        if self.multiplyImg_path:
            self.multiplyImg = Image.open(self.multiplyImg_path)
            self.status_label.config(text=f"Selected Shadow image: {self.multiplyImg_path}")
        else:
            self.status_label.config(text="No Shadow image selected")

    def select_screen(self):
        self.screenImg_path = filedialog.askopenfilename(title="Select Highlight image (press cancel to skip)", defaultextension=".png")
        if self.screenImg_path:
            self.screenImg = Image.open(self.screenImg_path)
            self.status_label.config(text=f"Selected Highlight image: {self.screenImg_path}")
        else:
            self.status_label.config(text="No Highlight image selected")

    def blend_images(self):
        if self.multiplyImg:
            image_blend1 = ImageChops.multiply(self.multiplyImg, self.sourceImg)
        else:
            image_blend1 = self.sourceImg

        if self.screenImg:
            if self.multiplyImg:
                image_blend2 = ImageChops.screen(self.screenImg, image_blend1)
            else:
                image_blend2 = ImageChops.screen(self.screenImg, self.sourceImg)
        else:
            image_blend2 = image_blend1
        output_path = "output.png"
        image_blend2.save(output_path)
        self.status_label.config(text=f"Output saved as {output_path}")

root = tk.Tk()
app = App(root)
root.mainloop()
