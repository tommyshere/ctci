# # different edits:
# insert a char
# remove a char
# replace a char
# check if two strings are only one edit away
from collections import Counter
class Solution(object):
    def one_away(str1, str2):
        # if difference len(str1) and len(str2) is greater than 1 then auto False
        if abs(len(str1) - len(str2)) > 1:
            return False
        # insertion and deletion should be the same
        # if it's one length is shorter than the other
        # first thing we do is check if one letter away
        if len(str1) < len(str2) or len(str2) < len(str1):
            if len(str2) > len(str1):
                longer = str2
                shorter = str1
            else:
                longer = str1
                shorter = str2

            l_i = 0
            s_i = 0
            while l_i < len(longer) and s_i < len(shorter):
                if longer[l_i] == shorter[s_i]:
                    s_i += 1
                l_i += 1

            # if the length s_i has been exhausted
            # the while loop has gone through the entire string to check each value
            # otherwise it would not have done so
            if s_i == len(shorter):
                return True
            return False


        # if they're the same length
        # just have to see if the
        if len(str1) == len(str2):
            check = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    check += 1

                if check > 2:
                    return False
            return True


if __name__ == "__main__":
    print(Solution.one_away("pale", "ple"))  # True
    print(Solution.one_away("pale", "bake"))  # False
    print(Solution.one_away("pale", "pales"))  # True
    print(Solution.one_away("pale", "palesss"))  # True
    print(Solution.one_away("pale", "pile")) # True
