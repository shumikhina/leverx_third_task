from threading import Thread, Lock


a = 0


def function(arg, lock):
    global a
    for _ in range(arg):
        with lock:
            a += 1
    return a


def main():
    threads = []
    lock = Lock()
    for i in range(5):
        thread = Thread(target=function, args=(1000000, lock))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)


if __name__ == "__main__":
    main()
