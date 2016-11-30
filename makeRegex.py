#!/usr/bin/python
# To help me with major system mnemonics
# Used with visca.com/regexdict, a regex dictionary
# 0: s, z
# 1: t, d
# 2: n
# 3: m
# 4: r
# 5: l
# 6: g, j
# 7: k, c
# 8: f, v
# 9: p, b
import regex_dict

mapping = {'0': 'sz',
           '1': 'td',
           '2': 'n',
           '3': 'm',
           '4': 'r',
           '5': 'l',
           '6': 'gj',
           '7': 'kc',
           '8': 'fv',
           '9': 'pb'}

while 1:
    stringToConvert = raw_input("Enter number: ")
    if stringToConvert == "quit":
        break
    notReserved = "[^sztdnmrlgjkcfvpb]*"
    listStrings = [notReserved]

    for digit in stringToConvert:
        listStrings.append("[" + mapping[digit] + "]" + notReserved)

    fullRegexString = "^" + ''.join(listStrings) + "$"
    # print fullRegexString
    print "/**************/"
    print "/* Nouns Only */"
    print "/**************/"
    regex_dict.printNouns(fullRegexString)

    listStrings1 = [notReserved]
    listStrings2 = [notReserved]

    digitIndex = 0
    for digit in stringToConvert:
        if digitIndex < len(stringToConvert)/2:
            listStrings1.append("[" + mapping[digit] + "]" + notReserved)
        else:
            listStrings2.append("[" + mapping[digit] + "]" + notReserved)
        digitIndex=digitIndex+1

    fullRegexString1 = "^" + ''.join(listStrings1) + "$"
    fullRegexString2 = "^" + ''.join(listStrings2) + "$"
    print "/**************/"
    print "/* Adjectives */"
    print "/**************/"
    regex_dict.printAdjectives(fullRegexString1)
    print "/*********/"
    print "/* Nouns */"
    print "/*********/"
    regex_dict.printNouns(fullRegexString2)
