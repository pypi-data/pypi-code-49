class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return (self.items == [])

    def clear(self):
        self.items.clear()

    def front(self):
        if self.is_empty():
            return (print("error"))
        else:
            return (self.items[0])

    def size(self):
        return (len(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return (print("error"))
        else:
            return self.items.pop(0)

    def print(self):
        return (print(self.items))

    def count(self,item):
        return (self.items.count(item))

    def reverse(self):
        return (self.items.reverse())

    def index(self,item):
        return (self.items.index(item))
        
    def exit(self):
        return ("bye bye")
