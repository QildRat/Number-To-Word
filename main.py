def group_number(number):
    number_length = len(number)
    remainder = number_length % 3
    group_num = []

    for i in range(3, number_length + 1, 3):
        start = number_length - i
        end = start + 3

        three_digit = number[start:end]
        group_num.append(three_digit)

    if remainder > 0:
        digit = number[:remainder]
        group_num.append(digit)

    return group_num


def converted_number(number):
    word_result = ""
    number = int(number)

    if number == 0:
        pass

    else:

        if number >= 100:
            n = int(number / 100)  # whole number
            word_result += f"{numWord[n]} hundred "

        tens = number % 100
        if tens in numWord:
            word_result += numWord[tens]

        elif tens == 0:
            pass

        else:  # kapag wala
            first_digit = int(str(tens)[0])
            second_digit = int(str(tens)[-1])

            if tens < 20:
                word_result += f"{numWord[second_digit]}{TEEN}"
            elif tens < 30:
                word_result += f"{numWord[20]} {numWord[second_digit]}"
            elif tens < 40:
                word_result += f"{numWord[30]} {numWord[second_digit]}"
            elif tens < 50:
                word_result += f"{numWord[40]} {numWord[second_digit]}"
            elif tens < 60:
                word_result += f"{numWord[50]} {numWord[second_digit]}"
            else:
                first_word = ""
                second_word = ""

                if first_digit == 8:
                    first_word += "eigh"
                else:
                    first_word += f"{numWord[first_digit]}"

                if second_digit == 0:
                    second_word = ""
                else:
                    second_word += numWord[second_digit]

                word_result += f"{first_word}{TY} {second_word}"

    return word_result


# ----- CODE HERE -----

numWord = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"
}

groupWord = {5: "trillion", 4: "billion", 3: "million", 2: "thousand"}

TEEN = "teen"
TY = "ty"

# ----- CODE BODY -----

number_input = input("NUMBER TO WORD CONVERTER.\nPlease enter a number:\n")

# store numbers into groups.
group_list = group_number(number_input)  # end to beginning.

# convert number into word.
number_word_output = ""
group_n = len(group_list)

for group in group_list[::-1]:

    if int(group) == 0:
        pass

    else:
        number_word = converted_number(group)

        if group_n < 2:
            number_word_output += f"{number_word}."
        else:
            group_name = groupWord[group_n]
            number_word_output += f"{number_word} {group_name}, "
    group_n -= 1

number_str = ""

for num in group_list[::-1]:
    number_str += f"{num} "

print(number_str)
print("-" * len(number_str))
print(number_word_output)
