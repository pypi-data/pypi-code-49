# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: Sep 16, 2018
# Modifi: Sep 16, 2018

import siki.basics.Exceptions as excepts

class Queue:

    def __init__(self):
        self.queue = list()
        self.index = 0

    def enqueue(self, data):
        """
        Adding element to queue
        """
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False


    def dequeue(self):
        """
        Deleting element from queue
        """
        if len(self.queue)>0:
            return self.queue.pop()
        raise excepts.EmptyCollectionElementException("Cannot dequeue an empty queue")    


    def size(self):
        """
        Getting the size of queue
        """
        return len(self.queue)


    def merge(self, queue):
        """
        merge two queues into one
        """
        if type(queue) is list or type(queue) is Queue:
            for item in queue:
                self.enqueue(item)
        else:
            raise excepts.InvalidParamException("cannot merge a non-list or non-queue type")


    def empty(self):
        del self.queue
        self.queue = list()

    
    def is_empty(self):
        return len(self.queue) <= 0


    def __str__(self):
        return str(self.queue)

    
    def __iter__(self):
        self.index = 0
        return self

    
    def __next__(self):
        try:
            return self.queue[self.index]
        except IndexError as e:
            raise StopIteration
        finally:
            self.index += 1


    def __len__(self):
        return len(self.queue)