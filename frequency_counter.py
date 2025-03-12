def count_frequency(string):
    frequency_dict = {}

    for characters in string:
        if characters in frequency_dict:
            frequency_dict[characters] += 1

        else:
            frequency_dict[characters] = 1

    return frequency_dict


input_string = "uryctgniuygcbiquwg4iuqcgtn4oivynoq3i5yivyqoyco4inyoinioruhno"
output = count_frequency(string=input_string)
print(output)