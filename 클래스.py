#타입이란.
data1 = "str"

print(id(data1))
print(type(data1))

#type클래스를 str클래스가 상속받아 구현하고
str
print(id(data1))
print(type(data1))

class Car:
    name = str()
    speed = int()
    position = int()
    def __init__(self,name: str ="자동차 기본이름",speed : int = 0,position: int = 0,*args) -> None:
        self.name = name
        self.speed = speed
        self.position = position
        print(args)
    def move(self):
        print(self.position,"에서",self.speed,"의 속도로")
        self.position += self.speed
        print(self.position,"으로 움직입니다.")
    def acc(self):
        if self.speed >= 0:
            self.speed = self.speed + 1
        else:
            print("역방향으로 가속할 수 없습니다.")
    def bre(self):
        if self.speed > 0:
            self.speed = self.speed - 1
        elif self.speed < 0:
            self.speed = self.speed + 1
        else:
            print("정차하였습니다.")
    def revAcc(self):
        if self.speed <= 0:
            self.speed = self.speed - 1
        else:
            print("정방향으로 가속할 수 없습니다.")

myCar = Car("자동차",1,2,1,2)

myCar.bre()
myCar.acc()
myCar.move()