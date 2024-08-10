from random import randint

class Train:
    def __init__(self,train_no):
        self.train_no = train_no
    def book(self,fro,to):
        print(f"your train {self.train_no} is booked from {fro} to {to}")
    def status(self):
        print(f"YOur Train {self.train_no} is on time")
    def fare(self,fro,to):
        print(f"your train{self.train_no} from {fro} to {to} if of {randint(2222,5555)}")

t = Train(122)
t.book("raampur","shahabad")
t.status()
t.fare("raampur","shahabad")