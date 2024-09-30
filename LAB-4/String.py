# 2A
X = "India.is.my.country"
newstring = X.replace('.', ',')
print("New string is: ", newstring)

# 2B
Y = "M.A.N.I.P.A.L"
charremove= 'A'  
removedstring = Y.replace(charremove, '')
print("New string is: ",removedstring)

# 2C
removedots = Y.replace('.', '')
print("New string after removing: ", removedots)

#3
strings = ["banana", "apple", "orange", "mango", "kiwi"]
sortedStrings = sorted(strings)
print("Sorted strings:", sortedStrings)

#4
userInput = input("Enter a string: ")
reversedString = userInput[::-1]
print("Reversed string:", reversedString)

#5
user_input = input("Enter a string: ")
is_digits = user_input.isdigit()
print("Contains only digits:", is_digits)

#6
vowels = "aeiouAEIOU"
string = input("Enter a string to count vowels: ")
count = sum(1 for char in string if char in vowels)
print(count)