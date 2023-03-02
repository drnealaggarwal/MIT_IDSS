class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
        return 'done'
        
player1 = PlayerCharacter('dna', 62)
player2 = PlayerCharacter('ami', 45)
player2.attack = 50

print(player1.membership)
