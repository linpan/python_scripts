#!/user/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing, Queue
import os
import time
from multiprocessing import Process
from time import sleep
from random import randint


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue


    """
     Method to be run in sub-process; can be overridden in sub-class
    """
    def run(self):
        while True:
            for item in range(10):
                self.queue.put(item)
                print(multiprocessing.current_process().name)
                time.sleep(randint(1, 5))
            else:
                print u'循环结束了！'


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            d = self.queue.get(1)
            if d != None:
                print(multiprocessing.current_process().name)
                sleep(randint(1, 4))
                continue
            else:
                break


queue = multiprocessing.Queue(40)

if __name__ == '__main__':
    print ('excited!')
    processed = []
    for i in range(2):
        processed.append(Producer(queue))
        processed.append(Consumer(queue))

    for i in range(len(processed)):
        processed[i].start()

    for i in range(len(processed)):
        processed[i].join()






