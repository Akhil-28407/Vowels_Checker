word = input("Enter a word: ")
vowels = "aeiouAEIOU"
if any(char in vowels for char in word):
    print("The word contains vowels.")
    print("The vowels present are: ", end="")
    for char in word:
        if char in vowels:
            print(char, end=" ")
    print()
else:
    print("The word does not contain vowels.")
