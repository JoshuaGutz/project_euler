# 89 Roman numerals

def explanation():
    # The rules for writing Roman numerals allow for many ways of writing 
    # each number (see About Roman Numerals...). However, there is always a 
    # "best" way of writing a particular number.

    # For example, the following represent all of the legitimate ways of 
    # writing the number sixteen:

    # IIIIIIIIIIIIIIII
    # VIIIIIIIIIII
    # VVIIIIII
    # XIIIIII
    # VVVI
    # XVI

    # The last example being considered the most efficient, as it uses the 
    # least number of numerals.

    # The 11K text file, roman.txt, contains one thousand numbers written in 
    # valid, but not necessarily minimal, Roman numerals; that is, they are 
    # arranged in descending units and obey the subtractive pair rule (see 
    # About Roman Numerals... for the definitive rules for this problem).

    # Note: You can assume that all the Roman numerals in the file contain 
    # no more than four consecutive identical units.

    # I = 1
    # V = 5
    # X = 10
    # L = 50
    # C = 100
    # D = 500
    # M = 1000
    pass

# Find the number of characters saved by writing each of these in their 
# minimal form.

def import_file(): # generates roman_strings and count_roman_characters
    global roman_strings, count_roman_characters
    my_file = open("roman.txt", "r")
    roman_strings = []
    count_roman_characters = []
    for i in range(1000):
        roman_strings.append(str(my_file.readline())[:-1])
        count_roman_characters.append(len(roman_strings[i]))
    my_file.close()
import_file()

def print_tests():
    print roman_strings[0], len(roman_strings[0])
    print count_roman_characters[0]
    print roman_strings[1], len(roman_strings[1])
    print count_roman_characters[1]
    print roman_strings[2], len(roman_strings[2])
    print count_roman_characters[2]
    print roman_strings[-1], len(roman_strings[-1])
    print count_roman_characters[-1]
# print_tests()

roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def convert_roman_to_arabic(roman_string):
    arabic = 0
    arabic_list = []
    for i in roman_string:
        arabic_list.append(roman[i])
    print arabic_list
    
    for i in range(len(arabic_list) - 1):
        if arabic_list[i] > max(arabic_list[i + 1:]):
            arabic += arabic_list[i]
        elif arabic_list[i] == max(arabic_list[i + 1:]):
            pass
            ###NEED CODE HERE
            if i + 1 == len(arabic_list) - 1:
                arabic += arabic_list[i + 1]
        else:
            arabic += arabic_list[i + 1] - arabic_list[i]
    return arabic
    
print convert_roman_to_arabic("MDCLXVII")
print 1000+500+100+50+10+5+1+1
print convert_roman_to_arabic("XLI")