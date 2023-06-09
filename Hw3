#!/usr/bin/python

"""
Python Core object Types
"""


def add_binary(a, b):
    """
    This is to review binary operations
    ============================================================
    Given two binary strings, return their sum (also a binary string).
    Return None if one of the input strings are empty or contains characters different than 1 or 0.
    Example 1:
                Input: a = "11", b = "1"
                Output: result = "100"
    Example 2:
                Input: a = "1010", b = "1011"
                Output: result = "10101"
    """
    c=""
    if a == "" or b == "":
        return None
    for i in range(len(a)):
        if a[i] != "0" and a[i] != "1":
            return None
    for i in range(len(b)):
        if b[i] != "0" and b[i] != "1":
            return None
    carry = 0
    diff=len(a)-len(b)
    if diff < 0:
        diff = abs(diff)
        for i in range(diff):
            a = "0" + a
    else:
        for i in range(diff):
            b = "0" + b
    length = len(a)     

    for i in range(length):
        if a[length-(i+1)] == "1" and b[length-(i+1)] == "1" and carry == 1:
            c = "1" + c
        elif a[length-(i+1)] == "1" and b[length-(i+1)] == "0" and carry == 1:
            c = "0" + c
        elif a[length-(i+1)] == "0" and b[length-(i+1)] == "1" and carry == 1:
            c = "0" + c
        elif a[length-(i+1)] == "0" and b[length-(i+1)] == "0" and carry == 1:
            carry = 0
            c = "1" + c
        elif a[length-(i+1)] == "1" and b[length-(i+1)] == "1" and carry == 0:
            carry = 1
            c = "0" + c
        elif a[length-(i+1)] == "1" and b[length-(i+1)] == "0" and carry == 0:
            c = "1" + c
        elif a[length-(i+1)] == "0" and b[length-(i+1)] == "1" and carry == 0:
            c = "1" + c
        elif a[length-(i+1)] == "0" and b[length-(i+1)] == "0" and carry == 0:
            c = "0" + c
    if carry == 1:
        c='1'+ c
    result = c        
    return result

def plus_one(digits):
    """
    This is to review loops and if statements
    ============================================================
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    You can do this in-place!
    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.
    Example 1:
            Input: digits = [1, 2, 3]
            Output: digits = [1, 2, 4]
            Explanation: The array represents the integer 123.
    Example 2:
            Input: digits = [1, 0, 9, 9]
            Output: digits = [1, 1, 0, 0]
    """
    length = len(digits)
    number = 0
    for i in range(length):
        number = (number*10) + digits[i]
    print(number)
    number+=1
    print (number)
    length = 1
    num = number
    while 1 == 1:
        if (num/10) >= 1:
            num = int(num / 10)
            print (num)
            length+=1
        else:
            break
    dig = list(range(length))
    for i in range(length):
        dig[length-(i+1)] = number%10 
        number = int(number/10)
    return dig

def roman_to_integers(roman_string):
    
    """
    This is to review loops, if statements and dictionaries
    ============================================================
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
    Example 1:
        Input: "III"
        Output: 3
    Example 2:
        Input: "IV"
        Output: 4
    Example 3:
        Input: "IX"
        Output: 9
    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.
    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    
    Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    integer = 0
    while len(roman_string) > 0:
        if len(roman_string) == 2 and ( Roman_number.get(roman_string[0])-Roman_number.get(roman_string[1]) ) < 0:
            integer += ( Roman_number.get(roman_string[1]) - Roman_number.get(roman_string[0]) )
            roman_string = ""

        elif len(roman_string) >= 3:
            if ( Roman_number.get(roman_string[0])-Roman_number.get(roman_string[1]) ) < 0:
                integer += ( Roman_number.get(roman_string[1]) - Roman_number.get(roman_string[0]) )
                roman_string = roman_string[2:]

            elif roman_string[0] == roman_string[1] and roman_string[0] == roman_string[2]:
                integer += ( 3*Roman_number.get(roman_string[0]) )
                roman_string = roman_string[3:]

            elif roman_string[0] == roman_string[1]:
                integer += ( 2*Roman_number.get(roman_string[0]) )
                roman_string = roman_string[2:]

            else:
                integer += Roman_number.get(roman_string[0]) 
                roman_string = roman_string[1:]

        elif len(roman_string) == 2:
            if roman_string[0] == roman_string[1]:
                integer += ( 2*Roman_number.get(roman_string[0]) )
                roman_string = roman_string[2:]

            else:
                integer += Roman_number.get(roman_string[0]) 
                roman_string = roman_string[1:]


        else:
            integer += Roman_number.get(roman_string[0])
            roman_string = ""

   
    return integer
