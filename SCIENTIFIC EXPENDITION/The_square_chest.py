def check_square(startingPoint, width):
    square_list = []
    for i in range(width):
        square_list.append([startingPoint+i, startingPoint+i + 1])
        square_list.append([startingPoint+i+4*width, startingPoint+i+4*width + 1])
        square_list.append([startingPoint+i*4, startingPoint+i*4 + 4])
        square_list.append([startingPoint+1*width+i*4, startingPoint+1*width+i*4 + 4])
    return square_list

def checkio(lines_list):
    """Return the quantity of squares"""

    # change sequence
    lines_list = [sorted(x) for x in lines_list]

    count_square = 0
    for each in lines_list:
        x, y = each

        # reduce the repeat. e.g. [1,2] [1,5], calculated twice
        if (y-x) == 1:
            for width in range(1, 4):
                square_list = check_square(x, width)
                for square in square_list:
                    if square in lines_list:
                        switch = True
                    else:
                        switch = False
                        break
                if switch: count_square += 1
    return count_square



if __name__ == '__main__':
    print("Example:")
    print(checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]))

'''
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
