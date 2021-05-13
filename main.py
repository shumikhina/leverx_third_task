from threading import Thread, Lock
import typing

a = 0


def function(arg):
    global a
    for _ in range(arg):
        a += 1
    return a


def function_lock(arg, lock: typing.TypeVar):
    temp = 0

    for _ in range(arg):
        temp += 1

    with lock:
        global a
        a += temp


def main():
    threads = []
    lock = Lock()
    for i in range(5):
        thread = Thread(target=function_lock, args=(1000000, lock))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)


if __name__ == "__main__":
    main()
