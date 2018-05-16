#!/usr/bin/python3

"""
    An implementation of the Binary Search Tree ADT in Python 3
    ============================================================

    Copyright (c) 2018 Nilashish Chakraborty

"""

from nodes import BSTNode
from sys import maxsize


class BinarySearchTree:

    def __init__(self):
        """
            Initialize the Binary Search Tree with a NULL root.
        """
        self.__root = None

    def insert(self, key, value):
        """
            Insert a (key, value) in the correct position.
            If the key in the passed (key, value) already exists, an Exception
            is thrown.
        """

        if self.__root and self.search(key):
            raise KeyError("Key : {0} already exists".format(key))

        if self.__root is None:
            self.__root = BSTNode(key, value)
            return

        else:
            self.__insert(self.__root, key, value)

    def __insert(self, currentNode, key, value):
        """
            Private recursive method to traverse the tree and insert the
            (key, value) in the appropriate position.
        """

        if key < currentNode.key:
            if currentNode.leftchild is None:
                currentNode.leftchild = BSTNode(key, value)
                currentNode.leftchild.parent = currentNode
            else:
                self.__insert(currentNode.leftchild, key, value)

        else:
            if currentNode.rightchild is None:
                currentNode.rightchild = BSTNode(key, value)
                currentNode.rightchild.parent = currentNode
            else:
                self.__insert(currentNode.rightchild, key, value)

    def inorder(self):
        if self.__root:
            self.__inorder(self.__root)

    def __inorder(self, currentNode):

        if currentNode:
            self.__inorder(currentNode.leftchild)
            print('{0} : {1}'.format(currentNode.key, currentNode.value))
            self.__inorder(currentNode.rightchild)

    def preorder(self):
        if self.__root:
            self.__preorder(self.__root)

    def __preorder(self, currentNode):

        if currentNode:
            print('{0} : {1}'.format(currentNode.key, currentNode.value))
            self.__preorder(currentNode.leftchild)
            self.__preorder(currentNode.rightchild)

    def postorder(self):
        if self.__root:
            self.__postorder(self.__root)

    def __postorder(self, currentNode):

        if currentNode:
            self.__postorder(currentNode.leftchild)
            self.__postorder(currentNode.rightchild)
            print('{0} : {1}'.format(currentNode.key, currentNode.value))

    def height(self):
        """
            Returns the height of the tree starting from 0.
        """

        if self.__root:
            return self.__height(self.__root, -1)
        else:
            raise KeyError("Tree is empty")

    def __height(self, currentNode, currentHeight):
        """
            This method recursively traverses the tree to find the
            height of the Tree.
        """
        if currentNode is None:
            return currentHeight

        leftHeight = self.__height(currentNode.leftchild, currentHeight + 1)
        rightHeight = self.__height(currentNode.rightchild, currentHeight + 1)

        return max(leftHeight, rightHeight)

    def search(self, key):
        """
            This method searches the Binary Search Tree and returns the
            True if key is present, else returns False.
        """
        if self.__root:
            return self.__search(self.__root, key)
        else:
            raise KeyError("Tree is empty")

    def __search(self, currentNode, key):

        if key == currentNode.key:
            return True

        elif key < currentNode.key and currentNode.leftchild:
            return self.__search(currentNode.leftchild, key)

        elif key > currentNode.key and currentNode.rightchild:
            return self.__search(currentNode.rightchild, key)

        return False

    def find(self, key):
        """
            This method searches the Binary Search Tree and returns the
            Node if a Node with that key is present, else returns None.
        """
        if self.__root:
            return self.__find(self.__root, key)
        else:
            raise KeyError("Tree is empty")

    def __find(self, currentNode, key):

        if key == currentNode.key:
            return currentNode

        elif key < currentNode.key and currentNode.leftchild:
            return self.__find(currentNode.leftchild, key)

        elif key > currentNode.key and currentNode.rightchild:
            return self.__find(currentNode.rightchild, key)

        return None

    def __findMin(self, node):
        """
            Returns Node with the minimum Key in the given Tree
        """
        currentNode = node

        while currentNode.leftchild:
            currentNode = currentNode.leftchild

        return currentNode

    def delete(self, key):

        if not self.search(key):
            raise KeyError("Key : {0} not found".format(key))

        return self.__delete_node(self.find(key))

    def __delete_node(self, currentNode):

        parent = currentNode.parent

        # Calculate number of children of the node to be deleted
        number_of_children = currentNode.number_of_children

        if number_of_children == 0:

            """

                All the nodes except for the root will have a parent.
                So if parent is none & number of children is 0, the node
                to be deleted is the root itself.

            """

            if parent:
                if parent.leftchild == currentNode:
                    parent.leftchild = None
                else:
                    parent.rightchild = None
            else:
                self.__root = None

        elif number_of_children == 1:

            child = currentNode.leftchild if currentNode.leftchild \
                else currentNode.rightchild

            """

                All the nodes except for the root will have a parent.
                So if parent is none & number of children is 1, the node
                to be deleted is the root itself and it's single child will
                replace it.

            """

            if parent:

                if parent.leftchild == currentNode:
                    parent.leftchild = child
                else:
                    parent.rightchild = child

            else:
                self.__root = child

            # Assign the correct parent pointer to the single child
            child.parent = parent

        else:
            # Inorder Successor : Minimum in right subtree
            inorder_successor = self.__findMin(currentNode.rightchild)

            # Replace the node to be deleted with it's inorder successor
            currentNode.key = inorder_successor.key
            currentNode.value = inorder_successor.value

            # Delete the copy of the inorder successor recursively
            self.__delete_node(inorder_successor)

    @staticmethod
    def validateBST(tree):
        """
            If the passed item is an instance of Binary Search Tree,
            then the root of the tree is sent for validation.

            If the passed item is an instance of BSTNode, then the item itself
            is sent for validation since it must be the root of the
            desired tree.

        """
        if isinstance(tree, BinarySearchTree):
            return BinarySearchTree.__validateBST(tree.__root)

        elif isinstance(tree, BSTNode):
            return BinarySearchTree.__validateBST(tree)

        else:
            raise TypeError('validateBST() not applicable on object of type {0}\
            '.format(type(tree)))

    @staticmethod
    def __validateBST(currentNode, minkey=-1, maxkey=maxsize):
        if currentNode is None:
            return True

        if currentNode.key <= minkey or currentNode.key >= maxkey:
            return False

        return BinarySearchTree.__validateBST(currentNode.leftchild, minkey,
                                              currentNode.key) and \
            BinarySearchTree.__validateBST(currentNode.rightchild,
                                           currentNode.key, maxkey)
