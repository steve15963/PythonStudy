def test(data1):
    print(data1)
    print(id(data1))

test("안녕")
print("=" * 20)

def test2():
    # 글로벌 변수 인식
    # 변수 먼저 변경시 지역변수 선언되므로 선 사용 후 변경
    print(data)
    # 에러발생! 보고 싶다면 주석 제거
    #data = 2
    print(id(data))

def test3():
    global data
    data = 3
    print(data)
    print(id(data))
    
data = 1
#다른 포인터
print("지역과 전역")
print("참조는 가능하지만 변경시 에러 발생")
test2()
print(data)
print(id(data))
print("-" * 20)
print("global키워드를 통해서 함수 내에서 전역 변수를 사용할 것을 명시하여 에러 방지")
test3()
print(data)
print(id(data))
print("=" * 20)