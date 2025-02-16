class Calculator:
    def add(self, x, y):
        if not all(isinstance(n, (int, float)) for n in [x, y]):
            raise TypeError("Inputs must be numbers")
        return x + y

    def subtract(self, x, y):
        if not all(isinstance(n, (int, float)) for n in [x, y]):
            raise TypeError("Inputs must be numbers")
        return x - y

    def multiply(self, x, y):
        if not all(isinstance(n, (int, float)) for n in [x, y]):
            raise TypeError("Inputs must be numbers")
        return x * y

    def divide(self, x, y):
        if not all(isinstance(n, (int, float)) for n in [x, y]):
            raise TypeError("Inputs must be numbers")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def power(self, x, y):
        if not all(isinstance(n, (int, float)) for n in [x, y]):
            raise TypeError("Inputs must be numbers")
        return x ** y

if __name__ == "__main__":
    calc = Calculator()
    input_x = float(input("Enter the first number: "))
    input_y = float(input("Enter the second number: "))
    print(calc.add(input_x, input_y))
    print(calc.subtract(input_x, input_y))
    print(calc.multiply(input_x, input_y))
    print(calc.divide(input_x, input_y))
    print(calc.power(input_x, input_y))