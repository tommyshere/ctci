# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
def is_unique_1():
    value = "abcdefgh"
    value_len = len(value)
    for i in range(value_len):
        if value[i] in value[i+1:]:
            return False
    return True

def is_unique_2():
    value = "abcdefgh"
    counter = {}
    for s in value:
        if s in counter:
            counter[s] = counter[s] + 1
        else:
            counter[s] = 1

    for value in counter.values():
        if value > 1:
            return False
    return True

if __name__ == "__main__":
    print(is_unique_1())
    print(is_unique_2())
