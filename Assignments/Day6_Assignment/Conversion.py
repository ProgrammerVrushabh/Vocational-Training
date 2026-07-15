# decimal to binary
def decimalToBinary(num):
    return bin(num)
#Binary to decimal
def binaryToDecimal(binary):
    return(int(binary, 2))
# binary to hexadecimal
def binaryToHexadecimal(binary):
    return hex(int(binary, 2))
# hexadecimal to binary
def hexadecimalToBinary(hexadecimal):
    return bin(int(hexadecimal, 16))
# hexadecimal to decimal
def hexadecimalToDecimal(hexadecimal):
    return int(hexadecimal, 16)
# decimal to hexadecimal
def decimalToHexadecimal(num):
    return hex(num)
# hexadecimal to octal
def hexadecimalToOctal(hexadecimal):
    decimal = hexadecimalToDecimal(hexadecimal)
    return oct(decimal)
# octal to hexadecimal
def octalToHexadecimal(octal):
    decimal = octalToDecimal(octal)
    return decimalToHexadecimal(decimal)
# octal to decimal
def octalToDecimal(octal):
    return int(octal, 8)
# decimal to octal
def decimalToOctal(num):
    return oct(num)

if __name__ == "__main__":
    num=int(input("Enter a decimal number: "))
    print("Decimal to Binary:", decimalToBinary(num))
    print("Decimal to Hexadecimal:", decimalToHexadecimal(num))
    print("Decimal to Octal:", decimalToOctal(num))
    binary=input("Enter a binary number: ")
    print("Binary to Decimal:", binaryToDecimal(binary))
    print("Binary to Hexadecimal:", binaryToHexadecimal(binary))
    hexadecimal=input("Enter a hexadecimal number: ")
    print("Hexadecimal to Decimal:", hexadecimalToDecimal(hexadecimal))
    print("Hexadecimal to Binary:", hexadecimalToBinary(hexadecimal))
    print("Hexadecimal to Octal:", hexadecimalToOctal(hexadecimal))
    octal=input("Enter an octal number: ")
    print("Octal to Decimal:", octalToDecimal(octal))
    print("Octal to Hexadecimal:", octalToHexadecimal(octal))
    
