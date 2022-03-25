'''def typechecker(numbercheck):

    while numbercheck >0 and  numbercheck  % 2==0:
        print('this number is a positive even number')
    if numbercheck < 0 and numbercheck % 2==0:
        print ('this number is a negative even number')
    if numbercheck > 0 and numbercheck % 2 !=0:
        print ('this number is a positive odd number')
    if numbercheck < 0 and numbercheck % 2 != 0:
        print ('this number is a negative odd number')
    print('thank you for your time')
    numbercheck = float(numbercheck)
    print(numbercheck)
    return


typechecker(3)'''
class ComplexNumber:
    def __init__(self,r,i):
        self.real = r
        self.imag = i
    def show(self):
        print(f"The real part of the complex number is {self.real} and the imaginary part is {self.imag}")
    @classmethod
    def complex(cls):
        print(cls.imag, cls.real)
    @staticmethod
    def abc(ghi):
        print('tahnk you')


b = ComplexNumber(5,8)
d = ComplexNumber(11,34)
print(ComplexNumber)
print(b.imag,b.real)
d.complex()

b.show()
d.show()

name = 'fioiyo'
x=2
print('%s is %d years old' %(name,x))

print(f"{name} is {x*2} years old")





