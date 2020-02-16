class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return "Node: " + str(self.val) + ((" -> " + self.next.__str__()) if self.next is not None else "")

    def __next__(self):
        if self is not None:
            cur = self
            self = self.next
            return cur
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def toArray(self):
        result = []
        head = self
        while head is not None:
            result = result + [head.val]
            head = head.next
        return result

    @staticmethod
    def arrayToNode(ary):
        head = ListNode(0)
        cur = head
        for el in ary:
            node = ListNode(el)
            cur.next = node
            cur = cur.next
        return head.next
