#Question 1
def count_vowels(word):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in word:
         if i in vowel:
              count += 1
    return count

print(count_vowels("2024NYUDSBootcamp"))

#Question 2
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

#Question 3
for number in range(1, 21):
    print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")

#Question 4:
def sum_of_int(a,b):
    return a + b
 #I know there is no need to print it out... I just want to check if I am correct :)
print(sum_of_int(1,7)) 


