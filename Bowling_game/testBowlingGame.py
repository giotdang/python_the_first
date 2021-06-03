from bowlingGame import bowlingGames
'''
The game consists of 10 frames as shown above. In each frame the
player has two opportunities to knock down 10 pins. The score for the
frame is the total number of pins knocked down, plus bonuses for strikes
and spares.
A spare is when the player knocks down all 10 pins in two tries. The
bonus for that frame is the number of pins knocked down by the next
roll. So in frame 3 above, the score is 10 (the total number knocked
down) plus a bonus of 5 (the number of pins knocked down on the next
roll.)
A strike is when the player knocks down all 10 pins on his first try. The
bonus for that frame is the value of the next two balls rolled.
In the tenth frame a player who rolls a spare or strike is allowed to roll
the extra balls to complete the frame. However, no more than three balls
can be rolled in tenth frame.
Input
1,4|4,5|6,4|5,5|10|0,1|7,3|6,4|10|2,8,6|
Expected output
133
'''
game= bowlingGames()
game.rolls(1)
game.rolls(4)

game.rolls(4)
game.rolls(5)

game.rolls(6)
game.rolls(4)

game.rolls(5)
game.rolls(5)

game.rolls(10)

game.rolls(0)
game.rolls(1)

game.rolls(7)
game.rolls(3)

game.rolls(6)
game.rolls(4)

game.rolls(10)

game.rolls(2)
game.rolls(8)
game.rolls(6)

print(game.score)
