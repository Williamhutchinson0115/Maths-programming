import random
letters = "abcdefghijklmnopqrstuvwxyz"
input_letter = random.choice(letters)

# don't edit the code above
# put your code below here:
print(input_letter)
if input_letter in "aeiou":
    print("the letter is a vowel")
elif input_letter in "y":
        print("the letter is y")
        
else:
        print("the letter is a consonant")


