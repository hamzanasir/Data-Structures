class Hashtable:
    class Node:
        """Instances of this class will be used to construct the linked lists (chains)
        found in non-empty hashtable buckets."""

        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self, n_buckets=1000):
        self.buckets = [None] * n_buckets  # initially empty buckets array
        self.count = 0

    def __getitem__(self, key):
        bucketidx = hash(key) % len(self.buckets)
        node = self.buckets[bucketidx]
        if node == None:
            raise KeyError
        if node.key == key:
            return node.val
        else:
            head = node.next
            while head:
                if head.key == key:
                    return head.val
                head = head.next
        raise KeyError

    def __setitem__(self, key, val):
        bucketidx = hash(key) % len(self.buckets)
        node = Hashtable.Node(key, val)

        if self.buckets[bucketidx] == None:
            self.buckets[bucketidx] = node
            self.count += 1
        else:
            head = self.buckets[bucketidx]
            if head.key == key:
                head.val = val
                return
            while head.next != None:
                head = head.next
                if head.key == key:
                    head.val = val
                    return
            head.next = node
            self.count += 1

    def __delitem__(self, key):
        bucketidx = hash(key) % len(self.buckets)
        node = self.buckets[bucketidx]
        if node == None:
            raise KeyError
        if node.key == key:
            self.buckets[bucketidx] = node.next
            self.count -= 1
            return
        if node != None:
            previousnode = node
            nextnode = node.next
            while nextnode:
                if nextnode.key == key:
                    previousnode.next = nextnode.next
                    self.count -= 1
                    return
                previousnode = nextnode
                nextnode = nextnode.next
        raise KeyError

    def __contains__(self, key):
        bucketidx = hash(key) % len(self.buckets)
        node = self.buckets[bucketidx]
        if node == None:
            return False
        if node.key == key:
            return True
        else:
            head = node.next
            while head:
                if head.key == key:
                    return True
                head = head.next
        return False

    def __len__(self):
        return self.count

    def __iter__(self):
        for x in range(len(self.buckets)):
            node = self.buckets[x]
            while node:
                yield node.key
                node = node.next

    def keys(self):
        return iter(self)

    def values(self):
        for x in range(len(self.buckets)):
            node = self.buckets[x]
            while node:
                yield node.val
                node = node.next

    def items(self):
        for x in range(len(self.buckets)):
            node = self.buckets[x]
            while node:
                yield (node.key, node.val)
                node = node.next

    def setdefault(self, key, default=None):
        try:
            val = self[key]
            return val
        except KeyError:
            self[key] = default
            return default