from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty






############################
'''

class WidgetsExample(GridLayout):
    counter = 0
    counter_string = StringProperty(str(counter))
    count_enabled = BooleanProperty(False)
    slider_enabled = BooleanProperty(False)
    slider_val_string = StringProperty(str(0))
    text_input_str = StringProperty("Foo")


    def on_button_click(self):
        if self.count_enabled == True:
            print("Button Clicked")
            self.my_text = "Button Pressed"
            self.counter += 1
            self.counter_string = str(self.counter)


    def on_toggle_button(self, toggle_button):
        print(f"toggle button state: {toggle_button.state}")
        if toggle_button.state == "normal":
            toggle_button.text = "Off"
            self.count_enabled = False

        else:
            toggle_button.text = "On"
            self.count_enabled = True


    #def on_switch_active(self, widget):
     #   print(f"Switch: {str(widget.active)}")
      #  if widget.active == True:
       #     self.slider_enabled = True

        #else:
         #   self.slider_enabled = False


    #def on_slider_value(self, widget):
        #print(f"Slider: {str(int(widget.value))}")
        #self.slider_val_string = str(int(widget.value))



    def on_text_validate(self, widget):
        self.text_input_str = widget.text

'''

##############################
'''
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=f"Button {i + 1}", size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
'''
##############################
# class GridLayoutExample(GridLayout):
#  pass


##############################
#class AnchorLayoutExample(AnchorLayout):
 #   pass

##############################
#class BoxLayoutExample(BoxLayout):
 #   pass
"""
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.orientation = "vertical"
      b1 = Button(text = "Button1")
      b2 = Button(text = "Button2")
      self.add_widget(b1)
      self.add_widget(b2)"""

##############################
#class MainWidget(Widget):
  #  pass

##############################
class practiceapp(App):
    pass


practiceapp().run()