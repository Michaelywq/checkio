from typing import List
dir = ((-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1))

def find_max(land_map, row, column):
    location = [(row, column)]
    land_map[row][column] = -1
    max_num = 1
    while location:
        row, column = location.pop()
        for dx, dy in dir:
            # have to use new_row and new_column.
            new_row = row + dx
            new_column = column + dy
            if new_row >= 0 and new_column >= 0 and \
                    new_row < len(land_map) and new_column < len(land_map[0]) \
                    and land_map[new_row][new_column] > 0:
                location.append((new_row, new_column))
                max_num += 1
                land_map[new_row][new_column] = -1
    return max_num

def checkio(land_map: List[List[int]]) -> List[int]:
    number_list = list()
    for row in range(len(land_map)):
        for column in range(len(land_map[0])):
            if land_map[row][column] > 0:
                number_list.append(find_max(land_map, row, column))
    return sorted(number_list)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
