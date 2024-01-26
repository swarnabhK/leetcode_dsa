# Given a character array s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
# Your code must solve the problem in-place, i.e. without allocating extra space.

class Solution:
    def reverse_string(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverse_words(self, s):
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] != " ":
                r += 1
            self.reverse_string(s, l, r - 1)
            r += 1
            l = r

    def reverseWords(self, s) -> None:
        # Reverse the whole string
        self.reverse_string(s, 0, len(s) - 1)
        # Reverse each word
        self.reverse_words(s)

# Test case
solution_obj = Solution()
test_input = ["t", "h", "i", "s", " ", "i", "s", " ", "a", " ", "t", "e", "s", "t"]
solution_obj.reverseWords(test_input)

# Display the result
print(test_input)
