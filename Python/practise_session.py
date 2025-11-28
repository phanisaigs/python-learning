numbers = [ "zero", "one", "two" ,"three", "four", "five", "six", "seven", "eight", "nine"]
n = int(input(" Enter the number between 0 to 9 :  "))
print(numbers[n] if 0 <= n <= 9 else " the number is not  between 0 to 10")
