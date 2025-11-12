from tkinter import messagebox

class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Calculator")

        # Labels and Entries for inputs
        tk.Label(root, text="First number:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_num1 = tk.Entry(root)
        self.entry_num1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Second number:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_num2 = tk.Entry(root)
        self.entry_num2.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Operation (+, -, *, /):").grid(row=2, column=0, padx=10, pady=5)
        self.entry_operation = tk.Entry(root)
        self.entry_operation.grid(row=2, column=1, padx=10, pady=5)

        # Button to calculate
        self.button_calculate = tk.Button(root, text="Calculate", command=self.controller.calculate)
        self.button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

        # Label for result
        self.label_result = tk.Label(root, text="Result: ")
        self.label_result.grid(row=4, column=0, columnspan=2, pady=10)

    def get_input(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            operation = self.entry_operation.get().strip()
            return num1, num2, operation
        except ValueError:
            raise ValueError("Invalid input. Please enter numbers.")

    def display_result(self, result):
        self.label_result.config(text=f"Result: {result}")

    def display_error(self, error):
        messagebox.showerror("Error", error)