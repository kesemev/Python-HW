"""Kesem Even Hen, 208055483"""
"""-----------------Question-1---------------"""

"""Write a program the receives a string and a rotation as input and 
outputs the encoded string using Caesar’s Cipher. 
only [A-Z] characters as valid input. """
def caesar_cipher(message, key):
    translated = ''
    key = key % 26
    for symbol in message:
        if symbol.isalpha():
            """The isalpha() string method will returמ True if the string is an uppercase or lowercase letter from A to Z. If the string contains any non-letter characters, then isalpha() will return False. """
            num = ord(symbol)
            """The ord() method returns an integer representing the Unicode code point of the given Unicode character."""
            num -= key
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

print(caesar_cipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3))
# => 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'
print(caesar_cipher('THOSE WHO DARE TO FAIL MISERABLY CAN ACHIEVE GREATLY', -7))
# => 'AOVZL DOV KHYL AV MHPS TPZLYHISF JHU HJOPLCL NYLHASF'

"""-------------------------------------------"""

"""-----------------Question-2---------------"""

"""The function should receive the player's action and return the number
 that represents the winner. 0 if tied """
def rock_paper_scissors(first, second):
    if first == second:
        return 0
    elif first == "rock":
        if second == "paper":
            return 2
        else:
            return 1
    elif first == "paper":
        if second == "scissors":
            return 2
        else:
            return 1
    elif first == "scissors":
        if second == "rock":
            return 2
        else:
            return 1


print(rock_paper_scissors('rock', 'scissors'))  # => 1
print(rock_paper_scissors('scissors', 'paper'))  # => 1
print(rock_paper_scissors('rock', 'paper'))  # => 2

"""-------------------------------------------"""

"""-----------------Question-3---------------"""

"""converts Arabic numbers to the Roman numeral notation.
there are no negative values and that the largest accepted value is 4000."""
def to_roman(i):
    map = zip(
        (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
        ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    )
    result = []
    for integer, numeral in map:
        count = int(i / integer)
        result.append(count * numeral)
        """The method append() appends a passed obj into the existing list."""
        i -= integer * count
    return ''.join(result)
    """The join() method provides a flexible way to concatenate string."""


print(to_roman(1))  # => 'I'
print(to_roman(51))  # => 'LI'
print(to_roman(199))  # => 'CXCIX'
print(to_roman(4123))  # => 'MMMMCXXIII'

"""-------------------------------------------"""

"""-----------------Question-4---------------"""

"""The function should receive the value, current unit of measure, and desired conversion. 
function that converts from the Imperial to the Metric measuring system """
def to_metric(val, Imperial, Metric):
    imperial_map = {'inch': 0.0254, 'foot': 0.3048, 'mile': 1609.344, 'yard': 0.9144}
    metric_map = {'km': 0.001, 'm': 1, 'dm': 10, 'cm': 100, 'mm': 1000}
    return val*imperial_map[Imperial]* metric_map[Metric]

print(to_metric(1, 'inch', 'cm'))  # => 2.54
print(to_metric(1, 'foot', 'm'))  # => 0.3048
print(to_metric(1, 'mile', 'cm'))  # => 160934
print(to_metric(1, 'yard', 'mm'))  # => 914.4

"""-------------------------------------------"""

"""-----------------Question-5---------------"""

"""The function should recieve a integer value that determines the amount 
of iterations before returning the approximation."""
def approx_pi(terms):
    result = 0.0
    sign = 1.0
    for n in range(terms):
        result += sign / (1.0 + 2.0 * n)
        sign = -sign
    return result * 4


print(approx_pi(5))  # => 3.3396825396825403
print(approx_pi(623))  # => 3.143197788992502

"""-------------------------------------------"""

"""-----------------Question-6---------------"""

"""Using recursion, determine whether or not a sorted collection contians a provided value."""
def binary_search(val, col):
    if len(col) == 0:
        return False
    mid = len(col) // 2
    if val == col[mid]:
        return True
    if val > col[mid]:
        return binary_search(val, col[mid + 1:])
    return binary_search(val, col[0:mid])


print(binary_search(4, [2, 3, 6, 100]))  # => False
print(binary_search(4, [4, 6, 100]))  # => True
print(binary_search(4, []))  # => False

"""------------------------------------------"""

"""-----------------Question-7---------------"""

"""Using Euclidean Algorithm and recursion,
 etermine the GCD for two given numbers"""
def GCD(a, b):
    while (b):
        a, b = b, a % b
    return a


print(GCD(45, 54))  # => 9
print(GCD(51, 100))  # => 1
print(GCD(60, 48))  # => 12

"""-------------------------------------------"""

"""-----------------Question-8---------------"""

"""Using recurision, determine whether a provided input contains balanced parenthesis."""
def is_balanced(s):
    counter = 0
    def temp(s):
        nonlocal counter
        if s == "":
            return True
        elif s[-1] == ')':
            counter += 1
            return True and temp(s[0:len(s) - 1])
        elif s[-1] == '(':
            counter -= 1
            if counter < 0:
                return False
            return True and temp(s[0:len(s) - 1])
    return temp(s) and counter == 0


print(is_balanced('(()()()())'))  # => True
print(is_balanced('(((())))'))  # => True
print(is_balanced('(()((())())))'))  # => False
print(is_balanced('((((((())'))  # => False
print(is_balanced('((())'))  # => False
print(is_balanced('(())())))'))  # => False

"""-------------------------------------------"""

"""-----------------Question-9---------------"""

"""a function to computing square roots using the Babylonian method"""
def babylonian(num):
    if num == 0:
        return 0
    r = num / 2.0
    r2 = r + 1
    while (r != r2):
        r2 = r
        r = (r + (num / r)) / 2
    return r


print(babylonian(2))  # =>  1.414213562373095
print(babylonian(101))  # =>  10.04987562112089
print(babylonian(11))  # =>  3.3166247903554
print(babylonian(100))  # =>  10
print(babylonian(0))  # =>  0

"""-------------------------------------------"""
