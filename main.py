def get_hundred_count(number):
    """get how many times number is divisible by 100 and return the extracted word."""
    word = ""
    number = int(number)
    if number > 100:
        num = int(number / 100)
        h_word = f"{numWord[num]} hundred "
        word += h_word
    return word


def get_tens_count(number):
    """get the remainder of number using modulo by 100 and return the extracted word."""
    num = int(number) % 100
    second_digit = int(str(num)[-1])
    first_digit = int(str(num)[0])
    if first_digit == 0:
        pass
    if num not in numWord:
        if num < 20:
            word = f"{numWord[second_digit]}{TEEN}"
        elif num < 30:
            word = f"{numWord[20]} {numWord[second_digit]}"
        elif num < 40:
            word = f"{numWord[30]} {numWord[second_digit]}"
        elif num < 50:
            word = f"{numWord[40]} {numWord[second_digit]}"
        elif num < 60:
            word = f"{numWord[50]} {numWord[second_digit]}"
        else:
            word = f"{numWord[first_digit]}{TY} {numWord[second_digit]}"

    else:
        word = f"{numWord[num]}"
    return word


def extract_number(number):
    """combine and return the extracted word from get_hundred_count and get_tens_count function. """
    word_result = f"{get_hundred_count(number)}{get_tens_count(number)}"
    return word_result


# CODE HERE ------------------------------------------------------------------------------------------------------
numWord = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"
}

groupWord = {5: ["trillion"], 4: ["billion"], 3: ["million"], 2: ["thousand"], 1:[]}

TEEN = "teen"
TY = "ty"

# BODY ----------------------------------------------
number_input = input("NUMBER TO WORD CONVERTER. \nPlease enter a number:\n")
number_length = len(number_input)

n = 0

for i in range(3, number_length, 3):
    start = number_length - i # 3 - 3
    end = (number_length + 3) - i # 6-3

    digit = number_input[start:end]
    n += 1
    groupWord[n].insert(0, digit)

remainder = number_length % 3

if remainder > 0:
    n += 1
    start = 0
    end = remainder
    digit = number_input[start:end]
    groupWord[n].insert(0, digit)

print(groupWord)
# group1 = number_input[-3:]
# group2 = number_input[-6:-3]
# group3 = number_input[-9:-6]
# group4 = number_input[-12:-9]
# group5 = number_input[-15:-12]
#
# numWordOutput = ""
#
# group_list = [group5, group4, group3, group2]
# n = 6
# for group_num in group_list:
#     n -= 1
#     numWordOutput += f"{extract_number(group_num)} {groupWord[n]}, "
#
# numWordOutput += f"{extract_number(group1)}."
#
# print(number_input)
# print("-" * len(numWordOutput))
# print(numWordOutput)

# PROBLEM:
# only works if number input is in trillion group.
