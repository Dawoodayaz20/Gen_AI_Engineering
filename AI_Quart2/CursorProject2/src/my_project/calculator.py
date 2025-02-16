class Calculator:
    def add(self, a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers together."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b.
        
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def get_number(self, prompt: str) -> float:
        """Get a valid number input from the user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        """Run the calculator program."""
        operations = {
            '1': ('Add', self.add),
            '2': ('Subtract', self.subtract),
            '3': ('Multiply', self.multiply),
            '4': ('Divide', self.divide)
        }

        print("Welcome to the Calculator!")
        
        while True:
            print("\nCalculator Menu:")
            for key, (name, _) in operations.items():
                print(f"{key}. {name}")
            print("q. Quit")

            choice = input("\nSelect an operation (1-4, or q to quit): ").lower()
            
            if choice == 'q':
                print("Thanks for using the calculator!")
                break
                
            if choice not in operations:
                print("Invalid choice. Please try again.")
                continue
                
            operation_name, operation = operations[choice]
            
            num1 = self.get_number("Enter first number: ")
            num2 = self.get_number("Enter second number: ")
            
            try:
                result = operation(num1, num2)
                print(f"\nResult: {num1} {operation_name.lower()} {num2} = {result}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
            except Exception as e:
                print(f"An error occurred: {e}")

def run():
    """Entry point for the calculator script."""
    calc = Calculator()
    calc.run() 