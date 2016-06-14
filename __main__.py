from sys import argv


def int_to_word(n):
    word = []
    if n < 0:
        return 'Minus ' + int_to_word(-n)
    elif n == 0:
        word.append('Zero')
    else:
        units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = [
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
            'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = [
            'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion',
            'Octillion', 'Nonillion', 'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion',
            'Quindecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Novemdecillion', 'Vigintillion']

        s = str(n)
        group = (len(s) + 2) // 3
        l = group * 3
        s = s.zfill(l)
        tl = len(thousands)
        for i in range(0, l, 3):
            h, t, u = int(s[i]), int(s[i + 1]), int(s[i + 2])
            g = group - (i // 3 + 1)
            if h > 0:
                word.append(units[h])
                word.append('Hundred')

            if t > 1:
                word.append(tens[t])
                if u > 0:
                    word.append(units[u])
            elif t == 1:
                word.append(teens[u])
            else:
                if u > 0:
                    word.append(units[u])

            if g > 0 and (h + t + u) > 0:
                idx = (g - 1) % tl
                word.append(thousands[idx])

    return ' '.join(word)

if __name__ == '__main__':
    ln = len(argv)
    if ln == 1:
        print('Error: No data input')
    else:
        print(int_to_word(int(argv[1])))
