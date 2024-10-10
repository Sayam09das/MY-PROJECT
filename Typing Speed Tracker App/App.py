import tkinter as tk
from tkinter import messagebox
import random
import time

# Sample sentences for typing practice
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "In the middle of difficulty lies opportunity."
]

class TypingSpeedTracker:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Tracker")

        self.sentence = random.choice(SENTENCES)
        self.start_time = None
        self.end_time = None

        self.instruction_label = tk.Label(master, text="Type the following sentence:")
        self.instruction_label.pack()

        self.sentence_label = tk.Label(master, text=self.sentence, font=("Arial", 12))
        self.sentence_label.pack()

        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack()
        self.text_entry.bind("<KeyRelease>", self.check_typing)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.pack()

    def check_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()

        typed_text = self.text_entry.get()
        if typed_text == self.sentence:
            self.end_time = time.time()
            self.calculate_wpm()

    def calculate_wpm(self):
        time_taken = self.end_time - self.start_time  # time in seconds
        words_typed = len(self.sentence.split())
        wpm = (words_typed / time_taken) * 60  # words per minute
        self.result_label.config(text=f"Your typing speed: {wpm:.2f} WPM")
        self.text_entry.config(state=tk.DISABLED)

    def restart(self):
        self.start_time = None
        self.end_time = None
        self.sentence = random.choice(SENTENCES)
        self.sentence_label.config(text=self.sentence)
        self.text_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.text_entry.config(state=tk.NORMAL)
        self.text_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTracker(root)
    root.mainloop()
