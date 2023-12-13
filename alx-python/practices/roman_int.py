def roman_to_int(roman_string):

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    numb = 0

    if roman_string == None or not isinstance(roman_string, str):
        return 0

    for x in roman_string:
        if x not in roman_dict.keys():
            print(f"{x} is not a roman number. pls provide valid roman numbers")
            return 0

    for x in range(len(roman_string) - 1, -1, -1):

        if (x != len(roman_string) - 1):
            if (roman_dict[roman_string[x]] >= roman_dict[roman_string[x + 1]]):
                numb += roman_dict[roman_string[x]]
            else:
                numb += roman_dict[roman_string[x]] * -1
        else:
            numb += roman_dict[roman_string[x]]

    return numb


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
