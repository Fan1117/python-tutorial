# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:55:44 2019

@author: macfa
"""
import multiprocessing
import time

#def clock(interval):
#    while True:
#        print("The time is %s" % time.ctime())
#        time.sleep(interval)
#if __name__ == '__main__':
#    p = multiprocessing.Process(target=clock, args=(15,))
#    p.start()
#        
#        

def consumer(input_q):
    while True:
        item = input_q.get()
        print(item)
        input_q.task_done()
        
def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)
        
        
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()
    
    sequence = [1,2,3,4]
    producer(sequence, q)
    q.join()
    
    