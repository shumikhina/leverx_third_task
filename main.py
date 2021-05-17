from multiprocessing import Lock
from multiprocessing.pool import ThreadPool


class Parameter:

    def __init__(self, a=0):
        self.a = a

    def __add__(self, other: int):
        self.a += other
        return self


def function(arg, param: Parameter, lock: Lock) -> Parameter:
    for _ in range(arg):
        with lock:
            param += 1
    return param


def main():
    a = Parameter()     # named as in example
    pool = ThreadPool(5)
    pool_lock = Lock()
    pool.starmap(function, [(1000000, a, pool_lock)]*5)
    pool.close()
    pool.join()
    print("----------------------", a.a)


if __name__ == "__main__":
    main()
