import numpy as np
x = np.array([2, np.nan, 5, 9])
print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))

#[Running] python -u "d:\NguyenHuuVuCNTT1405\CoBan\CodePython\BtLqNumpy\Vd9.py"
#mean =  5.333333333333333
#median =  5.0

#[Done] exited with code=0 in 0.685 seconds