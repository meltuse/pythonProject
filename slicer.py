if __name__ == '__main__':
    my_string = 'yooooouuuuupppppaaaaaaaassssssseeeeeedd'.capitalize()
    corrected_string = my_string.replace('oooo', '')
    corrected_string_2 = corrected_string.replace('uuuu', '')
    corrected_string_3 = corrected_string_2.replace('pppp', '')
    corrected_string_4 = corrected_string_3.replace('aaaaaaa', '')
    corrected_string_5 = corrected_string_4.replace('ssss', '')
    corrected_string_6 = corrected_string_5.replace('ssss', '')
    corrected_string_7 = corrected_string_6.replace('eeeee', '')
    corrected_string_8 = corrected_string_7.replace('d', '', 1)

    print(corrected_string_8)

