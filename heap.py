import heapq
class Heap(list):
    def __init__(self, heap=None):
        if heap is None:
            heap = []
        heapq.heapify(heap)
        super().__init__(heap)

    def __repr__(self):
        return 'Heap({})'.format(super().__repr__())

    def heappush(self, item):
        return heapq.heappush(self, item)

    def heappop(self):
        return heapq.heappop(self)

    def pushpop(self, item):
        return heapq.heappushpop(self, item)

    def replace(self, item):
        return heapq.heapreplace(self, item)
    
    def merge(self, *iterables, key=None, reverse=False):
        return heapq.merge(self, *iterables, key, reverse)

    def nlargest(self, n, *args, **kwargs):
        return heapq.nlargest(n, self, *args, **kwargs)

    def nsmallest(self, n, *args, **kwargs):
        return heapq.nsmallest(n, self, *args, **kwargs)
