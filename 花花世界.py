from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
a=mc.getBlockWithData(x,y,z)
    if a==8:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)