from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=f"Button {i + 1}", size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#  pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.orientation = "vertical"
      b1 = Button(text = "Button1")
      b2 = Button(text = "Button2")
      self.add_widget(b1)
      self.add_widget(b2)"""


class MainWidget(Widget):
    pass


class practiceapp(App):
    pass


practiceapp().run()