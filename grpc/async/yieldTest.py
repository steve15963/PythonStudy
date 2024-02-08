import time
import asyncio
from queue import PriorityQueue, Queue

jobQueue = PriorityQueue()
startTime = time.time()

def test1():
    for i in range(100):
        jobQueue.put((100-i, i))
        time.sleep(0.01)
    middleTime = time.time()
    print("블럭 싱크 중간 걸린 시간 :" , middleTime - startTime)

def test2():
    for i in range(100):
        jobQueue.put((100-i, i))
    endTime = time.time()
    print("블럭 싱크 총   걸린 시간 :" , endTime - startTime)
        
test1()
test2()

jobQueue = PriorityQueue()
startTime = time.time()

async def put(num):
    for i in range(100):
        jobQueue.put(num)

async def makeJob():
    tasks = []
    startTime = time.time()
    for i  in range(100):
        task = asyncio.create_task(put(i))
        tasks.append(task)
    
    #await asyncio.gather(*tasks)
    endTime = time.time()
    print("블럭 싱크 총   걸린 시간 :" , endTime - startTime)

asyncio.run(makeJob())



import random

# jobQueue = PriorityQueue()

# async def get2(num):
#     while True:
#         await asyncio.sleep(0.1)
#         if jobQueue.empty():
#             print(num , "async get Loop print : jobQueue is empty")
#             continue
#         print(num , "async get Loop print : ", jobQueue.get() )
        

# async def put2(r):
#     for i in r:
#         num = random.randint(1, 10000)
#         jobQueue.put(num)
#         print("async put Loop print : ", num )

# async def makeJob2():
#     tasks = []
#     for i in range(5):
#         tasks.append(asyncio.create_task(get2(i)))
#     await asyncio.sleep(1)

#     task = asyncio.create_task(put2(range(100)))


#     await asyncio.gather(task)

#     print(list(jobQueue.queue))

#     await asyncio.gather(*tasks)


# asyncio.run(makeJob2())



async def consumer(num,jobQueue):
    while True:
        await asyncio.sleep(0.1)
        print(num,"consumer is waiting job")
        job = await jobQueue.get()
        print(num, "consumer : ", job)
        jobQueue.task_done()

async def producer(num, jobQueue):
    while True:
        await asyncio.sleep(5)  # 생산자가 새 작업을 생성하는 데 시간이 걸립니다.
        job = random.randint(1, 10000)
        await jobQueue.put(job)  # 비동기 큐에 작업을 추가합니다.
        print(num ,"producer : ", job)

async def Main():
    jobQueue = asyncio.Queue()
    ConsumerTasks = []
    ProducerTasks = []

    for i in range(10000):
        ConsumerTasks.append(asyncio.create_task(consumer(i,jobQueue)))

    for i in range(1):
        ProducerTasks.append(asyncio.create_task(producer(i,jobQueue)))

    await asyncio.gather(*ConsumerTasks, *ProducerTasks)

asyncio.run(Main())

