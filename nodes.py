#!/usr/bin/python3

"""
    A collection of all the Node types required for the
    implemented data structures.
"""


class LLNode:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__nextNode = None

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def nextNode(self):
        return self.__nextNode

    @key.setter
    def key(self, key):
        self.__key = key

    @value.setter
    def value(self, value):
        self.__value = value

    @nextNode.setter
    def nextNode(self, nextNode):
        self.__nextNode = nextNode

    def __str__(self):
        return ('Key : {0} Value : {1}'.format(self.key, self.value))

    def hasNext(self):
        if self.nextNode:
            return True
        else:
            return False


class BSTNode:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__leftchild = None
        self.__rightchild = None
        self.__parent = None

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def leftchild(self):
        return self.__leftchild

    @property
    def rightchild(self):
        return self.__rightchild

    @property
    def parent(self):
        return self.__parent

    @key.setter
    def key(self, key):
        self.__key = key

    @value.setter
    def value(self, value):
        self.__value = value

    @leftchild.setter
    def leftchild(self, leftchild):
        self.__leftchild = leftchild

    @rightchild.setter
    def rightchild(self, rightchild):
        self.__rightchild = rightchild

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    def __str__(self):
        return ('{0} : {1}'.format(self.key, self.value))

    @property
    def number_of_children(self):
        count = 0

        if self.leftchild:
            count += 1
        if self.rightchild:
            count += 1

        return count

    @number_of_children.setter
    def number_of_children(self, count):
        raise TypeError("Assignment not allowed")
