attempts = 3
score = 0
gboard = [[0, 1], [0, 1]]

for gattempt in range(attempts): #goes though the loop 3(attempts=3) times
  if(attempts!=0):
    print("Enter positions: [row, column]")
    row = int(input())
    col = int(input())
    position = gboard[row][col]

    if(position == 0):
      attempts -= 1
      print("Ouch! It's a bomb! You have {0} attempts".format(attempts))
      #instead of writing "You have ", attempts, "attempts"
    else:
      score+=1
      print("Woohoo! You found a gold! Your score is ", score)
  else:
    print("You Lose! You have {0} attempts and your score is {1}".format(attempts, score))

if(score == 2):
    print("You win!")
else:
  print("You didn't collect enough gold!")





