#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


def consumer(cond_obj):
    print("consumer thread started...")
    with cond_obj:
        print("consumer thread's waiting...")
        cond_obj.wait()
        print("consumer thread's consuming resource...")


def producer(cond_obj):
    print("producer thread started...")
    with cond_obj:
        print("producer's producing resource")
        time.sleep(5)
        print("Resource's prepared and ready for consume...")
        time.sleep(2)
        print("Notifying all consumer threads")
        cond_obj.notify_all()


if __name__ == "__main__":
    lock = threading.RLock()
    cond = threading.Condition(lock)
    ct1 = threading.Thread(name="consumer1", target=consumer, args=(cond,))
    ct1.start()
    time.sleep(3)
    ct2 = threading.Thread(name="consumer2", target=consumer, args=(cond,))
    ct2.start()
    time.sleep(3)
    pd = threading.Thread(name="producer", target=producer, args=(cond,))
    pd.start()