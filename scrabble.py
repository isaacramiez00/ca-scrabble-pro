# ca-scrabble-pro


#two lists
letters = ["A", "B", "C", "d", "E", "F", "G", "H", "I",
 "J", "K", "L", "M", "N", "O", "P", "q", "R", "S", "T", 
 "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3,
 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#zip dict{}
letters_to_points = {letter.upper():point for letter, point in zip(letters, points)}



#added el to dict{}
letters_to_points[' '] = 0
print(letters_to_points)

#function counts points for word
def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letters_to_points.keys():
            point_total += letters_to_points.get(letter)
    return point_total



#dict that maps players to a list of the words they have played
players_to_words ={'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}


#dict to keep track of each players score
#dict gets updated as elements are added to player_to_words{}
#player_to_points = {}
#output: {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

#adds key to player_to_words{}
#par 'word' must be in [] for arg
def play_word(player, word):
    players_to_words[player] = word
    return 

play_word('hawk_lover99', ['BREAD'])   
play_word('gucci5', ['GUCCI', 'YOUNG', 'GADGET'])
players_to_words['gucci5'] += ['falls']
print(players_to_words) #updates

#update_point_totals() — turn your nested loops into a function that you can 
#call any time a word is played
def players_score(): 
    player_to_points = {}
    for player, words in players_to_words.items():
        score_for_word = 0
        for word in words:
            score_for_word += score_word(word)
            player_to_points[player] = score_for_word
    return player_to_points
print(players_score())




#make your letter_to_points dictionary able to handle lowercase inputs as well

