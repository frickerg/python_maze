#################
# Compass Class:
# Bei dieser Klasse geht es darum, einen Wert für die verschiedenen Richtungen zu setzen, und dazu sagen können, auf welcher Position sich dieser Wert befindet.
# Die klasse muss nicht umbedingt Compass heissen ;-)
#
# Beispiel: compass.setNorth(1, (x, y)) // hier sagen wir, dass sich auf dem Tupel der position (x, y) der Wert vom Typ '1' befindet
#################
class Compass():
    pass

def set_North(Compass):
    print(Compass.Wert + " ")

def set_West(Compass):
    print(Compass.Wert + " ")

def set_South(Compass):
    print(Compass.Wert + " ")

def set_Ost(Compass):
    print(Compass.Wert + " ")

North = Compass()
North.Wert = 1

West = Compass()
West.Wert = 2

South = Compass()
South.Wert = 3

Ost = Compass()
Ost.Wert = 4

