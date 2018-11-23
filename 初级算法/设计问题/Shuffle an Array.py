import numpy as np


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle = [i for i in range(len(self.origin))]
        shuffle_ = []
        np.random.shuffle(shuffle)
        for item in shuffle:
            shuffle_.append(self.origin[item])
        return shuffle_