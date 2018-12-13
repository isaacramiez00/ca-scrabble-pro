# ca-scrabble-pro


#two lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
 "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
 "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3,
 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#zip dict{}
letters_to_points = {letter:point for letter, point in zip(letters, points)}
print(letters_to_points)


#added el to dict{}
letters_to_points[' '] = 0


#function counts points for word
def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letters_to_points:
            point_total += letters_to_points.get(letter)
    return point_total

#brownies = score_word('BROWNIES')
#print(brownies) #16
