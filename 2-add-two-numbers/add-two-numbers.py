class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(0)
        current = ans
        carry = 0

        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            summ = d1 + d2 + carry
            carry = summ // 10
            digit = summ % 10

            current.val = digit

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2 or carry:
                current.next = ListNode(0)
                current = current.next

        return ans