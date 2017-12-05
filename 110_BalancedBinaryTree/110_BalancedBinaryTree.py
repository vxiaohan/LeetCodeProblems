import unittest
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(value_list):
    node_list = [(None if value_list[i] is None else TreeNode(value_list[i])) for i in range(len(value_list))]
    max_depth = int(math.log((len(value_list) + 1) / 2, 2)) + 1
    start_index = 0
    for i in range(max_depth - 1):
        end_index = start_index + pow(2, i)
        for j in range(start_index, end_index):
            left_node_index = pow(2, i + 1) - 1 + 2 * (j - start_index)
            right_node_index = left_node_index + 1
            if not node_list[j] is None:
                node_list[j].left = node_list[left_node_index]
                node_list[j].right = node_list[right_node_index]
        start_index += pow(2, i)
    return node_list


class Solution:
    depth = {}

    def get_depth(self, node):
        if node is None:
            return 0
        if id(node) in self.depth:
            return self.depth[id(node)]
        else:
            self.depth[id(node)] = max(self.get_depth(node.left), self.get_depth(node.right)) + 1
            return self.depth[id(node)]

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.depth.clear()
        stack = [root]
        searched = {}
        searched[id(root)] = 1
        while len(stack) > 0:
            if abs(self.get_depth(stack[-1].left) - self.get_depth(stack[-1].right)) > 1:
                return False
            if not stack[-1].left is None and id(stack[-1].left) not in searched:
                stack.append(stack[-1].left)
                searched[id(stack[-1])] = 1
                continue
            if not stack[-1].right is None and id(stack[-1].right) not in searched:
                stack.append(stack[-1].right)
                searched[id(stack[-1])] = 1
                continue
            stack.pop()
        return True


class TestMinDepth(unittest.TestCase):
    def testMinDepth(self):
        test = Solution()
        self.assertEqual(
            test.isBalanced(buildTree([1, 2, 3, 4, None, 5, 6, None, None, None, None, 7, None, None, None])[0]), True)
        self.assertEqual(test.isBalanced(buildTree([1, None, 2, None, None, None, 3])[0]), False)
        self.assertEqual(test.isBalanced(buildTree(
            [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5, None, None, None, None, None, None, None, None,
             None, None, None, None])[0]), True)

    if __name__ == '__main__':
        unittest.main()
