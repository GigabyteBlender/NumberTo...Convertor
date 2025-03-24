class NumberConverter:
    """Base class for all number converters"""
    
    def convert(self):
        """Template method for conversion process"""
        try:
            value = self._get_input()
            result = self._perform_conversion(value)
            self._display_result(result)
        except ValueError as e:
            print(f"Error: {e}")
        except KeyError:
            print("Error: Invalid input format.")
    
    def _get_input(self):
        """Get input from user - to be overridden by subclasses"""
        raise NotImplementedError
    
    def _perform_conversion(self, value):
        """Perform the conversion - to be overridden by subclasses"""
        raise NotImplementedError
    
    def _display_result(self, result):
        """Display the conversion result"""
        print(f"Result: {result}")


class RomanToDecimalConverter(NumberConverter):
    """Converts Roman numerals to decimal numbers"""
    
    def _get_input(self):
        roman = input('Enter the Roman numeral to convert: ').strip().upper()
        if not all(c in 'IVXLCDM' for c in roman):
            raise ValueError("Invalid Roman numeral. Use only I, V, X, L, C, D, M.")
        return roman
    
    def _perform_conversion(self, roman):
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


class DecimalToRomanConverter(NumberConverter):
    """Converts decimal numbers to Roman numerals"""
    
    def _get_input(self):
        try:
            decimal = int(input('Enter the decimal number to convert (1-3999): '))
            if not 1 <= decimal <= 3999:
                raise ValueError("Roman numerals can only represent numbers from 1 to 3999.")
            return decimal
        except ValueError:
            raise ValueError("Please enter a valid integer.")
    
    def _perform_conversion(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman_num = ''
        i = 0
        
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


class DecimalToBinaryConverter(NumberConverter):
    """Converts decimal numbers to binary"""
    
    def _get_input(self):
        try:
            decimal = int(input('Enter the decimal number to convert to binary: '))
            if decimal < 0:
                raise ValueError("Please enter a non-negative integer.")
            return decimal
        except ValueError:
            raise ValueError("Please enter a valid integer.")
    
    def _perform_conversion(self, num):
        return bin(num).replace("0b", "")


class BinaryToDecimalConverter(NumberConverter):
    """Converts binary numbers to decimal"""
    
    def _get_input(self):
        binary = input('Enter the binary number to convert to decimal: ').strip()
        if not all(bit in '01' for bit in binary):
            raise ValueError("Binary numbers can only contain 0s and 1s.")
        if not binary:
            raise ValueError("Please enter a valid binary number.")
        return binary
    
    def _perform_conversion(self, binary):
        return int(binary, 2)


class DecimalToHexadecimalConverter(NumberConverter):
    """Converts decimal numbers to hexadecimal"""
    
    def _get_input(self):
        try:
            decimal = int(input('Enter the decimal number to convert to hexadecimal: '))
            if decimal < 0:
                raise ValueError("Please enter a non-negative integer.")
            return decimal
        except ValueError:
            raise ValueError("Please enter a valid integer.")
    
    def _perform_conversion(self, num):
        return hex(num).replace("0x", "").upper()


class HexadecimalToDecimalConverter(NumberConverter):
    """Converts hexadecimal numbers to decimal"""
    
    def _get_input(self):
        hex_num = input('Enter the hexadecimal number to convert to decimal: ').strip().upper()
        if not all(c in '0123456789ABCDEF' for c in hex_num):
            raise ValueError("Hexadecimal numbers can only contain 0-9 and A-F.")
        if not hex_num:
            raise ValueError("Please enter a valid hexadecimal number.")
        return hex_num
    
    def _perform_conversion(self, hex_num):
        return int(hex_num, 16)


def display_menu():
    """Display the main menu options"""
    print("\n===== Number Conversion System =====")
    print("1. Roman numeral to decimal")
    print("2. Decimal to Roman numeral")
    print("3. Decimal to binary")
    print("4. Binary to decimal")
    print("5. Decimal to hexadecimal")
    print("6. Hexadecimal to decimal")
    print("7. Exit")
    print("===================================")


def main():
    """Main program function"""
    converters = {
        1: RomanToDecimalConverter(),
        2: DecimalToRomanConverter(),
        3: DecimalToBinaryConverter(),
        4: BinaryToDecimalConverter(),
        5: DecimalToHexadecimalConverter(),
        6: HexadecimalToDecimalConverter()
    }
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-7): "))
            
            if choice == 7:
                print("Thank you for using the Number Conversion System. Goodbye!")
                break
            
            if choice not in converters:
                print("Invalid choice. Please enter a number between 1 and 7.")
                continue
                
            converters[choice].convert()
            
        except ValueError:
            print("Please enter a valid number.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()