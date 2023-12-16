from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class AgeCalculatorApp(App):
    def build(self):
        self.age = "00"
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        text = Label(text="Write your age", font_size=20, background_color=(1, 0, 0, 1))
        layout.add_widget(text)

        self.age_input = TextInput(text=self.age, font_size=30, multiline=False, input_type="number")
        layout.add_widget(self.age_input)

        btn = Button(text="Calculate Age", size_hint=(None, None), size=(200, 80), background_color=(0, 0, 1, 1))
        btn.bind(on_press=self.calc)
        layout.add_widget(btn)

        return layout

    def calc(self, instance):
        try:
            age_value = int(self.age_input.text)
            months = age_value * 12
            weeks = months * 4
            days = weeks * 7

            result_text = (
                f"Your Age in Months Is: {months}\n"
                f"Your Age in Weeks Is: {weeks}\n"
                f"Your Age in Days Is: {days}"
            )

            popup = Popup(title="Your Age In All time units", content=Label(text=result_text), size_hint=(None, None), size=(400, 200))
            popup.open()

        except ValueError:
            popup = Popup(title="Error", content=Label(text="Please enter a valid age."), size_hint=(None, None), size=(300, 150))
            popup.open()

if __name__ == '__main__':
    AgeCalculatorApp().run()
