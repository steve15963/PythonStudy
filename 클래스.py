#타입이란.
data1 = "str"

print(id(data1))
print(type(data1))

#type클래스를 str클래스가 상속받아 구현하고
str
print(id(data1))
print(type(data1))

class Car:
    _name = str()
    _speed = int()
    _position = int()
    def __init__(self,name: str ="자동차 기본이름",speed : int = 0,position: int = 0,*args) -> None:
        self._name = name
        self._speed = speed
        self._position = position
        print(args)
    def move(self):
        print(self._position,"에서",self._speed,"의 속도로")
        self._position += self._speed
        print(self._position,"로 움직입니다.")
    def acc(self):
        if self._speed >= 0:
            self._speed = self._speed + 1
        else:
            print("역방향으로 가속할 수 없습니다.")
    def bre(self):
        if self._speed > 0:
            self._speed = self._speed - 1
        elif self._speed < 0:
            self._speed = self._speed + 1
        else:
            print("정차하였습니다.")
    def revAcc(self):
        if self._speed <= 0:
            self._speed = self._speed - 1
        else:
            print("정방향으로 가속할 수 없습니다.")

myCar = Car("자동차",1,2,1,2)

myCar.bre()
myCar.acc()
myCar.move()


class SportsCar(Car):
    def acc(self):
        if self._speed >= 0:
            self._speed = self._speed + 2
        else:
            print("역방향으로 가속할 수 없습니다.")
    def bre(self):
        if self._speed > 0:
            self._speed = self._speed - 2
        elif self._speed < 0:
            self._speed = self._speed + 2
        else:
            print("정차하였습니다.")

youCar = SportsCar()

youCar.bre()
youCar.acc()
youCar.move()

print("=" * 20)

def testFun(data:Car):
    data.move()
print("다형성 테스트 : ")
testFun( youCar)