class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b  
            else :
                return "Error: Division by zero"
        else:
            return "Invalid operation"

a=float(input("Enter number :"))
b=float(input("Enter number :"))
ope=input("Enter a Operation :")

calc = Calculator(a, b,ope)
print("Result:", calc.calculate())