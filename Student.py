import math
class student:
    def __init__(self,a,b,c):
        self.name=a
        self.surname=b
        self.group=c
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_group(self):
        return self.group
    def set_name(self,s):
        self.name=s
        return 0
    def set_surname(self,s):
        self.surname=s
        return 0
    def set_group(self,s):
        self.group=s
        return 0
    def next_group(self):
        if self.group==11:
            return 1
        else:
            self.group+=1
            return 0
    def vyvod(self):
        print(self.name, self.surname, self.group)
    def vvod(self):
        print("Введите имя")
        self.name=input()
        print("Введите фамилию")
        self.surname=input()
        print("Введите номер группы")
        self.group=int(input())

    def __str__(self):
            return "Name: {0}, {1}, {2} ".format(self.name, self.surname, self.group)

class Point():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
class Line():
    def __init__(self,a,b):
        self.p1=a
        self.p2=b
    def lenline(self):
        x1=self.p1.get_x()
        x2=self.p2.get_x()
        y1 = self.p1.get_y()
        y2 = self.p2.get_y()
        return(math.sqrt((x1-x2)**2+(y1-y2)**2))
