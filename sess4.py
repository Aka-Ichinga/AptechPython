class ComplexNumber:
    number = 6
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def show(self):
        print(f"The real part is {self.real} and the imaginary part is {self.imag}")

    @classmethod
    def complex(cls):
        print(cls.number)

    @staticmethod
    def fun():
        print('does something')


b = ComplexNumber(3, 2)
d = ComplexNumber(5, 8)
# print(type(b), type(ComplexNumber))
# del b.imag
# # b.imag = 7
# # b.real = 9
# b.show()
# # d.show()
# b.fun()
# ComplexNumber.show(b)
# ComplexNumber.complex()
# ComplexNumber.fun()