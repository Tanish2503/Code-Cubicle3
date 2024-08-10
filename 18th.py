class employee:
    salary = 2131
    increment = 30
    @property
    def salaryafter(self):
        return(self.salary+self.salary*(self.increment/100))
    
    @salaryafter.setter
    def salaryafter(self,salary):
        self.increment = ((salary/self.salary)-1)*100 

e=employee()
print(e.salaryafter)
e.salaryafter = 2800
print(e.increment)