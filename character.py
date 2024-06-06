

class Character:
    def __init__(self,name, level, strength, intelligence, magic, endurance, agility, luck):
        self.name = name
        self.level = level
        self.strength = strength
        self.intelligence = intelligence
        self.magic = magic
        self.endurance = endurance
        self.agility = agility
        self.luck = luck

        self.maxHP = self.SetMaxHP()
        self.HP = self.maxHP

        self.maxMP = self.SetMaxMP()
        self.MP = self.maxMP

        self.physicalAtt = self.SetPhysicalAttack()
        self.magicAtt = self.SetMagicAttack()

        self.physicalAcc = self.SetPhysicalAccuracy()
        self.magicAcc = self.SetMagicAccuracy()

        self.physicalDef = self.SetPhysicalDefense()
        #self.magicDef = pass #may not be needed at all

        self.evasion = self.SetEvasion()
        self.ailmentRecovery = self.SetAilmentRecovery()

        self.critical = self.SetCritical()
        self.rareDrop = self.SetRareDrop()
        self.initiative = self.SetInitiative()

    def SetMaxHP(self):
        self.maxHP = int(((self.level+self.endurance) * 6 + self.strength) * (self.luck * 0.01 + 1))

    def SetPhysicalAttack(self):#don't forget equipment
        self.physicalAtt = int(((self.strength*2) + self.level + self.endurance) * (self.luck * 0.01 + 1))

    def SetMagicAttack(self):
        self.magicAtt = int(((self.magic * 2) + self.level + self.intelligence) * (self.luck * 0.01 + 1))

    def SetPhysicalAccuracy(self):
        self.physicalAcc = int(((self.level / 2) + self.agility) * (self.luck * 0.01 + 1))

    def SetMagicAccuracy(self):
        self.magicAcc = int(((self.level / 2) + self.intelligence) * (self.luck * 0.01 + 1))

    def SetPhysicalDefense(self):
        self.physicalDef = int((((self.strength + level) / 2) + self.endurance) * 2 * (self.luck * 0.01 + 1))

    def SetEvasion(self):
        self.evasion = int(((self.level/2) + self.agility) * (self.luck * 0.01 + 1))
    
    def SetAilmentRecovery(self):
        self.ailmentRecovery = int((self.intelligence + self.endurance)/2 + (self.luck/2))

    def SetCritical(self):
        self.critical = 0.05 + (self.luck * 0.1)
    
    def SetRareDrop(self):
        self.rareDrop = 0.01 + (self.luck * 0.01)

    def SetInitiative(self):
        self.initiative = int((self.agility + self.level) / 2)
    