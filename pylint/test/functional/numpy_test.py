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
B.unexistant_method(4)  # [no-member]
C.unexistant_method(4)  # [no-member]
D.unexistant_method(4)  # [no-member]
E.unexistant_method(4)  # [no-member]

# bug 2747/2767. *_like functions call should be inferred as ndarray and thus
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

# bug 2694/2784. Calls to logical_or functions (and similar) should be inferred as ndarray
# and thus have itemset method
x = np.array([0, 1, 0, 1], dtype=np.bool)
y = np.array([0, 0, 1, 1], dtype=np.bool)
z = np.logical_or(x, y)
z.itemset(4, 0)
z.unexistant_method(3)  # [no-member]

# bug 2759. Calls to multiarray.dot function should be inferred as an ndarray
# and thus have itemset method
x = np.array([0, 1, 0, 1], dtype=np.bool)
y = np.array([0, 0, 1, 1], dtype=np.bool)
z = np.dot(x, y)
w = np.vdot(x, y)
z.itemset(4, 0)
w.itemset(4, 0)
z.unexistant_method(3)  # [no-member]
w.unexistant_method(3)  # [no-member]

# bug 2436. Calls to linspace function should be inferred as an ndarray
# end thus have itemset method
x = np.linspace(3, 5)
x.itemset(4, 0)
x.unexistant_method(3)  # [no-member]
