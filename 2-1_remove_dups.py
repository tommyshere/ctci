# remove duplicates in a linked list

def remove_dups(node):
    curr = node
    duplicate_check = []
    while curr is not None:
        if curr.value is not in duplicate_check:
            duplicate_check.append(curr.value)
            curr = curr.next
        else:
            curr.next = curr.next.next
