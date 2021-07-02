# Given a string, check if it is a permutation of a palindrome
# Input: "Tact Coa"
# Output: True (permutations: 'taco cat', 'atco cta', etc.)

# can the words be rearrange to create a palindrome?
# what is a palindrome?
# same letters front and back
# same count of letters
# aa aba aaa abba abcba abccba
# 2  2,1  3  2,2  2,2,1  2,2,2
# abca
# 2,1,1
# you con only have >2 odd number in the dictionary
class Solution(object):
    def pal_perm():
        input = "Tact Coa"
        count = {}
        for x in input.lower():
            if x != " " and x in count:
                count[x] = count[x] + 1
            elif x != " " and x not in count:
                count[x] = 1

        odd_count = 0
        for val in count.values():
            if val % 2 != 0:
                odd_count += 1

        if odd_count < 2:
            return True
        return False



if __name__ == "__main__":
    print(Solution.pal_perm())
