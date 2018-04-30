#!/usr/bin/python3

"""


    An implementation of the Linked List ADT in Python 3
    =====================================================

    Copyright (c) 2018 Nilashish Chakraborty


"""

from nodes import LLNode


class LinkedList:

    def __init__(self):
        """
            Initialize the Linked List with a NULL head
        """
        self.__head = None

    def append(self, key, value):
        """
            Append a new key value pair to the Linked List
        """

        tempNode = LLNode(key, value)

        if self.__head:

            currentNode = self.__head

            while(currentNode.hasNext()):
                currentNode = currentNode.nextNode

            currentNode.nextNode = tempNode

        else:
            self.__head = tempNode

    def prepend(self, key, value):
        """
            Append a new key value pair to the Linked List
        """

        tempNode = LLNode(key, value)

        if self.__head:
            tempNode.nextNode = self.__head
            self.__head = tempNode
        else:
            self.__head = tempNode

    def insert(self, key, value, position=None):
        """
            Add a new key value pair to the Linked List.
            Use Cases:
            (a) var 'position' > length of list : Item appended
            (b) var 'position' is None : Item appended
            (c) var 'position' is 1 : Item prepended
            (d) var 'position' != 1 & <= length of list :
                Item entered at given location
       """

        if self.__head:
            if position is None or position > self.length:
                self.append(key, value)

            elif position == 1:
                self.prepend(key, value)

            else:
                tempNode = LLNode(key, value)
                print (self.length)
                currentNode = self.__head
                count = 1
                while(count != (position - 1)):
                    currentNode = currentNode.nextNode
                    count += 1
                tempNode.nextNode = currentNode.nextNode
                currentNode.nextNode = tempNode

        else:
            self.__head = tempNode

    def delete(self, position=None):
        """

            This method deletes the element at position specified.
            If no position is specified or position is greater than the
            length of the Linked List, the last element is removed.

        """

        if self.__head:
            if position == 1:
                self.__head = self.__head.nextNode

            elif position is None or position > self.length:
                self.remove()

            else:
                count = 1
                currentNode = self.__head

                while(count != (position - 1)):
                    currentNode = currentNode.nextNode
                    count += 1

                currentNode.nextNode = currentNode.nextNode.nextNode

        else:
            raise KeyError("Linked List is empty")

    def __str__(self):
        """
            A end user specific representation of the Linked List.
        """
        if self.length < 1:
            return '[]'

        tempStr = '[ '
        currentNode = self.__head

        while(currentNode.hasNext()):
            tempStr += '{0} : {1}, '.format(currentNode.key, currentNode.value)
            currentNode = currentNode.nextNode

        tempStr += '{0} : {1} ]'.format(currentNode.key, currentNode.value)
        return tempStr

    @property
    def length(self):
        """
            This method renders the length of the Linked List.
            To be used as a Property of the list.
        """
        count = 0
        currentNode = self.__head

        while(currentNode):
            currentNode = currentNode.nextNode
            count += 1

        return count

    def __getitem__(self, key):
        """
            Returns item for the passed key.
        """

        currentNode = self.__head

        while(currentNode):
            if currentNode.key == key:
                return currentNode.value
            else:
                currentNode = currentNode.nextNode

        raise KeyError("No Such Key Found")

    def remove(self, key=None):
        """

        This method removes an element in the LinkedList.
        If key is not specified it removes the last element in the Linked List.
        Else, element with the specified key is removed.

        """

        if self.length < 1:
            raise KeyError('Linked List is empty')

        if(self.__head.key == key or self.length == 1):
            self.__head = self.__head.nextNode
            return

        if key:
            currentNode = self.__head

            while(currentNode.hasNext()):
                if currentNode.nextNode.key == key:
                    currentNode.nextNode = currentNode.nextNode.nextNode
                    return
                else:
                    currentNode = currentNode.nextNode

            raise KeyError("No Such Key Found")

        else:
            currentNode = self.__head
            while(currentNode.hasNext()):
                if currentNode.nextNode.nextNode is None:
                    currentNode.nextNode = None
                    return
                else:
                    currentNode = currentNode.nextNode

    def pop(self, key=None):
        """

            This method removes and returns an element in the LinkedList.
            If key is not specified it removes and returns the last element in
            the Linked List.Else, element with the specified key is
            removed and returned.

        """

        if self.length < 1:
            raise KeyError('Linked List is empty')

        if(self.__head.key == key or self.length == 1):
            value = self.__head.value
            self.__head = self.__head.nextNode
            return value

        if key:
            currentNode = self.__head

            while(currentNode.hasNext()):
                if currentNode.nextNode.key == key:
                    value = currentNode.nextNode.value
                    currentNode.nextNode = currentNode.nextNode.nextNode
                    return value
                else:
                    currentNode = currentNode.nextNode

            raise KeyError("No Such Key Found")

        else:
            currentNode = self.__head
            while(currentNode.hasNext()):
                if currentNode.nextNode.nextNode is None:
                    value = currentNode.nextNode.value
                    currentNode.nextNode = None
                    return value
                else:
                    currentNode = currentNode.nextNode

    def reverse(self):
        """
            Iterative reversal of a Linked List
        """

        if self.length < 1:
            raise KeyError("Linked List is empty")

        elif self.length == 1:
            return

        nextNode = None
        currentNode = self.__head

        while(currentNode):
            tempNode = currentNode.nextNode
            currentNode.nextNode = nextNode
            nextNode = currentNode
            currentNode = tempNode

        self.__head = nextNode

    def reverseprint(self):
        """
            Public interface for recursive reversed printing of the Linked List
            This method calls the private version to initiate the printing.
        """
        self.__reverseprint(self.__head)

    def __reverseprint(self, currentNode):
        """
            Private method for recursive reversed printing of the Linked List.
            This method is called by the public version.
        """

        if(currentNode is None):
            return

        self.__reverseprint(currentNode.nextNode)
        print('{0} : {1}'.format(currentNode.key, currentNode.value))

    def rev_recursion(self):
        """
            Recursive reversal of a Linked List [PUBLIC INTERFACE METHOD]
        """
        self.__rev_recursion(self.__head)

    def __rev_recursion(self, currentNode):
        """
            Recursive reversal of a Linked List [PRIVATE INTERFACE METHOD]
        """

        if(currentNode.nextNode is None):
            self.__head = currentNode
            return

        self.__rev_recursion(currentNode.nextNode)
        tempNode = currentNode.nextNode
        tempNode.nextNode = currentNode
        currentNode.nextNode = None
