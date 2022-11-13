

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles into km"""
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Converts input value into Km"""
        pass

    def handle_increment(self, value):
        """Adds on value to miles value"""
        input_value = float(self.root.ids.input_number.text)
        input_value += value
        self.root.ids.input_number.text = str(input_value)


ConvertMilesApp().run()
