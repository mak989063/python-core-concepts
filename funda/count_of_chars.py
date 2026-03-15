def count_chars(sentence):
    digit_count = 0
    lower_case_count = 0
    upper_case_count = 0
    space_count = 0
    for char in sentence:
        if char.isdigit():
            digit_count += 1

        if char.isupper():
            upper_case_count += 1

        if char.islower():
            lower_case_count += 1

        if char.isspace():
            space_count += 1

    print(f"Number of digits: {digit_count}")
    print(f"Number of upper case: {upper_case_count}")
    print(f"Number of lower case: {lower_case_count}")
    print(f"Number of spaces: {space_count}")


count_chars("I am No.1 complan boy")