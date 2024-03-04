def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for letter in word if letter in vowels)

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

for number in range(1, 21):
    print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")

def sum_of_int(a,b):
    return a+b

