from itertools import combinations
import numpy as np

tar = 15
nums = np.array([2, 3, 12, 11])

combs = [i for i in combinations(nums, 2)]

sums = np.sum(combs, axis=1)

good_comb = np.where(sums == tar)[0][0]

indices_sum_to_tar = [np.where(nums == i)[0][0] for i in combs[good_comb]]
print(indices_sum_to_tar)
