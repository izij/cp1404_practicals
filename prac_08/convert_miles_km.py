

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_RATE = 1.60934


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles into km"""
    result_message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result_message = "Answer in Km"
        return self.root

    def handle_calculation(self, value):
        """Converts input value into Km"""
        try:
            self.result_message = str(float(value) * CONVERSION_RATE)
        except ValueError:
            pass

    def handle_increment(self, text_input, change):
        """Adds on value to miles value"""
        try:
            input_value = float(text_input)
        except ValueError:
            input_value = 0
        result = float(input_value) + change
        self.root.ids.input_number.text = str(result)


ConvertMilesApp().run()
