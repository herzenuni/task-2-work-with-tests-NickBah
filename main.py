
import json

def readfile(filename):
    """
    >>> readfile('data.json')
    ------------------------------------
    Компания: PARCOE
    E-mail: muriellott@parcoe.com
    Телефон: +1 (983) 418-2041
    Адрес: 623 Hoyt Street, Waverly, Washington, 4681
    ------------------------------------
    Компания: COMTOURS
    E-mail: reedlogan@comtours.com
    Телефон: +1 (801) 482-3149
    Адрес: 334 Batchelder Street, Worcester, Massachusetts, 2966
    ------------------------------------
    Компания: APPLICA
    E-mail: bobbiemathews@applica.com
    Телефон: +1 (966) 405-3143
    Адрес: 991 Sackman Street, Caron, Maine, 5334
    ------------------------------------
    Компания: BOILICON
    E-mail: gilmorehendrix@boilicon.com
    Телефон: +1 (978) 536-2130
    Адрес: 917 Minna Street, Emerald, District Of Columbia, 4497
    ------------------------------------
    Компания: PERMADYNE
    E-mail: stellaworkman@permadyne.com
    Телефон: +1 (997) 448-3432
    Адрес: 696 Brightwater Avenue, Welda, Mississippi, 9203
    'Data printed'
    """
    with open(filename, encoding='utf-8') as data_file:
            data = json.load(data_file)
    if type(data) is not list:
        raise TypeError("File must have wrap as an array")
    for tmp in data:
        print("------------------------------------")
        print("Компания: {}".format(tmp["company"]))
        print("E-mail: {}".format(tmp["email"]))
        print("Телефон: {}".format(tmp["phone"]))
        print("Адрес: {}".format(tmp["address"]))
    return "Data printed"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
