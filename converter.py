ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands = ["", "M", "MM", "MMM", "MMMM"]

def arab_to_rome(num):

    if (num > 4999) or (type(num).__name__ != 'int'):
        return None

    arabic_thousands = thousands[num // 1000]
    arabic_hundreds = hundreds[num // 100 % 10]
    arabic_tens = tens[num // 10 % 10]
    arabic_ones = ones[num % 10]

    return arabic_thousands \
           + arabic_hundreds \
           + arabic_tens \
           + arabic_ones

if __name__ == '__main__':
    print(arab_to_rome(1221))
    print(arab_to_rome(3426))