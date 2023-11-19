def maxVowels(s, k):
    def is_vowel(char):
        return char.lower() in 'aeiou'

    count = 0
    max_count = 0

    # Count vowels in the first window of length k
    for i in range(k):
        if is_vowel(s[i]):
            count += 1
    max_count = count
    # Iterate through the rest of the string
    for i in range(k, len(s)):
        if is_vowel(s[i]):
            count += 1
        if is_vowel(s[i - k]):
            count -= 1

        # Update max_count outside of the loop
        max_count = max(count, max_count)

    return max_count

print(maxVowels("abciiidef",3))
