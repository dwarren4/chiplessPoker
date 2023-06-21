import player as p

class Game:
    pot = 0
    def __init__(self, numPlayers, players):
        self.numPlayers = numPlayers
        self.players = players
        
    def addToPot(self, betAmount):
        self.pot += betAmount
        
    def printFunction(self, betName):
        print()
        print("--------------------------------------------------")
        print("|", end="")
        print(f"{betName}".center(48), end="")
        print("|")
        print("--------------------------------------------------")
        
        for player in self.players:
            while True:
                try:
                    bet = int(input(f"Enter {player.name} bet amount: "))
                    if (bet < 0):
                        print("Bet's must be positive!")
                        continue
                    player.betChips(self, bet)
                    break
                except:
                    print("Error occured, try again.")
              
        print()  
        print ("------Pot------")
        print("|", end="")
        print(f"$ {self.pot} $".center(13), end="")
        print("|")
        print("---------------")
            
        print()
        print ("----------Chips----------")
        for player in self.players:
            print("|", end="")
            print(f"{player.name} | {player.chips}".center(23), end="")
            print("|")
        print ("-------------------------")
        print()
              
        
    def playGame(self):
        while True:
            self.printFunction("Small/big blind")
            
            self.printFunction("Preflop")
            
            self.printFunction("Flop")
            
            self.printFunction("Turn")
            
            self.printFunction("River")
            
            cont = input("\nRound over! Would you like to continue? (Y/N) ")
            if cont == "N":
                break
            
            playerInGame = True
            
            while playerInGame:
                winner = input("Who won? ")
                index = 0
                for player in self.players:
                    if player.name == winner:
                        playerInGame = False
                        break
                    index += 1
                
                if playerInGame == False:
                    break
                    
                print(f"{winner} not in game! Try again.")
                
            self.players[index].addWinnings(self.pot)
            self.pot = 0
                    
            
                
                
                
                
            
        
        
        