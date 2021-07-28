# import asyncio
# import time
#
# async def display_no():
#     staring=time.time()
#
#     while True:
#         dur= int(time.time() - staring)
#
#         if dur%3==0:
#             print("{} sec have passed".format(dur))
#         await asyncio.sleep(1)
#
# async def display_no2():
#     num=1
#
#     while True:
#         print(num)
#         num += 1
#
#         await asyncio.sleep(0.1)
#
# async def main():
#     task1=asyncio.create_task(display_no())
#     task2=asyncio.create_task(display_no2())
#
#     await asyncio.gather(task1,task2)
#
# asyncio.run(main())





                   # practice
import asyncio
import time

async def display_no():
    starting = time.time()
    while True:
        differnce = int(time.time()-starting)
        if differnce%3==0:
            print(f"{differnce} sec gone")

        await asyncio.sleep(1)

async def no_repeat():
    num=1
    while True:
        print(num)

        num +=1
        await asyncio.sleep(0.2)

async def main_1():
    task1=asyncio.create_task(display_no())
    task2=asyncio.create_task(no_repeat())

    await asyncio.gather(task1,task2)
asyncio.run(main_1())