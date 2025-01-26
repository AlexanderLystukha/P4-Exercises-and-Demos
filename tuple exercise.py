#exercise

letters = ["A", "B", "C", "D", "E", "F"]

#prints needs to be

#(A, B)
#(B, C)
#...
#(E, F)

oldLetter = ""

for letter in letters:
    if letter != "A":
        p1 = (oldLetter, letter)
        print(p1)

    oldLetter = letter