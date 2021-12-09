import numpy as np
a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
  
print("a.shape: ", a.shape)
print("mean a = ", np.mean(a))
#[Running] python -u "d:\NguyenHuuVuCNTT1405\CoBan\CodePython\BtLqNumpy\Vd3.py"
#a.shape:  (2, 262144)
#mean a =  0.54999924
#[Done] exited with code=0 in 1.061 seconds