# Given a number in Roman numeral format, convert it to decimal.

def roman_to_decimal(s):
    roman_numbers = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    total = 0
    prev_value = 0
    for i in s[::-1]: # reverse the string
        current_value = roman_numbers[i]
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value
    return total

print(roman_to_decimal('XV'))

