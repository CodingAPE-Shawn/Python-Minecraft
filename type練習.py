from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a = int(input("Block ID??"))
x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,a)
