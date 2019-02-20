import numpy as np
a=np.array([1,52,521])
b=np.array([
    [1,2,3],
    [5,5,4],
    [2,4,6]
])
c=np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[0,9,8],[7,6,5],[4,3,2]],
    [[3,4,4],[3,4,4],[3,3,3]]
])
print(a)
print(b)
print (c)

d=np.arange(10,20)
print (d)


e=np.arange(10,20,2)
print(e)

f=np.zeros((4,4))
print(f)


g=np.zeros((4,4), dtype=np.int)
print(g)


h=np.ones((4,4), dtype=np.int)
print(h)