# study_buddy.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os
import json

class TaskItem(BoxLayout):
    def __init__(self, task, deadline, **kwargs):
        super(TaskItem, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(Label(text=task, size_hint=(0.7, 1)))
        self.add_widget(Label(text=f'Due: {deadline}', size_hint=(0.3, 1)))

class StudyBuddyApp(App):
    def build(self):
        self.tasks = []
        self.load_tasks()

        self.layout = BoxLayout(orientation='vertical')

        # Input fields
        self.task_input = TextInput(hint_text='Enter Task', size_hint_y=None, height=40)
        self.deadline_input = TextInput(hint_text='Enter Deadline (YYYY-MM-DD)', size_hint_y=None, height=40)
        self.layout.add_widget(self.task_input)
        self.layout.add_widget(self.deadline_input)

        # Add button
        self.add_button = Button(text='Add Task', on_press=self.add_task)
        self.layout.add_widget(self.add_button)

        # Task display
        self.task_display = RecycleView(size_hint=(1, 0.8))
        self.layout.add_widget(self.task_display)

        self.update_task_display()

        return self.layout

    def add_task(self, instance):
        task = self.task_input.text
        deadline = self.deadline_input.text

        if task and deadline:
            self.tasks.append({'task': task, 'deadline': deadline})
            self.save_tasks()
            self.task_input.text = ''
            self.deadline_input.text = ''
            self.update_task_display()

    def update_task_display(self):
        self.task_display.data = [{'text': f"{task['task']} (Due: {task['deadline']})"} for task in self.tasks]

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)

if __name__ == '__main__':
    StudyBuddyApp().run()
