def compare_capitals(str1: str, str2: str):
    str1 = list(str1)
    str2 = list(str2)

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i].upper() == str2[j]:
                str1[i] = str1[i].upper()

    return ''.join(str1)