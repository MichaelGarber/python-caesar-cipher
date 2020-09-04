def rot13(str):
    cipher = []
    char_to_num = []
    letter = 13

    for s in str:
       char_to_num.append(ord(s))

    for i  in range(len(char_to_num)):
        if char_to_num[i] < 65 + letter and char_to_num[i] >= 65 or char_to_num[i] < 97 + letter and char_to_num[i] >= 97:
            char_to_num[i] = char_to_num[i] + letter
        elif char_to_num[i] >= 90 - letter and char_to_num[i] <= 90 or char_to_num[i] >= 122 - letter and char_to_num[i] <= 122:
            char_to_num[i] = char_to_num[i] - (26 - letter)

    for c in char_to_num:
        cipher.append(chr(c))
    cipher = ''.join(cipher)

    return cipher