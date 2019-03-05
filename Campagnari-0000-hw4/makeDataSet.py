#!/usr/bin/env python3
#
# Save an exponential dataset to a file
#
# CC 7 Feb 2019
#--------------------------------------
import numpy as np

# Initialize random number
np.random.seed(12345)

# could have used np.random.exponential instead
x = -2.3 * np.log(np.random.random_sample(50000))

# write it out
np.save("dataSet.npy", x)
