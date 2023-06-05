def perevod_cifr(stroka):
    Slovar = {"M" : 1000,"D" : 500,"C" : 100,"L" : 50,"X" : 10,"V" : 5,"I" : 1}
    SLOVAR = []
    check_1 = []
    check_2 = "x"
    check_3 = []
    cifra = 0

    if stroka != "":
        for i in stroka:

            if check_2 != i:
                check_1.append(stroka.count(i))
                SLOVAR.append(i)
            check_2 = i

        for i in SLOVAR:
            check_3.append(Slovar[i])

        if len(check_3) == 2:
            if check_3[0] > check_3[1]:
                cifra += check_3[0] * check_1[1] + check_3[1] * check_1[1]
            else:
                cifra += check_3[1] * check_1[1] - check_3[0] * check_1[0]
        elif len(check_3) == 1:
            cifra += check_3[0] * check_1[0]

        else:
            cifra += check_3[0]

            ch = len(check_3)
            
            for i in range(1,len(check_3) - 1,2):

                if check_3[i-1] > check_3[i] > check_3[i+1]:
                    cifra += check_3[i] * check_1[i] + check_3[i+1] * check_1[i+1]

                else:
                    cifra += check_3[i+1] * check_1[i+1] - check_3[i] * check_1[i]
            if len(check_3) % 2 == 0:
                cifra += check_3[ch-1] * check_1[ch-1]



    return cifra

def Test():
    assert perevod_cifr("XVI") == 16, "Ошибка перевода числа"
    assert perevod_cifr("I") == 1, "Ошибка 1 числа"
    assert perevod_cifr("MCDLXIV") == 1464, "Ошибка длинного числа"
    assert perevod_cifr("") == 0 , "Ошибка пустой строки"
    assert perevod_cifr("II") == 2, "Ошибка уменьшение числа"
    assert perevod_cifr("XVII") == 17, "Ошибка 1"
    assert perevod_cifr("XIIV") == 13, "Ошибка 2"
    assert perevod_cifr("IIX") == 8, "Ошибка 3"
    assert perevod_cifr("MCCDII") == 1302, "Ошибка 4"
print(perevod_cifr(input()))
Test()


def reversed_cifr(cifra):
    Slovar_1 = {1000 : "M",500 : "D",100 : "C",50 : "L",10 : "X",5 : "V",1 : "I"}
    check = 0
    perevod = ""
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""


    stroka = str(cifra)

    for i in reversed(stroka):
        beta = int(i)
        if check == 0:
            if beta < 4:
                Num_1 = beta
                str1 += ("I" * Num_1)
                check += 1
            elif beta >= 4 and beta <=5:
                Num_1 = 5 - beta
                str1 += ("I" * Num_1) + "V"
                check += 1
            else:
                Num_1 = beta - 5
                str1 += "V" + ("I" * Num_1)
                check += 1
        elif check == 1:
            if beta < 4:
                Num_2 = beta
                str2 += ("X" * Num_2)
                check += 1
            elif beta >= 4 and beta <=5:
                Num_2 = 5 - beta
                str2 += ("X" * Num_2) + "L"
                check += 1
            else:
                Num_2 = beta - 5
                str2 += "L" + ("X" * Num_2)
                check += 1
        elif check == 2:
            if beta < 4:
                Num_3 = beta
                str3 += ("C" * Num_3)
                check += 1
            elif beta >= 4 and beta <=5:
                Num_3 = 5 - beta
                str3 += ("C" * Num_3) + "D"
                check += 1
            else:
                Num_3 = beta - 5
                str3 += "D" + ("C" * Num_3)
                check += 1
        else:
            str4 += "M" * beta

    perevod += str4 + str3 + str2 + str1

    return perevod


