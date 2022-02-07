import threading


# 1. Write the method that returns the number of threads currently in execution.
# Also, prepare the method that will be executed with threads and run during the first method counting.
# (multithreading)

def counter():
    print(f'Now {threading.active_count()} thread currently in execution')


def method(name):
    print(f'The {name} currently in execution')


thread1 = threading.Thread(target=method, args=['first thread'])
thread2 = threading.Thread(target=method, args=['second thread'])

counter()

thread1.start()
thread2.start()

counter()

thread1.join()
thread2.join()

counter()
