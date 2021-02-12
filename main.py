from GUI import StartGui, UserGui
from Level1 import Level1

StartGui.run_gui()
player = UserGui.create_player()

level1 = Level1()
level1.start(player)
