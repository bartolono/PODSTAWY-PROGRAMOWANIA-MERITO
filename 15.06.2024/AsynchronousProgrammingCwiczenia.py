def exercise1():
    # Asynchronous Programming - Ćwiczenie 1
    # Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
    import asyncio

    async def print_message():
        await asyncio.sleep(2)
        print("Python Exercises!")

    async def program():
        await print_message()

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

def exercise2():
    # Asynchronous Programming - Ćwiczenie 2
    # Write a Python program that creates three asynchronous functions and displays their respective names with
    # different delays (1 second, 2 seconds, and 3 seconds).
    import asyncio

    async def print_message1():
        await asyncio.sleep(1)
        print("Function 1 executed after 1 second")

    async def print_message2():
        await asyncio.sleep(2)
        print("Function 2 executed after 2 seconds")

    async def print_message3():
        await asyncio.sleep(3)
        print("Function 3 executed after 3 seconds")

    async def program():
        await asyncio.gather(
            print_message1(),
            print_message2(),
            print_message3()
        )

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

def exercise3():
    # Asynchronous Programming - Ćwiczenie 3
    # Write a Python program that creates an asyncio event loop and runs a coroutine
    # that prints numbers from 1 to 7 with a delay of 1 second each.
    import asyncio

    async def print_numbers():
        for i in range(1, 8):
            print(i)
            await asyncio.sleep(1)

    async def program():
        await print_numbers()

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

def exercise4():
    # Asynchronous Programming - Ćwiczenie 4
    # Write a Python program that implements a coroutine to fetch data from two different
    # URLs simultaneously using the "aiohttp" library.
    import asyncio
    import aiohttp

    async def fetch_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def fetch_multiple_urls():
        url1 = 'https://www.wikipedia.org/'
        url2 = 'https://google.com'

        task1 = asyncio.create_task(fetch_url(url1))
        task2 = asyncio.create_task(fetch_url(url2))

        data1 = await task1
        data2 = await task2

        print("Data from ", url1, len(data1), "bytes")
        print("Data from ", url2, len(data2), "bytes")

    async def program():
        await fetch_multiple_urls()

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

def exercise5():
    # Asynchronous Programming - Ćwiczenie 5
    # Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather()
    # and measures the time taken.
    import asyncio
    import time

    async def task1():
        print("Task 1 started")
        await asyncio.sleep(4)
        print("Task 1 finished")

    async def task2():
        print("Task 2 started")
        await asyncio.sleep(1)
        print("Task 2 finished")

    async def task3():
        print("Task 3 started")
        await asyncio.sleep(2)
        print("Task 3 finished")

    async def program():
        print(f"Started at {time.strftime('%X')}")

        await asyncio.gather(
            task1(),
            task2(),
            task3()
        )

        print(f"Finished at {time.strftime('%X')}")

    if __name__ == "__main__":
        start_time = time.time()
        asyncio.run(program())
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
    print("")
    return main()

def exercise6():
    # Asynchronous Programming - Ćwiczenie 6
    # Write a Python program to create a coroutine that simulates a time-consuming task
    # and use asyncio.CancelledError to handle task cancellation.
    import asyncio
    import random

    async def time_consuming_task():
        print('Time-consuming task started...')
        try:
            for i in range(1, 6):
                await asyncio.sleep(random.randint(1, 5))
                print(f'Step {i} completed')
        except asyncio.CancelledError:
            print('Time consuming task was cancelled')
            raise

    async def program():
        task = asyncio.create_task(time_consuming_task())
        await asyncio.sleep(random.randint(1, 3))
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print('Main coroutine caught task cancellation!')

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

def exercise7():
    # Asynchronous Programming - Ćwiczenie 7
    # Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().
    import asyncio

    async def async_operation():
        time = 8
        print(f'Starting long operation for {time} seconds...')
        await asyncio.sleep(time)
        return f'Long operation completed in {time} seconds'

    async def program():
        try:
            result = await asyncio.wait_for(async_operation(), timeout=3)
            print(result)
        except asyncio.TimeoutError:
            timeout = 3
            print(f'Timeout occurred after waiting for {timeout} seconds')

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

def exercise8():
    # Asynchronous Programming - Ćwiczenie 8
    # Write a Python program that uses asyncio queues to simulate a producer-consumer scenario
    # with multiple producers and a single consumer.
    import asyncio
    import random

    async def producer(queue, id):
        for i in range(3):
            item = f"Item: {id}-{i}"
            await queue.put(item)
            print(f"Producer {id} produced-> {item}")
            await asyncio.sleep(random.uniform(0.1, 0.5))

    async def consumer(queue):
        while True:
            item = await queue.get()
            if item is None:
                break
            print(f"Consumer consumed {item}")
            queue.task_done()

    async def program():
        queue = asyncio.Queue()
        producers = [asyncio.create_task(producer(queue, i)) for i in range(3)]
        consumer_task = asyncio.create_task(consumer(queue))
        await asyncio.gather(*producers)
        await queue.join()
        await queue.put(None)
        await consumer_task

    if __name__ == "__main__":
        asyncio.run(program())
    print("")
    return main()

# Kod na "Wybierz ćwiczenie" menu
def get_exercise_function(name):
    exercises = {
        '1': exercise1,
        '2': exercise2,
        '3': exercise3,
        '4': exercise4,
        '5': exercise5,
        '6': exercise6,
        '7': exercise7,
        '8': exercise8,
    }
    return exercises.get(name)

def main():
    while True:
        exercise_name = input("Wpisz cyfrę ćwiczenia (zakres od 1 do 8), aby wczytać poszczególne ćwiczenie (przykład: po wpisaniu '5' wczyta ćwiczenie 5). Wpisz 'wyjdź' aby wyjść z programu: ")
        if exercise_name == 'wyjdź':
            break

        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            result = exercise_function()
            if result is not None:
                print(result)
            else:
                break
        else:
            print("Nie znaleziono ćwiczenia.")

if __name__ == "__main__":
    main()