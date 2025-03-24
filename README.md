# Number Converter System

A versatile Python application for converting between different number systems: decimal, Roman numerals, binary, and hexadecimal.

## Features

- **Multiple Conversion Options:**
  - Roman numerals to decimal
  - Decimal to Roman numerals
  - Decimal to binary
  - Binary to decimal
  - Decimal to hexadecimal
  - Hexadecimal to decimal

- **User-Friendly Interface:**
  - Clear menu system
  - Guided input prompts
  - Informative error messages

- **Robust Error Handling:**
  - Input validation for all number formats
  - Appropriate range checking
  - Graceful error recovery

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/number-converter.git
cd number-converter
```

No external dependencies are required - just Python 3.x.

## Usage

Run the application:

```bash
python main.py
```

Follow the on-screen menu to select your desired conversion type:

1. Choose a conversion option (1-7)
2. Enter your input according to the prompts
3. View the conversion result
4. Press Enter to return to the main menu

## Code Structure

The application is built using object-oriented programming principles:

- `NumberConverter`: Abstract base class with template methods
- Specialized converter classes for each number system
- Clean separation of input, conversion, and output operations

## Examples

### Roman to Decimal Conversion
```
Enter the Roman numeral to convert: XIV
Result: 14
```

### Decimal to Roman Conversion
```
Enter the decimal number to convert (1-3999): 42
Result: XLII
```

### Binary to Decimal Conversion
```
Enter the binary number to convert to decimal: 1010
Result: 10
```

## Limitations

- Roman numeral conversion is limited to the range 1-3999
- Negative numbers are not supported for binary and hexadecimal conversions

## Future Enhancements

Planned features for future releases:

- Support for octal number system
- Conversion between non-decimal systems (e.g., binary to hex)
- GUI interface