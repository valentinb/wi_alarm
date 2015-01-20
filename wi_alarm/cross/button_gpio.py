import button_interface
from gpio.input import Input

class Button(button_interface.ButtonInterface):

    def __init__(self):
        self.input = Input()

    def IsPressed(self):
        return self.input.GetState()

