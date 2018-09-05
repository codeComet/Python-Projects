letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
  points_total = 0
  for item in word:
    if item in letters:
      points_total += letter_to_points[item]
    else:
      points_total += 0
  return points_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_word = {
  "player1":	["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH", "EYES", "MACHINE"], 
  "Lexi con": ["ERASER", "BELLY", "HUSKY"], 
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}
for key, value in player_to_word.items():
  print(key, value)
  player_points = 0
  for word in value:
    player_points += score_word(word)
  print(key+"'s scores: "+ str(player_points))
    
  









