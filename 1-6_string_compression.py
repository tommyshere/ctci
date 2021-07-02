# Input: aabcccccaaa
# Output: a2b1c5a3
# if compressed string is not smaller than original, return original
# mix of upper and lower case letters
class Solution(object):
    def string_compress(input):
        count = 0
        i = 0
        return_str = ""
        while i < len(input):
            if len(return_str) > len(input):
                return input
            if count == 0:
                return_str += input[i]
                count += 1
            elif return_str[-1] == input[i]:
                count += 1
            elif return_str[-1] != input[i]:
                # I kept skimming over the current character
                return_str += str(count) + input[i]
                count = 1
            i += 1
        if count > 0:
            return_str += str(count)
        return return_str

if __name__ == "__main__":
    print(Solution.string_compress("aaabcccccaaa"))
