class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    def enqueue(self, val):

        if self.head - self.tail == 1:
            raise RuntimeError

        if len(self.data) - 1 == self.tail and self.head == 0:
            raise RuntimeError

        if self.head == -1 and self.tail == -1:
            self.data[0] = val
            self.head = 0
            self.tail = 0
        else:
            if len(self.data) - 1 == self.tail and self.head != 0:
                self.tail = -1
            self.data[self.tail + 1] = val
            self.tail = self.tail + 1

    def dequeue(self):

        if self.head == self.tail:
            temp = self.head
            self.head = -1
            self.tail = -1
            return self.data[temp]

        if self.head == -1 and self.tail == -1:
            raise RuntimeError
        if self.head != len(self.data):
            ret = self.data[self.head]
            self.data[self.head] = None
            self.head = self.head + 1
        else:
            # resetting head
            self.head = 0
            ret = self.data[self.head]
            self.data[self.head] = None
            self.head = self.head + 1
        return ret

    def resize(self, newsize):
        assert (len(self.data) < newsize)
        newdata = [None] * newsize
        head = self.head
        current = self.data[head]
        count = 0
        while current != None:
            newdata[count] = current
            count += 1
            if count != 0 and head == self.tail:
                break
            if head != len(self.data) - 1:
                head = head + 1
                current = self.data[head]
            else:
                head = 0
                current = self.data[head]
        self.data = newdata
        self.head = 0
        self.tail = count - 1

    def empty(self):
        if self.head == -1 and self.tail == -1:
            return True
        return False

    def __bool__(self):
        return not self.empty()

    def __str__(self):
        if not (self):
            return ''
        return ', '.join(str(x) for x in self)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        head = self.head
        current = self.data[head]
        count = 0
        while current != None:
            yield current
            count += 1
            if count != 0 and head == self.tail:
                break
            if head != len(self.data) - 1:
                head = head + 1
                current = self.data[head]
            else:
                head = 0
                current = self.data[head]