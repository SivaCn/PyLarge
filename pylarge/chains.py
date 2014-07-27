#! /usr/bin/python

"""Linked list Representation and implementation.
"""

# -*- coding: utf-8 -*-

## ------ Imports ------ ##
## ------ Imports ------ ##


__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Node:
    """Referential Structure used to create new nodes"""
    def __init__(self, **kwargs):
        """Constructor."""
        self.data = kwargs.get('filaname', '')
        self.next = None
        self.col_name = None
        self.hashcode = None
        self.start = None
        self.end = None


class Meta:
    """A meta class contains info about the tree at any moment."""
    def __init__(self, **kwargs):
        """Constructor."""
        self.chain = None
        self.size = 0
        self.next_chain = None

        self._id_start, self._id_end = kwargs.get('_id_range', (-1, -1))

    def __repr__(self):
        """."""
        return "SubList({0}, {1})".format(self._id_start, self._id_end)


class LinkedList:
    def __init__(self, **kwargs):
        """Constructor."""
        self._list = Meta(**kwargs)
        self._list.chain = None

    def insert(self, data):
        """Insert a new node with in the tree."""
        _temp = Node(data)

        if not self._list.chain:
            self._list.chain = _temp
            return

        walker = self._list.chain

        while walker.next:
            walker = walker.next

        self._list.size += 1
        walker.next = _temp

    def show(self):
        walker = self._list.chain

        while walker:
            print walker.data
            walker = walker.next
