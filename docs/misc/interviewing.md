# Interviewing

## Coding

```python
from bisect import bisect, insort
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from typing import List


# sets
s1 = set()
s2 = set()
s1.add(1)
s2.update(s1)
s2.remove(1)

# sorting
l = [(1, 2), (2, 3), (3, 4)]
sorted(l, key=lambda el: el[0])  # returns a sorted copy [(1, 2), (2, 3), (3, 4)]
l.sort(reverse=True)  # in-place [(3, 4), (2, 3), (1, 2)]

# heaps (python heapq is min-heap; tree; each element smaller than children)
heap = []
heappush(heap, 1) # min heap; O(log n) (holds k-largest elements)
heappop(heap)

# deque
queue = deque([])
queue.append(1)
queue.popleft()

# bisect
l = [2, 4, 5, 6, 8]
bisect(l, 3)  # 1; O(log n)
bisect(l, 5)  # 3; equivalent to bisect_right
insort(l, 1)  # O(n) due to shifting array elements; l == [1, 2, 4, 5, 6, 8]

# defaultdict
d = defaultdict(list)
d["foo"].append(44)
d["foo"].append(42)

# counter
c = Counter([1, 1, 1, 2, 2, 3])
c = Counter("aaabbc")
c.update("a")  # adds 1
c.subtract("b")  # subtracts 1

# BST
# all children of n on left smaller than n; all children of n on right larger than n
```

## System Design

* narrow scope, clarifying questions
    * what are the business and product priorities?  E.g., engagement or revenue
* requirements / metrics
    * batch or real time?
    * all users or a subset?
    * scale (number of users/items/etc, requests/second)
* high-level design
    * propose several w/ pros and cons
    * pick one (and justify)
* data brainstorming
    * data sources
    * high-level features (e.g., context, user, item, interactions)
    * feature representation (numerical, categorical, text, other)
        * share specific knowledge of preparing/cleaning each type
    * feature importance / selection
* model
    * type: classification (multi), regression, other
    * specific model (discuss alternatives + pros/cons)
    * offline training + evaluation
* online evaluation
* model lifecycle management (monitoring performance, feature drift)

## Tmp

```txt
abcdefghijklmnopqrstuvwxyz
0        1         2
12345678901234567890123456
```
