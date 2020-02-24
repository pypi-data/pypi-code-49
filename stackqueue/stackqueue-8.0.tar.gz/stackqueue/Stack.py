class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return (print("error"))
        else:
            return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def print(self):
        return (print(self.items))

    def size(self):
        return (len(self.items))

    def back(self):
        if self.is_empty():
            return (print("error"))
        else:
            return (self.items[len(self.items)-1])

    def clear(self):
        self.items.clear()

    def count(self,item):
        return (self.items.count(item))

    def reverse(self):
        return (self.items.reverse())

    def index(self,item):
        return (self.items.index(item))
    
    def exit(self):
        return ("bye bye")