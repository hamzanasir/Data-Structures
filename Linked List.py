class LinkedList:
    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next = next

    def __init__(self):
        self.head = LinkedList.Node(None)  # sentinel node (never to be removed)
        self.head.prior = self.head.next = self.head  # set up "circular" topology
        self.length = 0

    ### prepend and append, below

    def prepend(self, value):
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next.prior = self.head.next = n
        self.length += 1

    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n
        self.length += 1

    ### subscript-based access ###

    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self)
            if nidx < 0:
                nidx = 0
        return nidx

    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= self.length:
            raise IndexError
        current = self.head.next
        for i in range(self.length):
            if i == nidx:
                return current.val
            current = current.next

    def _getnode_(self, idx):
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= self.length:
            raise IndexError
        current = self.head.next
        for i in range(self.length):
            if i == nidx:
                return current
            current = current.next

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= self.length:
            raise IndexError
        current = self.head.next
        for i in range(self.length):
            if i == nidx:
                current.val = value
            current = current.next

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert (isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= self.length:
            raise IndexError
        current = self.head.next
        for i in range(self.length):
            if i == nidx:
                current.prior.next = current.next
                current.next.prior = current.prior
                self.length -= 1
            current = current.next

    ### stringification ###

    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        if self.length == 0:
            return '[]'
        else:
            string = '['
            string += ', '.join(str(x) for x in self)
            string += ']'
            return string

    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        if self.length == 0:
            return '[]'
        else:
            string = '['
            string += ', '.join(str(x) for x in self)
            string += ']'
            return string

    ### single-element manipulation ###

    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        nidx = self._normalize_idx(idx)
        if nidx > self.length:
            raise IndexError
        if nidx == self.length:
            self.append(value)
        else:
            currentnode = self.head.next
            for x in range(nidx):
                currentnode = currentnode.next
            newnode = LinkedList.Node(value, currentnode.prior, currentnode)
            currentnode.prior.next = newnode
            currentnode.prior = newnode
            self.length += 1

    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        nidx = self._normalize_idx(idx)
        temp = self[nidx]
        del self[nidx]
        return temp

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        flag = False

        currentnode = self.head.next
        for x in range(self.length):
            if currentnode.val == value:
                indextorem = x
                flag = True
                break
            currentnode = currentnode.next
        if flag == True:
            del self[indextorem]
        else:
            raise ValueError

    ### predicates (T/F queries) ###

    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in order) as
        other. If other is not an LinkedList, returns False."""

        if self.length != other.length:
            return False

        for i in range(self.length):
            if self[i] != other[i]:
                return False
        return True


    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""

        currentnode = self.head.next
        for x in range(self.length):
            if currentnode.val == value:
                return True
            currentnode = currentnode.next
        return False


    ### queries ###

    def __len__(self):
        """Implements `len(self)`"""
        return self.length

    def min(self):
        """Returns the minimum value in this list."""

        minimum = self[0]

        for x in self:
            if x < minimum:
                minimum = x
        return minimum


    def max(self):
        """Returns the maximum value in this list."""
        maximum = self[0]
        for x in self:
            if x > maximum:
                maximum = x
        return maximum

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""

        if j != None:
            ni = self._normalize_idx(i)
            nj = self._normalize_idx(j)
            for x in range(ni, nj):
                if self[x] == value:
                    return x
            raise ValueError
        else:
            ni = self._normalize_idx(i)
            for x in range(ni, self.length):
                if self[x] == value:
                    return x
            raise ValueError

    def count(self, value):
        """Returns the number of times value appears in this list."""
        count = 0
        currentnode = self.head.next
        for x in range(self.length):
            if currentnode.val == value:
                count += 1
            currentnode = currentnode.next
        return count


    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those
        of other."""
        assert (isinstance(other, LinkedList))

        newlist = LinkedList()
        if len(self) > 0:
            for x in self:
                newlist.append(x)
        if len(other) > 0:
            for x in other:
                newlist.append(x)
        return newlist


    def clear(self):
        """Removes all elements from this list."""
        self.head.prior = self.head.next = self.head
        self.length = 0
        return self

    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        newlist = LinkedList()
        for x in self:
            newlist.append(x)
        return newlist

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        for x in other:
            self.append(x)
        return self

    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        current = self.head.next
        while current and current.val != None:
            yield current.val
            current = current.next