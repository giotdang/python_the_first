class bowlingGames:
    def __init__(self):
        self.rollList=[]    #Value of roll
        self.frameNum=0     #Number of frame
        self.rollNum=0      #Number of roll
        self.bonusRoll=0    #Number of bonus roll after frame 10
    def rolls(self,pinsFall):
        if(pinsFall<=10):
            self.rollList.append(pinsFall)
        # When number of frame is less than 10, increase number of frame by 1
        # after 1 roll if it is a strike roll, after 2 rolls if it is a spare or a normal roll
        # When number of frame reaches 10, stop increasing number of frame 
        # and calculate number of bonus rolls in a case of strike or spare 
        if self.frameNum<10:
            if pinsFall==10:
                self.frameNum+=1
                self.rollNum+=1
            elif len(self.rollList)>1 and pinsFall<10:
                if self.rollNum<=(len(self.rollList)-2) and self.rollList[len(self.rollList)-1]<10:
                    self.frameNum+=1
                    self.rollNum+=2
        else:
            self.rollNum+=1
            self.bonusRoll+=1
    # The game is valid when every frame is completed.
    # Completed frames require 2 rolls if they are spare or normal rolls
    # and requires 1 rolls if they are strike rolls 
    def isGameValid(self):
        return(len(self.rollList)==self.rollNum)  
    # Check if a roll is spare or not
    def isSpare(self,turn):
        if turn<=(len(self.rollList)-3):
            return (self.rollList[turn]+self.rollList[turn+1]==10)
        else:
            return False
    # Check if a roll is strike or not
    def isStrike(self,turn):
        if turn<=(len(self.rollList)-3):
            return (self.rollList[turn]==10)
        else:
            return False
    # Check if a roll is normal or not
    def isNormal(self,turn):
        if turn<=(len(self.rollList)-2):
            return (self.rollList[turn]+self.rollList[turn+1]<10)
        else:
            return False
    @property
    # Return score of a game
    def score(self):
        # Calculate game score only if the game is valid
        if self.isGameValid():
            result=0
            turn=0
            for frames in range(self.frameNum):
                # Frame 10 is a special frame because 3 rolls is available 
                # if player perform a strike or a spare in this frame. Check number
                # of bonus rolls to justify validity of frame 10.
                # IF Strike: 2 bonus rolls
                #    Spare:  1 bonus roll
                #    Normal: 0 bonus roll
                if frames==9:
                    if self.isSpare(turn) and self.bonusRoll>1:
                        return "Invalid roll at frame 10. Only 1 more roll for spare"
                    elif self.isStrike(turn) and self.bonusRoll>2:
                        return "Invalid roll at frame 10. Only 2 more rolls for strike"
                    elif self.isNormal(turn) and self.bonusRoll>0:
                        return "Invalid roll at frame 10. No strike or spare"
                # Calculate score after a strike
                if self.isStrike(turn):
                    result+=self.rollList[turn]+self.rollList[turn+1]+self.rollList[turn+2]
                    turn+=1
                # Calculate score after a spare
                elif self.isSpare(turn):
                    result+=self.rollList[turn]+self.rollList[turn+1]+self.rollList[turn+2]
                    turn+=2
                # Calculate score after a normal roll
                elif self.isNormal(turn):
                    result+=self.rollList[turn]+self.rollList[turn+1]
                    turn+=2
                else:
                    return f"Your data is not valid at frame {frames+1}"
            return result
        else:
            return "Your game is not valid. Lack of rolls"
            










    

