import unittest
from collections import deque


class Solution:
    @staticmethod
    def get_sum(node1, node2):
        if node1 is None and node2 is None:
            return 0
        elif node1 is None:
            return node2.val
        elif node2 is None:
            return node1.val
        else:
            return node1.val + node2.val

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestMergeTrees(unittest.TestCase):
    @staticmethod
    def convertTreeToList(root):
        if root is None:
            return []
        level = 1
        result = []
        nodes = []

    @staticmethod
    def create_tree_from_list(values):
        if len(values) == 0:
            return None
        nodes = []
        for i in range(len(values)):
            nodes.append(TreeNode(val=values[i]))
        level = 0
        last_level_index = -1
        while last_level_index + 1 < len(nodes):
            for k in range(last_level_index + 1, min(last_level_index + 2 ** level + 1, len(nodes))):
                left_index = last_level_index + 2 ** level + (k - 1 - last_level_index) * 2 + 1
                right_index = left_index + 1
                nodes[k].left = nodes[left_index] if (
                            left_index < len(nodes) and nodes[left_index].val is not None) else None
                nodes[k].right = nodes[right_index] if (
                            right_index < len(nodes) and nodes[right_index].val is not None) else None
            last_level_index = last_level_index + 2 ** level
            level += 1
        return nodes[0]

    def testConvertTreeToList(self):
        self.assertListEqual(self.convertTreeToList(self.create_tree_from_list([1, 3, 2, 5])), [1, 3, 2, 5])
        self.assertListEqual(self.convertTreeToList(self.create_tree_from_list([2, 1, 3, None, 4, None, 7])),
                             [2, 1, 3, None, 4, None, 7])
    '''
    def testMergeTrees(self):
        test = Solution()
        self.assertListEqual(test.mergeTrees(self.create_tree_from_list([1, 3, 2, 5]),
                                             self.create_tree_from_list([2, 1, 3, None, 4, None, 7])),
                             [3, 4, 5, 5, 4, None, 7])
    '''

if __name__ == "__main__":
    unittest.main()
