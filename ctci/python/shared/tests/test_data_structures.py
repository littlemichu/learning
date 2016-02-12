# Tests for data_structures module
import unittest

from shared.src import data_structures

class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        linked = data_structures.LinkedList()
        data = [1,5,1,1,4,5,2,3,0]
        for d in data:
            linked.add(d)

        self.linked = linked
        self.data = data

    def test_add(self):
        linked = data_structures.LinkedList()
        data = self.data[:]
        # Add each element of data one at a time and assert that
        # the data returned from the linked list includes the added element
        for i in range(len(data)):
            linked.add(data[i])
            self.assertEquals(linked.get_data(), data[:i + 1],
                              'element not added to linked list properly '
                              'after calling LinkedList.add method')

    def test_remove(self):
        linked = self.linked
        data = self.data

        # Test removing data that is not in linked list
        linked.remove(-1)
        self.assertEquals(linked.get_data(), data, 'incorrect removal of '
                          'data that is not in linked list')

        # Test removing from front all the way to last node
        for i in range(len(data)):
            linked.remove(data[i])
            self.assertEquals(linked.get_data(), data[i + 1:])

        # Test removing from empty linked list
        linked.remove(1)
        self.assertEquals(linked.get_data(), [], 'incorrect removal from '
                          'empty linked list')

    def test_get_nth_node(self):
        linked = self.linked
        data = self.data

        for n in range(len(data)):
            nth_node = linked.get_nth_node(n)
            self.assertEqual(nth_node.data, data[n], 'wrong node retrieved for '
                        'get_nth_node method')

    def test_get_data(self):
        self.assertEqual(self.linked.get_data(), self.data, 'wrong data retrieved '
                    'for get_data method')

linked_list_suite = unittest.TestLoader().loadTestsFromTestCase(LinkedListTestCase)
unittest.TextTestRunner(verbosity=2).run(linked_list_suite)
