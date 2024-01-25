import Default_Components


class Standard_Calculator(Default_Components.BasicCalculator):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
        for i in range(len(Standard_Calculator.operation_buttons)):
         Standard_Calculator.operation_buttons[i].destroy()

        Standard_Calculator.number_buttons[10].destroy()
