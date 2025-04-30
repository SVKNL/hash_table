class MyDict:
    def __init__(self, capacity = 4, load_factor = 0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

    def _get_index(self, key):
        return hash(key) % self.capacity

    def rehash(self):
        buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in buckets:
            for key, value in bucket:
                self.__setitem__(key, value)

    def __setitem__(self, key, value):
        index = self._get_index(key)
        bucket = self.buckets[index]
        flag = True
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                flag = False
        if flag:
            bucket.append((key, value))
            self.size += 1

        if self.load_factor < self.size / self.capacity:
            self.rehash()

    def __getitem__(self, key):
        index = self._get_index(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError

    def __delitem__(self, key):
        index = self._get_index(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError

    def __contains__(self, key):
        index = self._get_index(key)
        bucket = self.buckets[index]
        for (k, _) in bucket:
            if k == key:
                return True
        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        for bucket in self.buckets:
            for key, _ in bucket:
                yield key

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def keys(self):
        return self.__iter__()

    def values(self):
        for bucket in self.buckets:
            for _, value in bucket:
                yield value

    def items(self):
        for bucket in self.buckets:
            for key, value in bucket:
                yield (key, value)
