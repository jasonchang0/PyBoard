class LinkedList(object):

    def __init__(self, head=None, fromArray=None):
        if head and fromArray:
            raise Exception('Bad Argument!')

        if fromArray is not None:
            self._fromArray(fromArray)
            return

        self.sentinel = 0
        self.head = self.Node(val=self.sentinel)
        self.tail = self.head
        self.size = 0

        if head:
            new_node = self.Node(val=self.head)
            self.head.next = new_node
            self.tail = new_node
            self.size += 1

    class Node(object):

        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

        def hasNext(self):
            return self.next
        
    def add(self, index, element):
        i_site = self.head.next

        if index > self.size:
            raise Exception('Bad Index.')

        for i in range(index):
            i_site = i_site.next

        i_site.next = i_site
        i_site.val = element
        self.size += 1

    def addFirst(self, e):
        self.head.next = self.Node(e, self.head.next)
        self.size += 1

    def addLast(self, e):
        if self.isEmpty():
            new_node = self.Node(val=e)
            self.head.next = new_node
            self.tail = new_node
            self.size += 1
            return

        i_site = self.head.next

        while i_site.hasNext():
            i_site = i_site.next

        i_site.next = self.Node(val=e)
        self.tail = i_site.next
        self.size += 1

    def clear(self):
        self.__init__()

    def clone(self):
        return self.head

    def isEmpty(self):
        return not self.size

    def contain(self, e):
        current = self.head

        while not current:
            if current.val == e or current.val is e:
                return True

            current = current.next

        return False

    def getFirst(self):
        return self.head.val

    def getLast(self):
        return self.tail.val

    def indexOf(self, e):
        current = self.head.next
        index = 0

        while not current:
            if current.val == e or current.val is e:
                return index

            current = current.next
            index += 1

        return -1

    def remove(self, index):
        r_site = self.head.next

        if index > self.size:
            raise Exception('Bad Index.')

        for i in range(index):
            r_site = r_site.next

        r_site.next = None
        self.size -= 1

    def removeFirst(self):
        if not self.isEmpty():
            self.head.next = self.head.next.next
            self.size -= 1

    def removeLast(self):
        current = self.head.next

        if not current or current.hasNext():
            self.__init__()
            return

        while current.next.next:
            current = current.next

        current.next = None
        self.size -= 1

    def set(self, index, element):
        s_site = self.head.next

        if index >= self.size:
            raise Exception('Bad Index.')

        for i in range(index):
            s_site = s_site.next
            s_site.val = element

    def _fromArray(self, arr):
        self.__init__(head=arr[0])
        # self.head = self.Node(val=arr[0])
        # self.tail = self.head.next
        # self.size = 0

        for i in arr[1:]:
            self.addLast(i)

    def toArray(self):
        out_array = []
        current = self.head.next

        if self.isEmpty():
            return out_array

        while current.hasNext():
            out_array += [current.val]
            current = current.next
            # print(out_array)

        out_array.append(current.val)

        return out_array







