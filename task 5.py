if __name__ == '__main__':
    my_string = 't1234h1234i1234saaaaiaaaasbbbbm1234yaaaapbbbbabbbbsaaaas1234'
    corrected_string = my_string.replace('1234', '')
    corrected_string_2 = corrected_string.replace('bbbb', '')
    corrected_string_3 = corrected_string_2.replace('aaaa', '')
    print(corrected_string_3)