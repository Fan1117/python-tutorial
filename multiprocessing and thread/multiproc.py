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

#def consumer(input_q, message):
#    while True:
#        item = input_q.get()
#        print(message + ": ", item)
#        input_q.task_done()
#        
#def producer(sequence, output_q):
#    for item in sequence:
#        output_q.put(item)
#        
#        
#if __name__ == '__main__':
#    q = multiprocessing.JoinableQueue()
#    cons_p1 = multiprocessing.Process(target=consumer, args=(q,"Process 1"))
#    cons_p1.daemon = True
#    cons_p1.start()
#    
#    q = multiprocessing.JoinableQueue()
#    cons_p2 = multiprocessing.Process(target=consumer, args=(q,"Process 2"))
#    cons_p2.daemon = True
#    cons_p2.start()
#    
#    sequence = [1,2,3,4]
#    producer(sequence, q)
#    q.join()

def consumer(input_q, message):
    while True:
        item = input_q.get()
        print(message + ": ", item, time.time())
        input_q.task_done()
        
def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)
        
        
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,"Process 1"))
    cons_p1.daemon = True
    cons_p1.start()
    
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,"Process 2"))
    cons_p2.daemon = True
    cons_p2.start()
    
    sequence = [1,2,3,4,5,6,7,8,9]
    producer(sequence, q)
    q.join()
    
    