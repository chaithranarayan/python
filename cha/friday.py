class first:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        def printname(self):
            print(self.name,self.age);
class child1(first):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname1(self):
        print(self.name,self.age)
ch=child1("chaithramn",21)
ch.printname1()
ch.printname()
class second:
    def dispaly(self,marks,id):
        self.marks=marks
        self.id=id
class father():
    def transport(self):
        print("bike")
          # sam=first("chaithra","mn")
            # sam.printname()