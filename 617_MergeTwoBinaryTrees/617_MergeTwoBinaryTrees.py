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
        root_node = TreeNode(self.get_sum(t1, t2))
        result_stack = deque()
        result_stack.append(root_node)
        result_node_temp = root_node
        tree_1_stack = deque()
        tree_1_stack.append(t1)
        tree_1_node_temp = t1.left
        tree_2_stack = deque()
        tree_2_stack.append(t2)
        tree_2_node_temp = t2.left
        while len(result_stack) > 0 or result_node_temp is not None:
            while tree_1_node_temp is not None or tree_2_node_temp is not None:
                result_node_temp = TreeNode(self.get_sum(tree_1_node_temp, tree_2_node_temp))
                result_stack.append(result_node_temp)
                tree_1_stack.append(tree_1_node_temp)
                tree_2_stack.append(tree_2_node_temp)
                if not (tree_1_node_temp is None):
                    tree_1_node_temp = tree_1_node_temp.left
                if not (tree_2_node_temp is None):
                    tree_2_node_temp = tree_2_node_temp.left
            result_node_temp = result_stack.pop()
            tree_1_node_temp = tree_1_stack.pop()
            tree_2_node_temp = tree_2_stack.pop()
            if tree_1_node_temp is None and tree_2_node_temp is None:
                result_node_temp = None
                continue
            elif tree_1_node_temp is None and tree_2_node_temp is not None:
                if tree_2_node_temp.right is None:
                    tree_2_node_temp = None
                    result_node_temp = None
                else:
                    result_node_temp.right = TreeNode(tree_2_node_temp.right.val)
                    result_node_temp = result_node_temp.right
                    tree_2_node_temp = tree_2_node_temp.right
            elif tree_2_node_temp is None and tree_1_node_temp is not None:
                if tree_1_node_temp.right is None:
                    tree_1_node_temp = None
                    result_node_temp = None
                else:
                    result_node_temp.right = TreeNode(tree_1_node_temp.right.val)
                    result_node_temp = result_node_temp.right
                    tree_1_node_temp = tree_1_node_temp.right
            else:
                if tree_1_node_temp.right is None and tree_2_node_temp.right is None:
                    result_node_temp = None
                else:
                    result_node_temp.right = TreeNode(tree_1_node_temp.right, tree_2_node_temp.right)
                    result_node_temp = result_node_temp.right
                tree_1_node_temp = tree_1_node_temp.right
                tree_2_node_temp = tree_2_node_temp.right
        return root_node


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
                nodes[k].left = nodes[left_index] if left_index < len(nodes) else None
                nodes[k].right = nodes[right_index] if right_index < len(nodes) else None
            last_level_index = last_level_index + 2 ** level
            level += 1
        return nodes[0]

    def testMergeTrees(self):
        test = Solution()
        self.assertListEqual(test.mergeTrees(self.create_tree_from_list([1, 3, 2, 5]),
                                             self.create_tree_from_list([2, 1, 3, None, 4, None, 7])),
                             [3, 4, 5, 5, 4, None, 7])


if __name__ == "__main__":
    unittest.main()
