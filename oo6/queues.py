# The queue class is typically used as a sort of communication medium when
# one or more objects is producing data and one or more other objects is
# consuming the data in some way, probably at a different rate.

############### FIFO

from queue import Queue, Empty, Full

lineup = Queue(maxsize=3)

# The default behavior is to block or idly wait until the Queue object
# has data or room available to complete the operation.

# You can have it raise exceptions instead by passing block=False parameter
try:
    lineup.get(block=False)
except Empty as e:
    print(e)


lineup.put('one')
lineup.put('two')
lineup.put('three')
try:
    lineup.put('four', timeout= 1)
except Full as e:
    print(e)


lineup.full()
lineup.get()
lineup.full()
lineup.get()
lineup.get()
lineup.empty()

# Underneath the hood, python implements
# queues on top of the collections.deque
# ddata structure.
# deques are advanced data structures that
# permits efficient access to both end of
# the collection. It provides a more flexible
# interface than is exposed by Queue



###################### LIFO (stack)

# instead of using push and pop, Python again use put() and get().

from queue import LifoQueue

stack = LifoQueue(maxsize=3)
stack.put("one")
stack.put("two")
stack.put("three")
try:
    stack.put("four", block=False)
except Full as e:
    print(e)


stack.get()
stack.get()
stack.get()
stack.empty()

# normally people use append() and pop() on list instead of LIFO queue

################## priority queues

# the most important item is returned first
# the most important is the one that sorts lowest using the less than operator

# Usually put tuples in the priority queue, in which the first element palsy the
# role of weight. This is because of the implementation of __lt__ in tuples.

import heapq


h = []
heapq.heapify(h)
type(h)

heapq.heappush(h, (3, "three"))
heapq.heappush(h, (4, "four"))
heapq.heappush(h, (1, "one"))
heapq.heappush(h, (2, "two"))

while h:
    print(heapq.heappop(h))


class Heap(list):
    def __new__(*args):
        h = list.__new__(*args)
        heapq.heapify(h)
        return h

    def put(self, elm):
        return heapq.heappush(self, elm)

    def get(self):
        return heapq.heappop(self)

    def empty(self):
        return self


h = Heap()
h.put((3, "three"))
h.put((4, "four"))
h.put((1, "one"))
h.put((2, "two"))

while h.empty():
    print(h.get())







