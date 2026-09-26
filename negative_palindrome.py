class Solution(object):
    def reverse(self, x):
        original_no = x
        reverse_no = 0

        if x < 0:
            x = x * -1

        while (x > 0):
            last_digit = x % 10
            x = x // 10
            reverse_no = (reverse_no * 10) + last_digit

        if original_no < 0:
            reverse_no = reverse_no * -1

        return reverse_no