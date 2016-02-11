# Tests for Chapter Three of CTCI
import unittest

from ch03.src import solutions

class ChapterThreeQuestionsTestCase(unittest.TestCase):

    def setUp(self):
        # Set up three stacks initiated with data:
        # Stack 0: 0, 1, 2, 3
        # Stack 1: 4, 5, 6, 7
        # Stack 2: 8, 9, 10, 11
        # stacks.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.num_stacks = 3
        self.stack_size = 4
        stacks_filled = solutions.Stacks(self.num_stacks, self.stack_size)
        value = 0
        for stack in range(self.num_stacks):
            for index in range(self.stack_size):
                stacks_filled.push(stack, value)
                value += 1
        self.stacks_filled = stacks_filled

        # Set up three stacks initiated with None:
        # Stack 0: None, None, None, None
        # Stack 1: None, None, None, None
        # Stack 2: None, None, None, None
        # stacks.arr = [None, None, None, None,
        #               None, None, None, None,
        #               None, None, None, None]
        stacks_empty = solutions.Stacks(self.num_stacks, self.stack_size)
        self.stacks_empty = stacks_empty

    # Question 3.1 tests
    def test_stacks_push(self):
        stacks_empty = self.stacks_empty
        expected_arr = [x for x in range(len(stacks_empty.arr))]
        value = 0
        for stack in range(self.num_stacks):
            for index in range(self.stack_size):
                stacks_empty.push(stack, value)
                value += 1
        self.assertEqual(stacks_empty.arr, expected_arr, 'push method did not '
                    'function as expected')

    def test_stacks_pop(self):
        stacks_filled = self.stacks_filled
        for stack in range(self.num_stacks):
            for offset in range(self.stack_size - 1, -1, -1):
                i = stack * self.stack_size + offset
                expected_value = stacks_filled.arr[i]
                popped_value = stacks_filled.pop(stack)
                self.assertEqual(popped_value, expected_value,
                                 'pop method returned wrong value')

    def test_stacks_peek(self):
        stacks_filled = self.stacks_filled
        for i in range(3):
            peek_val = stacks_filled.peek(0)
            calc_val = stacks_filled.arr[self.stack_size - 1]
            self.assertEqual(stacks_filled.peek(0),
                             stacks_filled.arr[self.stack_size - 1],
                             'peek method returned incorrect value')
            self.assertEqual(stacks_filled.peek(1),
                             stacks_filled.arr[2*self.stack_size - 1],
                             'peek method returned incorrect value')

    # Question 3.2 tests
    def test_stack_with_min_push(self):
        stack = solutions.StackWithMin()
        data = [1, 2, 3, -1, -1, 2]
        expected_min = [1, 1, 1, -1, -1, -1]
        for d, m in zip(data, expected_min):
            stack.push(d)
            self.assertEqual(stack.get_min(), m, 'wrong min returned after new '
                        'value pushed onto stack')

    def test_stack_with_min_pop(self):
        stack = solutions.StackWithMin()
        data = [1, 2, 3, -1, -1, 2]
        expected_min = [1, 1, 1, -1, -1, -1]
        expected_min.reverse()
        for d in data:
            stack.push(d)
        data.reverse()
        for m, d in zip(expected_min, data):
            self.assertEqual(stack.get_min(), m, 'wrong min returned after pop '
                             'method invoked')
            self.assertEqual(stack.pop(), d, 'wrong value returned for pop '
                             'method')

    # Question 3.3 tests
    def test_set_of_stacks_push(self):
        stack = solutions.SetOfStacks(3)
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
        for row in data:
            for col in row:
                stack.push(col)
        self.assertEqual(stack.stacks, data, 'push method failed')

    def test_set_of_stacks_pop(self):
        stack = solutions.SetOfStacks(3)
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
        for row in data:
            for col in row:
                stack.push(col)
        results = [x for x in range(9, 0, -1)]
        for result in results:
            self.assertEqual(stack.pop(), result, 'pop method failed')
    
    # Question 3.4 tests
    def test_pad_towers(self):
        test_cases = []
        test_cases.append([[5, 4], [3], [2, 1]])
        test_cases.append([[5, 4, 3, 2, 1], [], []])
        test_cases.append([[], [], [5, 4, 3, 2, 1]])
        expected_results = []
        expected_results.append([[5, 4], [3, 0], [2, 1]])
        expected_results.append([[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        expected_results.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [5, 4, 3, 2, 1]])
    
        for towers, expected in zip(test_cases, expected_results):
            self.assertEqual(solutions.pad_towers(towers), expected, 'pad_towers method failed')
            
    def test_print_towers(self):
        tower_test_cases = []
        tower_test_cases.append([[5, 4], [3], [2, 1]])
        tower_test_cases.append([[5, 4, 3, 2, 1], [], []])
        tower_test_cases.append([[], [], [5, 4, 3, 2, 1]])
        for towers in tower_test_cases:
            solutions.print_towers(towers)

    def test_validate_towers(self):
        test_cases = []
        test_cases.append(([[5, 4], [3], [2, 1]], True))
        test_cases.append(([[5, 4, 3, 2, 1], [], []], True))
        test_cases.append(([[], [], [1, 2, 3, 4, 5]], False))
        test_cases.append(([[5, 4], [3], [1, 2]], False))
        for towers, is_valid in test_cases:
            if not is_valid:
                self.assertRaises(ValueError, solutions.validate_towers, towers)
            else:
                solutions.validate_towers(towers)

    def test_solve_towers(self):
        test_cases = []
        test_cases.append(([[5, 4, 3, 2, 1], [], []], [[], [], [5, 4, 3, 2, 1]]))
        test_cases.append(([[3, 2, 1], [], []], [[], [], [3, 2, 1]]))
        test_cases.append(([[4, 3, 2, 1], [], []], [[], [], [4, 3, 2, 1]]))
        for towers, result in test_cases:
            self.assertEqual(solutions.solve_towers(towers), result, 'solve_towers method failed')

    # Question 3.5 Tests
    def test_insert(self):
        # Prepare two tests
        queues = []
        queues.append(solutions.MyQueue())
        queues.append(solutions.MyQueue())
        arrs = []
        arrs.append([x for x in range(10)])
        arrs.append([1])

        # Insert each item into the queues for each test
        for arr, queue in zip(arrs, queues):
            for item in arr[::-1]:
                queue.insert(item)
            # Check that all items in the test have been correctly inserted
            # into the queue
            self.assertEqual(queue.stacks[0].arr, arr[::-1], 'queue insert method failed')
        
    def test_remove(self):
        # Prepare two tests
        queues = []
        queues.append(solutions.MyQueue())
        queues.append(solutions.MyQueue())
        arrs = []
        arrs.append([x for x in range(10)])
        arrs.append([1])
        # Insert each item into the queues for each test
        for arr, queue in zip(arrs, queues):
            for item in arr:
                queue.insert(item)

        # For each test, remove the first item and check for equality:
	# Check that the item returned was correct.
	# Check that the item was actually removed.
        # - arr: remove manually via list manipulation
        # - queue: remove via queue's remove method
        for arr, queue in zip(arrs, queues):
            for n in range(len(arr)):
                arr_val = arr.pop(0)
                queue_val = queue.remove()
                self.assertEqual(arr_val, queue_val,
                                 'queue remove method returned the wrong value')
                self.assertEqual(queue.stacks[0].arr, arr,
                                 'queue remove method left stacks in wrong state')
        
    
    def test_examine(self):
        pass #TODO
    
suite = unittest.TestLoader().loadTestsFromTestCase(ChapterThreeQuestionsTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
