def roman_to_decimal(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10}
    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        if roman_dict[numeral] >= prev_value:
            decimal += roman_dict[numeral]
        else:
            decimal -= roman_dict[numeral]
        prev_value = roman_dict[numeral]

    return decimal
for i in range(1, 11):
    roman_numeral = 'I' * i
    decimal_value = roman_to_decimal(roman_numeral)
    print(f"{roman_numeral} in Roman numerals is {decimal_value} in decimal")