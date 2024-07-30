class employee:
    def __init__(self, dept,sal):
        self.dept=dept
        self.sal=sal
    def showDetail(self):
        print("dept = ",self.dept)
        print("salary = ",self.sal)

class Engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("IT",45000) 

engg1=Engineer("David",32)
engg1.showDetail()
