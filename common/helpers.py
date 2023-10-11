from math import ceil

def toRadix(radix, num, minWords=1):
    mask = (1 << radix) - 1
    pad = (radix // 4)
    outStr = []
    outNum = []
    numWords = ceil((len(bin(num))-2) / radix)
    if minWords > numWords: numWords += minWords - numWords
    for i in range(0, numWords):
        t = (num >> (i * radix)) & mask
        outNum.append(t)
        outStr.append('0x{num:0{p}x}'.format(num = t, p = pad))
    return '{}'.format(outStr).replace('[', '{').replace(']', '}').replace('\'', ''), outNum