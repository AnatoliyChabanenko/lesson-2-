"""Generate 2 lists with the length of 10 with random integers from 1 to 10,
 and make a third list containing the common integers between the 2 initial lists without
  any duplicates.

Constraints: use only while loop and random module to generate numbers
"""

import random
x = random.sample(range(10), 10)
y = random.sample(range(10), 10)
z = set(x).union(set(y))
print(y)


