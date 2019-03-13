class Math_obj():
    def __init__(self,number):
        self.number=number

    def pow(self,x):
        result=1
        if x<0:
            return 1/self.number**(-x)
        for power in range(x):
            result*=self.number
        return f'{self.number} to power of {x} will be {result}'




alpha=Math_obj(5)
print(alpha.pow(-2))