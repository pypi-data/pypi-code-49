# A simple implementation of Priority Queue  From Geeks For Geeks
# using Queue. 
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data)

    # find size of the list Added By MD Robiuddin
    def size(self):
        return len(self.queue)
      
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i].total_cost < self.queue[max].total_cost: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit()
