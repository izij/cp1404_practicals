

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_RATE = 1.60934


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles into km"""
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """Converts input value into Km"""
        result = float(value) * CONVERSION_RATE
        self.root.ids.output_label.text = str(result)
        pass

    def handle_increment(self, input_value, change):
        """Adds on value to miles value"""
        result = float(input_value) + change
        self.root.ids.input_number.text = str(result)


ConvertMilesApp().run()
