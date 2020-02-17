import datetime as dt


class Interval:
    def __init__(self, left, right, count=0, closed='left'):
        self.left = left
        self.right = right
        self.closed = closed
        self.count = count
        self.width = self.right - self.left

        if isinstance(self.left, dt.datetime) & isinstance(self.right, dt.datetime):
            delta = (self.right - self.left) / 2
            self._mid = self.left + delta
        else:
            self._mid = (self.left + self.right) / 2

    def to_string(self):
        print_string = ''

        if self.closed == 'left':
            print_string = f"Interval:[{self.left},{self.right}) \n"

        elif self.closed == 'right':
            print_string = f"Interval:({self.left},{self.right}] \n"

        elif self.closed == 'both':
            print_string = f"Interval:[{self.left},{self.right}] \n"

        elif self.closed == 'none':
            print_string = f"Interval:({self.left},{self.right}) \n"

        print_string += f"Midpoint: {self._mid} \n"
        print_string += f"Count: {self.count}"

        return print_string

    def is_in(self, x):
        if self.closed == 'left':
            if self.left <= x < self.right:
                return True
            else:
                return False

        elif self.closed == 'right':
            if self.left < x <= self.right:
                return True
            else:
                return False

        elif self.closed == 'both':
            if self.left <= x <= self.right:
                return True
            else:
                return False

        elif self.closed == 'none':
            if self.left < x < self.right:
                return True
            else:
                return False

    def set_count(self, x):
        self.count = x

    def add_count(self, x):
        self.count += x

    def plot_info(self):
        return self._mid, self.width, self.count

    def __eq__(self, other):
        if self.left == other.left and self.right == other.right and self.closed == other.closed:
            return True
        else:
            return False
