import Default_Components
import Areas_Calculator

class Standard_Calculator(Default_Components.BasicCalculator):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.slide_panel.standard_calculator_button.configure(command = None, state = 'disabled')
        self.slide_panel.areas_calculator_button.configure(command = lambda: self.open_areas_calculator(), state = 'normal')

    def open_areas_calculator(self) -> None:
        '''Starts up the areas calculator once the correpondent button is clicked'''

        # Remove all widgets from the window
        for widget in self.window.winfo_children():
            widget.destroy()

        # Create the Areas Calculator in the current window
        self.areas_calculator = Areas_Calculator.Areas_Calculator(self.window, "Circle")