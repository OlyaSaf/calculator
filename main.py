PI = 3.14159

def main():
    while True:
        # Display menu
        print("Calculations")
        print("1. Calculate area of a square")
        print("2. Calculate area of a circle")
        print("3. Display palindromes up to 1,000")
        print("4. Exit")
        # Get input
        option = int(input("Enter an option: "))
        
        if 1 <= option <= 4:
            if option == 1:
                print("\n**** Area of a square ****")
                width = int(input("Enter width of square (cm): "))
                print("The area of a square of {}cm = {}cm squared".format(width, area_square(width)))
            elif option == 2:
                print("\n**** Area of a circle ****")
                radius = float(input("Enter radius of circle (cm): "))
                print("The area of a square of {:.2f}cm = {:.2f}cm squared".format(radius, area_circle(radius)))
            elif option == 3:
                print("\n**** Palindromes ****")
                for i in range(1001):
                    if is_palindrome(i):
                        print(i)
            elif option == 4:  #closes application
                break
                print("\n**** Exit ****")
                for i in range(1001):
                    if is_palindrome(i):
                        print(i)

        else:
            print("Invalid option")

def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def area_square(width):
    return width * width

def area_circle(radius):
    return PI * (radius * radius)

if __name__ == "__main__":
    main()