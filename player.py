import game as g

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        
    def betChips(self, game, betAmount):
        self.chips -= betAmount
        game.addToPot(betAmount)
        
    def addWinnings(self, amount):
        self.chips += amount
        
        