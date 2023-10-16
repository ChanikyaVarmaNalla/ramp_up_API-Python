class ComplexNumber:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(f"Complex Number 1: {self.format_complex(self.a, self.b)}"
              f"\nComplex Number 2: {self.format_complex(self.c, self.d)}")

    def format_complex(self, real, ima):
        if real < 0 < ima:
            return f"{ima}i - {-real}"
        elif real > 0 > ima:
            return f"{real} - {-ima}i"
        elif real < 0 and ima < 0:
            return f"-({-real} + {-ima}i)"
        else:
            return f"{real} + {ima}i"

    def add(self):
        res1 = self.a + self.c
        res2 = self.b + self.d
        return self.format_complex(res1, res2)

    def subtract(self):
        res1 = self.a - self.c
        res2 = self.b - self.d
        return self.format_complex(res1, res2)

    def multiply(self):
        res1 = self.a * self.c - self.b * self.d
        res2 = self.a * self.d + self.b * self.c
        return self.format_complex(res1, res2)

    def __eq__(self, other):
        if self.a == self.c:
            return f"The real parts of the complex numbers " \
                   f"'{self.format_complex(self.a, self.b)}' and the " \
                   f"'{self.format_complex(self.c, self.d)}' are equal"
        elif self.b == self.d:
            return f"The complex parts of the complex numbers " \
                   f"'{self.format_complex(self.a, self.b)}' and the " \
                   f"'{self.format_complex(self.c, self.d)}' are equal"
        else:
            return f"The complex numbers '{self.format_complex(self.a, self.b)}' " \
                   f"and '{self.format_complex(self.c, self.d)}' are not equal."

# Example usage
c = ComplexNumber(-2, -3, -1, -4)

print(f"Addition: {c.add()}")
print(f"Subtraction: {c.subtract()}")
print(f"Multiplication: {c.multiply()}")
print(f"Equality: {c == c}")
