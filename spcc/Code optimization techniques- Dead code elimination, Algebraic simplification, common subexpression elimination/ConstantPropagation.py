import time
time_exe = []


def without_opt():
    start_time = time.time()
    pi = 3.14
    r = 10
    area = pi * r * r

    a = 0
    for i in range(10000):
        a +=0

    end_time = time.time()
    print(end_time - start_time)
    time_exe.append(end_time - start_time)

def with_opt():
    start_time = time.time()
    pi = 3.14
    r = 10
    area = 3.14 * 10 * 10

    a = 0
    for i in range(10000):
        a +=0

    end_time = time.time()
    print(end_time - start_time)
    time_exe.append(end_time - start_time)

without_opt()
with_opt()
