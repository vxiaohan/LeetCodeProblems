# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer1 = l1
        pointer2 = l2
        result = ListNode(0)
        resultPointer = result
        addFlage = False
        while(True):
            if pointer1 == None:
                resultPointer.val = pointer2.val
            elif pointer2 == None:
                resultPointer.val = pointer1.val
            else:
                resultPointer.val = pointer1.val + pointer2.val
            if addFlage:
                resultPointer.val += 1
            if resultPointer.val >= 10:
                addFlage = True
                resultPointer.val -= 10
            else:
                addFlage = False
            if (pointer1 == None or pointer1.next == None) and (pointer2 == None or pointer2.next == None):
                if addFlage:
                    resultPointer.next = ListNode(1)
                    break
                else:
                    break
            if pointer1 != None:
                pointer1 = pointer1.next
            if pointer2 != None:
                pointer2 = pointer2.next
            resultPointer.next = ListNode(0)
            resultPointer = resultPointer.next
        return result