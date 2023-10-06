# roman to decimal number

def rom_to_decimal(roman):
    roman_numerals = {'i':1,'v':5,'x':10}
    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            decimal -= value
        else:
            decimal +=value
        prev_value = value
    return decimal
roman_numeral = input("Enter a roman numeral: ")
decimal_value = rom_to_decimal(roman_numeral.upper())
print(f"the decimal equivalent of {roman_numeral} is {decimal_value}")