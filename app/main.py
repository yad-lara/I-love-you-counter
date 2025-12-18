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
        self.counter_window = self.canvas.create_window(0,0, window = self.counter_label)

        self.heart_canvas = tk.Canvas(self.canvas, width= 200, height= 200, bg = "white", highlightthickness=0)
        self.heart_window = self.canvas.create_window(0,0, window=self.heart_canvas)

        self.heart = self.heart_canvas.create_oval(50, 80, 150, 180, fill = self.heart_color, outline="")
        self.heart_text=""
        self.heart_canvas.create_text(100, 130, text="", font=("Arial", 16, "bold"), fill="white")
        

         
