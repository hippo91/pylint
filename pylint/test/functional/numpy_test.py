"""Test of numpy linting"""
#pylint: disable=invalid-name
import numpy as np

# bug 2721. *_like functions call should be inferred as ndarray and thus
# have itemset method
A = np.random.randint(9, size=(3, 3))
B = np.zeros_like(A)
C = np.full_like(A, 3)
D = np.empty_like(A)
E = np.ones_like(A)
A.itemset(4, 0)
B.itemset(4, 0)
C.itemset(4, 0)
D.itemset(4, 0)
E.itemset(4, 0)
A.unexistant_method(4)  # [no-member]

# bug 2747. *_like functions call should be inferred as ndarray and thus
# have __getitem__ and __setitem__
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.zeros_like(a)
c = np.full_like(a, 3)
d = np.empty_like(a)
e = np.ones_like(a)

index = (0, 1)
a[index] = 9
b[index] = 9
c[index] = 9
d[index] = 9
e[index] = 9
x = b[index]
y = c[index]
z = d[index]
w = e[index]
