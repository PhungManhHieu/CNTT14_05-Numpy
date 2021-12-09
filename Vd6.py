import numpy as np
arr = np.array([[7, 4, 2], [3, 9, 5]])
print("median arr (axis = 0) = ", np.median(arr, axis=0))
print("median arr (axis = 1) = ", np.median(arr, axis=1))

#[Running] python -u "d:\NguyenHuuVuCNTT1405\CoBan\CodePython\BtLqNumpy\Vd6.py"
#median arr (axis = 0) =  [5.  6.5 3.5]
#median arr (axis = 1) =  [4. 5.]

#[Done] exited with code=0 in 0.708 seconds