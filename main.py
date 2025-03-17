class ConvertToDecimal:

    def from_roman(self, roman):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        decimal = 0
        prev_value = 0

        for char in reversed(roman):
            value = roman_to_int[char]
            if value < prev_value:
                decimal -= value
            else:
                decimal += value
            prev_value = value

        return decimal

    def Convert(self):
        roman = input('Enter the Roman numeral to convert: ')
        print(self.from_roman(roman))

class ConvertToRoman:

    def to_roman(self, num):

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        
        roman_num = ''
        i = 0
        
        while num > 0:
            for x in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def Convert(self):
        decimal = int(input('Enter the number to convert: '))
        print(self.to_roman(decimal))

class ConvertToBinary:

    def to_binary(self, num):
        return bin(num).replace("0b", "")

    def Convert(self):
        binary = int(input('Enter the number to convert to binary: '))
        print(self.to_binary(binary))

class ConvertToHexadecimal:
    
    def to_hexadecimal(self, num):
        return hex(num).replace("0x", "").upper()

    def Convert(self):
        hexadecimal = int(input('Enter the number to convert to hexadecimal: '))
        print(self.to_hexadecimal(hexadecimal))