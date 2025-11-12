import tkinter as tk
from tkinter import messagebox
from Model import CalculatorModel
from View import CalculatorView

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate(self):
        try:
            num1, num2, operation = self.view.get_input()
            self.model.num1 = num1
            self.model.num2 = num2
            self.model.operation = operation

            if operation == '+':
                self.model.result = self.model.num1 + self.model.num2
            elif operation == '-':
                self.model.result = self.model.num1 - self.model.num2
            elif operation == '*':
                self.model.result = self.model.num1 * self.model.num2
            elif operation == '/':
                if self.model.num2 == 0:
                    raise ValueError("Cannot divide by zero")
                self.model.result = self.model.num1 / self.model.num2
            else:
                raise ValueError("Invalid operation")

            self.view.display_result(self.model.result)
        except ValueError as e:
            self.view.display_error(str(e))

    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root, None) 
    controller = CalculatorController(model, view)
    view.controller = controller  
    root.mainloop()