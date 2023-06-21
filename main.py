import player as p
import game as g

if __name__ == "__main__":
    print("\n\n\n\n\n")
    print("♣ ♦ Welcome to chiplessPoker! ♥ ♠\n")
    numPlayers = int(input("Enter the number of players: "))
    players = []
    startingAmount = int(input("Enter the number of chips each player starts with: "))
    
    print()
    
    for name in range(numPlayers):
        name = input("Enter name of player: ")
        player = p.Player(name, startingAmount)
        players.append(player)
        
    mainGame = g.Game(numPlayers, players)
    mainGame.playGame()