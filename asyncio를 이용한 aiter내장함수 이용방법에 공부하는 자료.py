class DiyRange:
    def __init__(self, end_value=0):
        self.start_value = 0
        self.end_value = end_value
        self.current_value = 0
        self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.end_value:
            temp = self.current_value
            self.current_value += self.step
            return temp
        else:
            self.current_value = 0
            # 카운터가 최대값에 도달하면 StopAsyncIteration 예외를 발생시켜 이터레이션을 종료합니다.
            raise StopIteration


def DiyList(range):
    li = []
    itertor = iter(range)
    try:
        while True:
            li.append(next(itertor))
    except StopIteration:
        pass
    return li
        
print(DiyList(DiyRange(5)))

print(list(range(5)))