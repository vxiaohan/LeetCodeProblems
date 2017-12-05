import unittest
import math


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, value_list):
        # root = TreeNode(value_list[0])
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

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        max_depth = 1
        max_depth_value = root.val
        current_depth = 1
        searched = {}
        searched[id(root)] = 1
        while len(stack) != 0:
            if (not stack[-1].left is None) and id(stack[-1].left) not in searched:
                stack.append(stack[-1].left)
                searched[id(stack[-1])] = 1
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
                    max_depth_value = stack[-1].val
            elif (not stack[-1].right is None) and id(stack[-1].right) not in searched:
                stack.append(stack[-1].right)
                searched[id(stack[-1])] = 1
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
                    max_depth_value = stack[-1].val
            else:
                stack.pop()
                current_depth -= 1
        return max_depth_value


class TestBinaryTree(unittest.TestCase):
    def testBuildTree(self):
        test = Solution()
        test.buildTree([1, 2, 3, 4, None, 5, 6, None, None, None, None, 7, None, None, None])

    def testFindBottomValue(self):
        test = Solution()
        node_list = test.buildTree([1, 2, 3, 4, None, 5, 6, None, None, None, None, 7, None, None, None])
        self.assertEqual(test.findBottomLeftValue(node_list[0]), 7)


if __name__ == '__main__':
    unittest.main()
