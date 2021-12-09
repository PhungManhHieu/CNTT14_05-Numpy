import numpy as np
x = np.array([[14, 96],
               [46, 82],
               [80, 67],
               [77, 91],
               [99, 87]])
print("x = ", x)
 
print("Range = ", np.ptp(x))
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))

#[Running] python -u "d:\NguyenHuuVuCNTT1405\CoBan\CodePython\BtLqNumpy\Vd15.py"
#x =  [[14 96]
#      [46 82]
#      [80 67]
#      [77 91]
#      [99 87]]
#Range =  85
#Range (axis = 0) =  [85 29]
#Range (axis = 1) =  [82 36 13 14 12]

#[Done] exited with code=0 in 0.817 seconds