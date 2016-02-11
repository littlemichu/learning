# Tests for Chapter Two of CTCI
from sets import Set
import unittest

from ch02.src import solutions
from shared.src import data_structures

class ChapterTwoQuestionsTestCase(unittest.TestCase):

    def setUp(self):
        linked = data_structures.LinkedList()
        data = [1,5,1,1,4,5,2,3,0]
        for d in data:
            linked.add(d)
        self.linked = linked
        self.data = data
        
    def test_remove_duplicates(self):
        linked = self.linked
        unique_data = Set(linked.get_data())
        solutions.remove_duplicates(linked)
        data = linked.get_data()
        self.assertEqual(len(data), len(unique_data), 'incorrect number of nodes '
                         'after removal of duplicates')
        for x in unique_data:
            self.assertTrue(x in data, 'data missing after removal of duplicates')

    def test_get_kth_to_last(self):
        for k in range(len(self.data)):
            kth_node = solutions.get_kth_to_last(self.linked, k)
            self.assertEqual(kth_node.data, self.data[len(self.data) - 1 - k],
                             'incorrect node returned by '
                             'get_kth_to_last method')

    def test_delete_node(self):
        data = self.data[:]
        n = 5
        delete_node = self.linked.get_nth_node(n)
        solutions.delete_node(delete_node)
        self.assertEqual(self.linked.get_data(), data[:n] + data[n + 1:],
                         'incorrect deletion of node by delete_node method')

    def test_partition(self):
        x = 3
        less_than_x_count = 0
        
        # Count values less than x
        for d in self.data:
            if d < x:
                less_than_x_count += 1

        solutions.partition(self.linked, x)

        curr_p = self.linked.head
        i = 0
        # Check values 'less than x' come first, followed by values '>= x'
        while curr_p:
            if i < less_than_x_count:
                self.assertLess(curr_p.data, x, 'data in front not less than '
                                'x after partition method was called')
            else:
                self.assertGreaterEqual(curr_p.data, x, 'data in back not '
                                        'greater than or equal to x after '
                                        'partition method was called')
            curr_p = curr_p.next
            i += 1
                
    def test_sum_linked_lists(self):
        data1 = [1, 2, 3] # 321
        data2 = [0, 9, 1] # 190
        data3 = [0, 9, 7] # 790
        expected_sum1 = [1, 1, 5] # 321 + 190 = 511 - Test carry over
        expected_sum2 = [1, 1, 1, 1] # 321 + 790 = 1111 - Test carry over at end
        
        # Create linked lists
        linked1 = data_structures.LinkedList()
        linked2 = data_structures.LinkedList()
        linked3 = data_structures.LinkedList()

        # Initiate linked lists' data
        for d1, d2, d3 in zip(data1, data2, data3):
            linked1.add(d1)
            linked2.add(d2)
            linked3.add(d3)

        linked_sum1 = solutions.sum_linked_lists(linked1, linked2)
        linked_sum2 = solutions.sum_linked_lists(linked1, linked3)
        self.assertEqual(linked_sum1.get_data(), expected_sum1, 'incorrect sum '
                         'after adding linked1 and linked2 linked lists')
        self.assertEqual(linked_sum2.get_data(), expected_sum2, 'incorrect sum '
                         'after adding linked1 and linked3 linked lists')

    def test_pad_with_zeroes(self):
        data1 = [3, 2, 1] # 321
        data2 = [2] # 2
        expected1 = (data1, [0, 0, 2]) # 321 + 2 --> 321 + 002

        data3 = [1, 9, 0] # 190
        expected2 = (data1, data3) # 321 + 190 --> 321 + 190

        # Create linked lists
        linked1 = data_structures.LinkedList()
        linked2 = data_structures.LinkedList()
        linked3 = data_structures.LinkedList()
        linked1_pad1 = data_structures.LinkedList()
        linked2_pad1 = data_structures.LinkedList()
        linked1_pad2 = data_structures.LinkedList()
        linked3_pad2 = data_structures.LinkedList()
        
        # Initiate data in linked lists
        linked1.add_arr(data1)
        linked2.add_arr(data2)
        linked3.add_arr(data3)

        # Pad linked lists
        linked1_pad1.head, linked2_pad1.head = solutions.pad_with_zeroes(linked1.head, linked2.head)
        linked1_pad2.head, linked3_pad2.head = solutions.pad_with_zeroes(linked1.head, linked3.head)

        # Convert results to tuples
        result1 = (linked1_pad1.get_data(), linked2_pad1.get_data())
        result2 = (linked1_pad2.get_data(), linked3_pad2.get_data())

        # Check actual results against expected results
        self.assertEqual(result1, expected1, 'linked1 and linked2 were not padded correctly')
        self.assertEqual(result2, expected2, 'linked1 and linked3 were not padded correctly')

    def test_sum_linked_lists_follow_up(self):
        data1 = [3, 2, 1] # 321
        data2 = [2] # 2
        expected1 = [3, 2, 3] # 321 + 2 = 322

        data3 = [7, 9, 0] # 790
        expected2 = [1, 1, 1, 1] # 321 + 790 = 1111

        # Create linked lists
        linked1 = data_structures.LinkedList()
        linked2 = data_structures.LinkedList()
        linked3 = data_structures.LinkedList()

        # Initiate data in linked lists
        linked1.add_arr(data1)
        linked2.add_arr(data2)
        linked3.add_arr(data3)

        # Compute sums
        result1 = solutions.sum_linked_lists_follow_up(linked1.head, linked2.head)
        result2 = solutions.sum_linked_lists_follow_up(linked1.head, linked3.head)
        
        # Check actual results against expected results
        self.assertEqual(result1.get_data(), expected1, 'linked1 and linked2 '
                         'were not added correctly')
        self.assertEqual(result2.get_data(), expected2, 'linked1 and linked2 '
                         'were not added correctly')

    def test_get_loop_start(self):
        # Create nodes
        nodeA = data_structures.Node('A')
        nodeB = data_structures.Node('B')
        nodeC = data_structures.Node('C')
        nodeD = data_structures.Node('D')
        nodeE = data_structures.Node('E')

        # Link nodes together to form circular linked list:
        # A -> B -> C -> D -> E -> C
        nodeA.next = nodeB
        nodeB.next = nodeC
        nodeC.next = nodeD
        nodeD.next = nodeE
        nodeE.next = nodeC

        self.assertEqual(solutions.get_loop_start(nodeA), nodeC, 'wrong node '
                         'returned as the start of the loop in the circular '
                         'linked list')
        self.assertEqual(solutions.get_loop_start(self.linked.head), None, 'nothing '
                                            'should be returned since this '
                                            'linked list is not circularly '
                                            'linked')
        
    def test_is_palindrome(self):
        # Create linked lists
        linked1 = data_structures.LinkedList()
        linked2 = data_structures.LinkedList()
        linked3 = data_structures.LinkedList()
        linked4 = data_structures.LinkedList()
        linked5 = data_structures.LinkedList()
        linked6 = data_structures.LinkedList()

        # Initialize data in linked lists
        linked1.add_arr([1,2,3,4])
        linked2.add_arr([1,2,3,4,5])
        linked3.add_arr([1,2,2,1])
        linked4.add_arr([1,2,3,2,1])
        linked5.add_arr([1])
        linked6.add_arr([])

        # Expected results
        expected1 = False
        expected2 = False
        expected3 = True
        expected4 = True
        expected5 = True
        expected6 = False

        # Test
        self.assertEqual(solutions.is_palindrome(linked1.head), expected1,
                         'incorrect, this is not a palindrome')
        self.assertEqual(solutions.is_palindrome(linked2.head), expected2,
                         'incorrect, this is not a palindrome')
        self.assertEqual(solutions.is_palindrome(linked3.head), expected3,
                         'incorrect, this is a palindrome')
        self.assertEqual(solutions.is_palindrome(linked4.head), expected4,
                         'incorrect, this is a palindrome')
        self.assertEqual(solutions.is_palindrome(linked5.head), expected5,
                         'incorrect, this is a palindrome')
        self.assertEqual(solutions.is_palindrome(linked6.head), expected6,
                         'incorrect, this is a palindrome')
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(ChapterTwoQuestionsTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
