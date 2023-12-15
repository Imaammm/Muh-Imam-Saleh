def SevenSegmentDisplay(num):
    patterns = [
        [" 444 ", "  4  ", "  4  ", "  4  ", " 444 "],
        ["4   4", "   4 ", "   4 ", "   4 ", "   4 "],
        [" 444 ", "   4 ", " 444 ", "4   ", " 444 "],
        ["444  ", "   4 ", " 444 ", "   4 ", "444  "],
        ["4  4 ", "4   4", "44444", "    4", "    4"],
        ["44444", "4    ", "4444 ", "    4", "4444 "],
        [" 444 ", "4    ", "4444 ", "4   4", " 444 "],
        ["44444", "   4 ", "   4 ", "   4 ", "   4 "],
        [" 444 ", "  4  ", " 444 ", "  4  ", " 444 "],
        [" 444 ", "  4  ", " 4444", "    4", "444  "]
    ]

    print("Seven Segment Display:")
    print("----------------------")
    for row in range(5):
        for digit in str(num):
            digit = int(digit)
            print(patterns[digit][row], end=" ")
            if digit < 9:
                print("|", end=" ")
            else:
                print()
        if row == 4:
            print("----------------------")
        else:
            print()

def displayTruthTable(num):
    print("Truth Table for Binary Number:")
    print("--------------------------------------")
    print(" Decimal | Binary |")
    print("--------------------------------------")
    
    for digit in str(num):
        digit = int(digit)
        binary = bin(digit)[2:].zfill(4)
        print(f"    {digit}    |   {binary}   |")
        print("--------------------------------------")

def main():
    num = -1
    while num < 0:
        try:
            num = int(input("Masukkan angka yang bukan negatif: "))
            if num < 0:
                print("tolong masukkan angka yang bukan negatif.")
        except ValueError:
            print("Angka salah. tolong masukkan angka yang benar.")

    displayTruthTable(num)
    SevenSegmentDisplay(num)

if __name__ == "__main__":
    main()
