class RomanNumerals():

    @classmethod
    def to_roman(cls, number):
        symbol_dict = dict(zip((1, 5, 10, 50, 100, 500, 1000), ('I', 'V', 'X', 'L', 'C', 'D', 'M')))
        result_list = []
        for i, j in zip(str(number), range(len(str(number)), 0, -1)):
            if j==4:
                result_list.append((number // 1000) * symbol_dict[1000])
                continue
            if i in ('4', '9'):
                result_list.append(symbol_dict[int('1' + ('0' * (j - 1)))])
                result_list.append(symbol_dict[int(str(int(i) + 1) + ('0' * (j - 1 + (int(j) // 5))))])
                continue
            if int(i) >= 5:
                result_list.append(symbol_dict[int('5' + ('0' * (j - 1)))])
                if int(i) > 5:
                    for s in range(int(i)-5):
                        result_list.append(symbol_dict[int('1' + ('0' * (j - 1)))])
                continue
            if int(i)<4:
                if int(i) == 0:
                    continue
                for l in range(int(i)):
                    result_list.append(symbol_dict[int('1' + ('0' * (j - 1)))])

        return ''.join(result_list)

    @classmethod
    def from_roman(cls, roma):
        number=0
        symbol_dict = dict(zip(('I', 'V', 'X', 'L', 'C', 'D', 'M'), (1, 5, 10, 50, 100, 500, 1000)))
        for i in roma:
            number+=symbol_dict[i]
        return number

print(RomanNumerals.to_roman(1000))
print(RomanNumerals.from_roman('M'))