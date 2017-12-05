import unittest
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, value_list):
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

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        stack = [root]
        searched = {}
        searched[id(root)] = 1
        current_depth = 1
        min_depth = float('inf')
        while len(stack) > 0:
            if stack[-1].left is None and stack[-1].right is None:
                if current_depth < min_depth:
                    min_depth = current_depth
                    continue
            if not stack[-1].left is None and id(stack[-1].left) not in searched:
                stack.append(stack[-1].left)
                current_depth += 1
                searched[id(stack[-1])] = 1
                continue
            if not stack[-1].right is None and id(stack[-1].right) not in searched:
                stack.append(stack[-1].right)
                current_depth += 1
                searched[id(stack[-1])] = 1
                continue
            stack.pop()
            current_depth -= 1
        return min_depth

class TestMinDepth(unittest.TestCase):
    def testMinDepth(self):
        test = Solution()
        self.assertEqual(
            test.minDepth(test.buildTree([1, 2, 3, 4, None, 5, 6, None, None, None, None, 7, None, None, None])[0]), 3)


if __name__ == '__main__':
    unittest.main()
