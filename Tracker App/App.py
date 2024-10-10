import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store skills
SKILL_FILE = "skills.json"

# Load skills from JSON file
def load_skills():
    if os.path.exists(SKILL_FILE):
        with open(SKILL_FILE, "r") as f:
            return json.load(f)
    return {}

# Save skills to JSON file
def save_skills(skills):
    with open(SKILL_FILE, "w") as f:
        json.dump(skills, f)

class SkillTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Computer Skill Tracker")

        self.skills = load_skills()

        self.skill_label = tk.Label(master, text="Skill Tracker", font=("Arial", 16))
        self.skill_label.pack()

        self.skill_listbox = tk.Listbox(master)
        self.skill_listbox.pack()

        self.add_skill_button = tk.Button(master, text="Add Skill", command=self.add_skill)
        self.add_skill_button.pack()

        self.remove_skill_button = tk.Button(master, text="Remove Skill", command=self.remove_skill)
        self.remove_skill_button.pack()

        self.update_skill_button = tk.Button(master, text="Update Skill", command=self.update_skill)
        self.update_skill_button.pack()

        self.display_skills()

    def display_skills(self):
        self.skill_listbox.delete(0, tk.END)
        for skill, data in self.skills.items():
            self.skill_listbox.insert(tk.END, f"{skill} - {data['level']}")

    def add_skill(self):
        skill_name = simpledialog.askstring("Input", "Enter skill name:")
        if skill_name:
            level = simpledialog.askstring("Input", "Enter proficiency level (Beginner, Intermediate, Advanced):")
            if level:
                self.skills[skill_name] = {"level": level}
                save_skills(self.skills)
                self.display_skills()

    def remove_skill(self):
        selected_skill = self.skill_listbox.curselection()
        if selected_skill:
            skill_name = self.skill_listbox.get(selected_skill).split(" - ")[0]
            del self.skills[skill_name]
            save_skills(self.skills)
            self.display_skills()
        else:
            messagebox.showwarning("Selection Error", "Please select a skill to remove.")

    def update_skill(self):
        selected_skill = self.skill_listbox.curselection()
        if selected_skill:
            skill_name = self.skill_listbox.get(selected_skill).split(" - ")[0]
            level = simpledialog.askstring("Input", "Update proficiency level (Beginner, Intermediate, Advanced):")
            if level:
                self.skills[skill_name]['level'] = level
                save_skills(self.skills)
                self.display_skills()
        else:
            messagebox.showwarning("Selection Error", "Please select a skill to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SkillTrackerApp(root)
    root.mainloop()
