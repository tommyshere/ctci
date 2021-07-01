# Given two strings,
# write a method to decide if one is a permutation of the other.
class Solution(object):
    def check_permutation():
        s1 = "ab", s2 = "eidbaooo"

        # the sliding window
        # check a splice of the longer text
        # can assume s2 will always be longer than s1

        shorter = len(s1)
        longer = len(s2)
        short_counter = Counter(s1)

        for i in range(longer - shorter + 1):
            window = s2[i:i+shorter]
            # check if the count of letters in window
            # match up to count of letters in s1
            longer_counter = Counter(window)
            if short_counter == longer_counter:
                return True

        return False
