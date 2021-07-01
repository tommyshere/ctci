# Replace all spaces in a string with "%20"
# and given "true" length of the string

class Solution(object):
    def urlify():
        input_val = "Mr John Smith   "
        true_length = 13
        result_str = ""
        i = 0
        for i in range(13):
            if input_val[i] == " ":
                result_str += "%20"
            else:
                result_str += input_val[i]
        return result_str

if __name__ == "__main__":
    print(Solution.urlify())
