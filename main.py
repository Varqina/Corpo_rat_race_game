from GUI import StartGui, UserGui

StartGui.run_gui()
player = UserGui.create_player()

from Level1 import Level1

level1 = Level1()
level1.start(player)
