def roman(number):
    tuple_num = [
        ("1000", "M"), ("900", "CM"), ("500", "D"), ("400", "CD"),
        ("100", "C"), ("90", "XC"), ("50", "L"), ("40", "XL"),
        ("10", "X"), ("9", "IX"), ("5", "V"), ("4", "IV"), ("1", "I")
    ]
    roman_number = ""
    for digit, character in tuple_num:
        count = number // int(digit)  
        roman_number += character * count  
        number %= int(digit)  
    return roman_number
