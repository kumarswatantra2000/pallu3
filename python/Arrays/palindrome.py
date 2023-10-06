def swatantra(str):

    # cleaning the str
    clean_str = (str.replace(" ", "")).lower()

    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str1 = int(input("Enter a string: "))
if swatantra(str):
    print("it is a palidrome string")
else:
    print("no ia a palindrome string")