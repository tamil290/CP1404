from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def build(self):
        # This is the data or model
        names = ['Tamil', 'Logesh', 'Ahimsa','Madhan' ]

        # This is the main layout
        main_layout = BoxLayout(orientation='vertical')

        # This loop creates the labels
        for name in names:
            label = Label(text=name)
            main_layout.add_widget(label)

        return main_layout


DynamicLabelsApp().run()
