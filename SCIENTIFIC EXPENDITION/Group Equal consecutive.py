def group_equal(els):
    # your code here
    final_li = []
    if len(els) == 0:
        return final_li
    else:
        li = [els.pop(0)]
        while True:
            if len(els) != 0 and els[0] == li[-1]:
                li.append(els.pop(0))
            else:
                final_li.append(li)
                break
        return final_li + group_equal(els)


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
