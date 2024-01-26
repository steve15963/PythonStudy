import asyncio

class AsyncCounter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __aiter__(self):
        print(self)
        return self

    async def __anext__(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            # 각 숫자 사이에 1초의 지연을 둡니다.
            await asyncio.sleep(self.current_value)
            return self.current_value
        else:
            # 카운터가 최대값에 도달하면 StopAsyncIteration 예외를 발생시켜 이터레이션을 종료합니다.
            raise StopAsyncIteration

async def main():
    async for number in AsyncCounter(5):
        print(number)

# 비동기 메인 함수를 실행합니다.
asyncio.run(main())
print("비동기적으로 작동한다면 이 출력이 먼저 나올 것 입니다.")
print("그렇지는 않네요.")