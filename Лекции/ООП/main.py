class Player:
    def __int__(self, name, battle_cry='Geronimo!'):
        self.hp = 100

        self.name = name
        self.battle_cry = battle_cry

    def shout_battle_cry(self):
        print(self.battle_cry)

    def kick(self, p, f):
        # ... some logic
        p.hp -= f
        # ... some logic

class HealerPlayer:
    def __int__(self, name, battle_cry='Geronimo!'):

        self.hp = 100
        self.heal_point = 20
        self.name = name
        self.battle_cry = battle_cry

    def shout_battle_cry(self):
        print(self.battle_cry)

    def kick(selfs, p, f):
        # ... some logic
        p.hp -= f
        # ... some logic

    def heal(self, x):
        if x <= self.heal_point:
            self.hp += x
            self.heal_point -= x
