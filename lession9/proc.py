#!/usr/bin/env python3
from multiprocessing import Queue, Process
queue = Queue()
def f1():
    queue.put('shiyanlou')
def f2():
    data = get.queue()
    print(date)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()
