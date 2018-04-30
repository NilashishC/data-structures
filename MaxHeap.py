#!/usr/bin/python3

"""


    An implementation of the MAX HEAP ADT & Heap Sort Algorithm in Python 3
    ========================================================================

    Copyright (c) 2018 Nilashish Chakraborty


"""


class Heap:

    @staticmethod
    def build_max_heap(seq):
        """
            This method builds a max heap from the passed sequence.
        """

        n = len(seq)

        temp = int((n / 2))

        # Call MAX_HEAPIFY(A, i)
        for i in range(temp, -1, -1):
            Heap.__max_heapify(seq, n, i)

    @staticmethod
    def __max_heapify(seq, n, i):

        left_child_index = (2 * i) + 1
        right_child_index = (2 * i) + 2
        largest = i

        heapsize = n

        if(left_child_index < heapsize and seq[i] < seq[left_child_index]):
            largest = left_child_index

        if(right_child_index < heapsize and seq[largest]
           < seq[right_child_index]):
            largest = right_child_index

        if(largest != i):
            seq[i], seq[largest] = seq[largest], seq[i]

            """

            Recursively call MAX_HEAPIFY(A, i) to preserce MAX_HEAP property

            """
            Heap.__max_heapify(seq, n, largest)

    @staticmethod
    def heapsort(seq):
        """
            This method performs a Heap Sort on the passed sequence
            by calling build_max_heap(seq) & __max_heapify(seq)
        """
        n = len(seq)

        Heap.build_max_heap(seq)

        """

        At this point, the largest item is stored at the root of the heap.
        Replace it with the last item of the heap followed by reducing the
        size of heap by 1. Finally, heapify the root of tree.
        Repeat above steps while size of heap is greater than 1.

        """

        for i in range(n-1, 0, -1):
            seq[i], seq[0] = seq[0], seq[i]
            Heap.__max_heapify(seq, i, 0)

    @staticmethod
    def extract_max(seq):
        """
            This method returns and removes the maximum element from present
            Heap
        """
        if len(seq) < 1:
            return
        max = seq[0]
        seq[0] = seq[(len(seq) - 1)]

        del seq[0]

        Heap.__max_heapify(seq, len(seq), 0)

        return max
