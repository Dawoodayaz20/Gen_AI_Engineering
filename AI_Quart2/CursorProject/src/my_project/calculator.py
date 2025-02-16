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
    print(calc.add(1, 2))
    print(calc.subtract(1, 2))
    print(calc.multiply(1, 2))
    print(calc.divide(1, 2))
    print(calc.power(1, 2))