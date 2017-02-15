class Heap:
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key = key

    @staticmethod
    def _parent(idx):
        return (idx - 1) // 2

    @staticmethod
    def _left(idx):
        return idx * 2 + 1

    @staticmethod
    def _right(idx):
        return idx * 2 + 2

    def _heapify(self, idx=0):
        curr = idx
        left = Heap._left(curr)
        right = Heap._right(curr)
        while True:
            left = Heap._left(curr)
            right = Heap._right(curr)
            max_idx = curr
            if left < len(self.data) and self.key(self.data[left]) > self.key(self.data[curr]):
                max_idx = left
            if right < len(self.data) and self.key(self.data[right]) > self.key(self.data[max_idx]):
                max_idx = right

            if max_idx != curr:
                self.data[curr], self.data[max_idx] = self.data[max_idx], self.data[curr]
                curr = max_idx
            else:
                break

    def add(self, x):
        self.data.append(x)
        idx = len(self.data) - 1
        pidx = Heap._parent(idx)
        while self.key(self.data[pidx]) < self.key(self.data[idx]) and idx != 0:
            self.data[pidx], self.data[idx] = self.data[idx], self.data[pidx]
            idx = pidx
            pidx = Heap._parent(idx)

    def max(self):
        return self.data[0]

    def pop_max(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        self._heapify()
        return ret

    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)