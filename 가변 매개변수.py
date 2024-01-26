
def test(*data):
    length = len(data)
    print(type(data),length,data)

def test2(**data):
    length = len(data)
    print(type(data),length)
    for key,value in data.items():
        print(key,value,sep='-')

def test3(*data1,**data2):
    print(data1)
    print(data2)

def test4(data1,*data2,**data3):
    print(data1)
    print(data2)
    print(data3)
#튜플에 각각의 요소가
test('가','나','다')
print('-' * 10)
#하나의 튜플요소에 리스트가.
test(['가','나','다'])
print('-' * 10)
a = {
    'a' : '123',
    'b' : '456',
}

test2(**a)
print('-' * 10)
test3(1,2,3,'가','나', a=123,b=456)
print('-' * 10)
test4('나는 튜플에 안들어간다',1,2,3,'가','나', a=123,b=456)
print('-' * 10)