import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(5.0)
    print(f'{time.ctime()} GoodBye!')
    
loop = asyncio.get_event_loop()
task = loop.create_task(main())
print("ㅅㄷㄴㅅ")
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True) # 루프 중지 증으로 블로킹 상태가 풀린 후에 아직 실행중인 태스크를 취합하고  
                                                         # 모든 태스크에게 취소 요청을 한 후에 loop.run_until_complete()를 호출하여 태스크들이 모두 종료 상태가 될 때까지 기다린다.
                                                         # asyncio.run()의 내부에서 위의 절차를 모두 포함한다.
loop.run_until_complete(group)
loop.close()