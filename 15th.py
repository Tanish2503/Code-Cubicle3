class calculator:
    def __init__(self,n):
        self.n = n
    def sq(self):
        print(f"The sq is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def sqrt(self):
        print(f"The sqrt is {self.n ** (1/2)}")
    

a = calculator(4)
a.cube()
a.sq()
a.sqrt()
