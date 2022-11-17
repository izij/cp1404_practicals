"""
CP1404 Prac 8
Dynamic labels task
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Dynamic Labels App"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Isabel", "Keziah", "Ethan", "Lindsay"]

    def build(self):
        """Build Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list of names and adds to GUI"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main_section.add_widget(temp_label)


DynamicLabelsApp().run()
