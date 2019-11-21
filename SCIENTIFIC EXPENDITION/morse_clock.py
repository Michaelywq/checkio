def get_binary(number, weishu):
    return format(int(number), '0' + str(weishu) + 'b')

def checkio(time_string: str) -> str:
    time_list = time_string.split(':')
    time_list = [(x[:1], x[1:]) for x in time_list]
    binary_list = list()
    for i, (x, y) in enumerate(time_list):
        if not y:
            y = x
            x = '0'
        if i == 0:
            x_binary = get_binary(x, 2)
        else:
            x_binary = get_binary(x, 3)

        x_morse = x_binary.replace('0', '.').replace('1', '-')
        y_morse = get_binary(y, 4).replace('0', '.').replace('1', '-')

        binary_list.append(x_morse + ' ' + y_morse)
    return ' : '.join(binary_list)

if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
