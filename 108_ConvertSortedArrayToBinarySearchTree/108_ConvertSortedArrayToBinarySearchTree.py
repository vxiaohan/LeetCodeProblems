import unittest


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def creatTreeNode(self, numbers):
        if len(numbers) < 1:
            return None
        if len(numbers) == 1:
            return TreeNode(numbers[0])
        middle_index = int(len(numbers)/2)
        root = TreeNode(numbers[middle_index])
        root.left = self.creatTreeNode(numbers[0:middle_index])
        root.right = self.creatTreeNode(numbers[middle_index+1:])
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        root = self.creatTreeNode(nums)
        return root

class TestArrayToBST(unittest.TestCase):
    def testSortedArrayToBST(self):
        test = Solution()
        haha = test.sortedArrayToBST([-10,-3,0,5,9])
        test.sortedArrayToBST([])

if __name__ == '__main__':
    unittest.main()
