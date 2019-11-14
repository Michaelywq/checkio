def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    # must convert number by this. or it will output 999999Y, rather than 1000000Y
    import decimal
    number = decimal.Decimal(number)


    for pw in powers:
        if abs(number) < base:
            break
        elif decimals and pw != powers[-1]:
            number /= base
        elif pw != powers[-1]:
            number = int(number/base)

    return '{:.{de}f}'.format(number, de=decimals) + pw + suffix


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(friendly_number(10**32))
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
