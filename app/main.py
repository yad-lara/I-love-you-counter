import tkinter as tk
from tkinter import filedialog
import os

class Croissant: 
    def __init__(self, root): 
        self.root=root 
        self.root.title ("I love you couter") 
        self.root.geometry ("800x600")

        self.count
        self.timer 
        self.heart_color ="#FFD1DC" 
        self.dark_color = "#F8B2C1"
        self.is_dark = False
        self.bg_photo = None

        self.canvas = tk.Canvas(root, highlightthickness=0, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.counter_label = tk.Label(self.canvas, text="0", font=("Arial", 48, "bold"), bg="white", fg="#FF1493")
        

         
