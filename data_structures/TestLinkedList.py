import unittest
import LinkedList as ll
import numpy as np
import sys


class TestLinkedList(unittest.TestCase):
    def testArrayEquals(self):
        lst = [1, 2, 3, 4, 5]
        linked_lst = ll.LinkedList(fromArray=lst)

        # self.assertEquals(expected, observed)
        self.assertEqual(lst, linked_lst.toArray())

    def testAddFirst(self):
        lst = [1, 3, 5, 7, 9]
        linked_lst = ll.LinkedList()
        linked_lst.addFirst(lst[-1])
        lst = lst[:-1]

        print(linked_lst.toArray())

        for i in range(len(lst)-1, -1, -1):
            linked_lst.addFirst(lst[i])

        self.assertEqual([1, 3, 5, 7, 9], linked_lst.toArray())

    def testAddLast(self):
        lst = [1, 3, 5, 7, 9]
        linked_lst = ll.LinkedList()
        linked_lst.addLast(lst[-1])
        lst = lst[:-1]

        print(str(linked_lst.toArray()))

        for i in range(len(lst)-1, -1, -1):
            linked_lst.addLast(lst[i])

        self.assertEqual(list(reversed([1, 3, 5, 7, 9])), linked_lst.toArray())

    def testRemoveFirst(self):
        lst = [1, 3, 5, 7, 9]
        linked_lst = ll.LinkedList(fromArray=lst)
        linked_lst.removeFirst()
        lst = lst[1:]

        print(linked_lst.toArray())

        for i in range(len(lst)):
            linked_lst.removeFirst()

        self.assertEqual([], linked_lst.toArray())

    def testRemoveLast(self):
        lst = [1, 3, 5, 7, 9]
        linked_lst = ll.LinkedList(fromArray=lst)
        linked_lst.removeLast()
        lst = lst[:-1]

        print(linked_lst.toArray())

        for i in range(len(lst)):
            linked_lst.removeLast()

        self.assertEqual([], linked_lst.toArray())

    def testRandomArrayEquals(self):
        lst = np.random.randint(sys.maxsize, size=10)
        linked_lst = ll.LinkedList(fromArray=lst)
        ops = ['addFirst', 'addLast', 'removeFirst', 'removeLast']

        for i in range(50):
            op = ops[np.random.randint(len(ops))]
            e = np.random.randint(sys.maxsize)

            if op == 'addFirst':
                lst = [e] + lst
            elif op == 'addLast':
                lst += [e]
            elif op == 'removeFirst':
                lst = lst[1:]
            else:
                lst = lst[:-1]

            if 'add' not in op:
                exec('linked_lst.' + op + '()')
                continue

            exec('linked_lst.' + op + '(' + str(e) + ')')

        print(str(lst))
        print(str(linked_lst.toArray()))
        self.assertEqual(lst, linked_lst.toArray())

# Run the Tests
    if __name__ == '__main__':
        unittest.main()




