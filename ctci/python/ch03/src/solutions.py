# Questions from Chapter Three of CTCI - Stacks and Queues
import sys

# Question 3.1
class Stacks(object):
    class StackFullError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

    class StackEmptyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
        
    class MiniStack(object):
        def __init__(self, size, start_i):
            if size < 1 or start_i < 0:
                raise ValueError('size must be an integer value >= 1, '
                                 'and start index must be >= 0')
            self.size_limit = size
            self.start_i = start_i
            self.top_i = start_i

        def size(self):
            return self.top_i - self.start_i
        
        # Returns index to insert value at
        def push(self):
            if self.size() == self.size_limit:
                return -1
            self.top_i += 1
            return self.top_i - 1

        # Returns index to pop value from
        def pop(self):
            if self.size() == 0:
                return -1
            self.top_i -= 1
            return self.top_i

        # Returns index to peek
        def peek(self):
            if self.size() == 0:
                return -1
            return self.top_i - 1
            
    def __init__(self, num_stacks, stack_size):
        self.arr = [None for x in range(num_stacks * stack_size)]
        stacks = []
        # Initiate a MiniStack for each stack requested
        for n in range(num_stacks):
            stacks.append(self.MiniStack(stack_size, n * stack_size))
        self.stacks = stacks

    def push(self, stack, value):
        index = self.stacks[stack].push()
        if index < 0:
            raise StackFullError('Unable to insert because stack is full')
        self.arr[index] = value

    def pop(self, stack):
        index = self.stacks[stack].pop()
        if index < 0:
            raise StackEmptyError('Stack is empty, nothing to return')
        return self.arr[index]

    def peek(self, stack):
        index = self.stacks[stack].peek()
        if index < 0:
            raise StackEmptyError('Stack is empty, nothing to look at')
        return self.arr[index]

# Question 3.2
class StackWithMin(object):
    def __init__(self):
        self.arr = []
        self.min_arr = [sys.maxsize]

    def get_min(self):
        if not self.min_arr:
            return sys.maxsize
        return self.min_arr[len(self.min_arr) - 1]
    
    def push(self, val):
        if val <= self.get_min():
            self.min_arr.append(val)
        self.arr.append(val)

    def pop(self):
        popped = self.arr.pop()
        if popped == self.get_min():
            self.min_arr.pop()
        return popped

# Question 3.3
class SetOfStacks(object):
    class StackEmptyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stacks = []
        self.stacks.append([])
        self.num_stacks = 1

    def __is_max_size(self):
        size = len(self.stacks[self.num_stacks - 1])
        return size == self.stack_size

    def __add_new_stack(self):
        self.stacks.append([])
        self.num_stacks += 1

    def __remove_empty_stack(self):
        self.stacks.pop()
        self.num_stacks -= 1
        
    def push(self, value):
        if self.__is_max_size():
            self.__add_new_stack()
        self.stacks[self.num_stacks - 1].append(value)

    def pop(self):
        if not self.stacks[self.num_stacks - 1]:
            if self.num_stacks > 1:
                self.__remove_empty_stack()
            else:
                raise StackEmptyError('Nothing to pop, stack is empty')
        return self.stacks[self.num_stacks - 1].pop()

# Question 3.4
# Return an 2d array padded to the max tower height with zeroes
# Example:
#  [[5, 4], [3], [2, 1]]  --> [[5, 4], [3, 0], [2, 1]]
def pad_towers(towers):
    max_plates = 0
    for tower in towers:
        if len(tower) > max_plates:
            max_plates = len(tower)

    padded = []
    for tower in towers:
        padded_tower = tower[:]
        while len(padded_tower) < max_plates:
            padded_tower.append(0)
        padded.append(padded_tower)
    return padded

def count_plates(towers):
    count = 0
    for tower in towers:
        for plate in tower:
            count += 1
    return count

# Print a pictoral depiction of the towers
# Example:
# [[5, 4], [3], [2, 1]]
#
#  ****        *
#  ***** ***   **
#  1     2     3
def print_towers(towers):
    padded = pad_towers(towers)
    width = count_plates(towers)
    print "\n\n"
    for t1, t2, t3 in zip(padded[0][::-1], padded[1][::-1], padded[2][::-1]):
        print "{0:<{width}} {1:<{width}} {2:<{width}}".format(t1*"*", t2*"*", t3*"*", width=width)
    print "{0:<{width}} {1:<{width}} {2:<{width}}".format(1, 2, 3, width=width)

# Validates that each tower has plates stacked in decrementing order
# Example:
# [[5, 4, 3, 2, 1], [], []] --> Valid
# [[1, 2, 3, 4, 5], [], []] --> Invalid
def validate_towers(towers):
    for tower in towers:
        if tower and tower[0]:
            prev_plate = tower[0]
            for plate in tower:
                if plate > prev_plate:
                    raise ValueError('Towers of Hanoi in an invalid state')
                prev_plate = plate

def move_plates(towers, n, start, finish, transition):
    if n == 0:
        return
    elif n > 0:
        move_plates(towers, n-1, start, transition, finish)
        towers[finish].append(towers[start].pop())
        # print_towers(towers)
        move_plates(towers, n-1, transition, finish, start)
        validate_towers(towers)

def solve_towers(towers):
    if towers:
        if towers[0]:
            n = len(towers[0])
            start = 0
            finish = 2
            transition = 1
            try:
                move_plates(towers, n, start, finish, transition)
            except ValueError as e:
                print e
                print_towers(towers)
    return towers

# Question 3.5
# Implement a MyQueue class which implements a queue using two stacks
class MyQueue(object):
    class QueueEmptyError(Exception):
        def __init__(self, value):
	    self.value = value
	def __str__(self):
	    return repr(self.value)

    class Stack(object):
        class StackEmptyError(Exception):
            def __init__(self, value):
                self.value = value
            def __str__(self):
                return repr(self.value)
            
        def __init__(self):
            self.arr = []

        def push(self, value):
            self.arr.append(value)

        def pop(self):
            if self.arr:
                return self.arr.pop()
            else:
                raise self.StackEmptyError('stack is empty')

        def peek(self):
            if self.arr:
                return self.arr[len(arr) - 1]
            else:
                raise self.StackEmptyError('stack is empty')

        def is_empty(self):
            if self.arr:
                return False
            return True

    # Move all elements in stack-start_i to stack-finish_i
    def __move(self, start_i, finish_i):
        while self.stacks[start_i].arr:
            value = self.stacks[start_i].pop()
            self.stacks[finish_i].push(value)
        
    def __init__(self):
        stacks = []
        stacks.append(self.Stack())
        stacks.append(self.Stack())
        self.stacks = stacks

    # Insert an element into the "queue"
    def insert(self, value):
        self.stacks[0].push(value)

    # Remove an element from the "queue"
    # Throws QueueEmptyError
    def remove(self):
        self.__move(0, 1)
	try:
            value = self.stacks[1].pop()
	except StackEmptyError:
	    raise QueueEmptyError("queue is empty")
        self.__move(1, 0)
        return value

    def examine(self):
        self.__move(0, 1)
        value = self.stacks[1].peek()
        self.__move(0, 1)
        return value
