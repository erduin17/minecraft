# Base project format.
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create()
    x, y, z = mc.player.getPos()
    return mc
    

def clear_with_air(mc, x, y, z,h,k,l):
    mc.setBlocks(-100,-100, -100, 100, 100, 100, block.AIR.id)
    mc.setBlocks(-200,-200, -200, 200, 200, 200, block.AIR.id)

def board(mc):
    mc.setBlocks(-100,-100, -100, 100, 100, 100, block.AIR.id)
    mc.setBlocks(-200,-200, -200, 200, 200, 200, block.AIR.id)

    mc.setBlocks(0,0, 0, 50, 0, 50, block.GLOWSTONE_BLOCK.id)
    mc.setBlocks(0,5, 0, 50, 5, 50, block.GLOWSTONE_BLOCK.id)
    mc.setBlocks(0,10, 0, 50, 10, 50, block.GLOWSTONE_BLOCK.id)
    mc.setBlocks(0,15, 0, 50, 15, 50, block.GLOWSTONE_BLOCK.id)
    mc.setBlocks(0,20, 0, 50, 20, 50, block.GLOWSTONE_BLOCK.id)
    mc.player.setPos(25, 25,25 )


    mc.setBlocks(-1,1, -1, -1, 1, 50, block.GLASS.id)
    mc.setBlocks(-1,3, -1, -1, 3, 50, block.GLASS.id)
    mc.setBlocks(-1,6, -1, -1, 6, 50, block.GLASS.id)
    mc.setBlocks(-1,8, -1, -1, 8, 50, block.GLASS.id)
    mc.setBlocks(-1,11, -1, -1, 11, 50, block.GLASS.id)
    mc.setBlocks(-1,13, -1, -1, 13, 50, block.GLASS.id)
    mc.setBlocks(-1,16, -1, -1, 16, 50, block.GLASS.id)
    mc.setBlocks(-1,18, -1, -1, 18, 50, block.GLASS.id)
    mc.setBlocks(-1,21, -1, -1, 21, 50, block.GLASS.id)
    mc.setBlocks(-1,23, -1, -1, 23, 50, block.GLASS.id)

    mc.setBlocks(-1,1, -1, 51, 1, -1, block.GLASS.id)
    mc.setBlocks(-1,3, -1, 51, 3, -1, block.GLASS.id)
    mc.setBlocks(-1,6, -1, 51, 6, -1, block.GLASS.id)
    mc.setBlocks(-1,8, -1, 51, 8, -1, block.GLASS.id)
    mc.setBlocks(-1,11, -1, 51, 11, -1, block.GLASS.id)
    mc.setBlocks(-1,13, -1, 51, 13, -1, block.GLASS.id)
    mc.setBlocks(-1,16, -1, 51, 16, -1, block.GLASS.id)
    mc.setBlocks(-1,18, -1, 51, 18, -1, block.GLASS.id)
    mc.setBlocks(-1,21, -1, 51, 21, -1, block.GLASS.id)
    mc.setBlocks(-1,23, -1, 51, 23, -1, block.GLASS.id)

    mc.setBlocks(-1,1, 51, 51, 1, 51, block.GLASS.id)
    mc.setBlocks(-1,3, 51, 51, 3, 51, block.GLASS.id)
    mc.setBlocks(-1,6, 51, 51, 6, 51, block.GLASS.id)
    mc.setBlocks(-1,8, 51, 51, 8, 51, block.GLASS.id)
    mc.setBlocks(-1,11, 51, 51, 11, 51, block.GLASS.id)
    mc.setBlocks(-1,13, 51, 51, 13, 51, block.GLASS.id)
    mc.setBlocks(-1,16, 51, 51, 16, 51, block.GLASS.id)
    mc.setBlocks(-1,18, 51, 51, 18, 51, block.GLASS.id)
    mc.setBlocks(-1,21, 51, 51, 21, 51, block.GLASS.id)
    mc.setBlocks(-1,23, 51, 51, 23, 51, block.GLASS.id)

    mc.setBlocks(51,1, -1, 51, 1, 50, block.GLASS.id)
    mc.setBlocks(51,3, -1, 51, 3, 50, block.GLASS.id)
    mc.setBlocks(51,6, -1, 51, 6, 50, block.GLASS.id)
    mc.setBlocks(51,8, -1, 51, 8, 50, block.GLASS.id)
    mc.setBlocks(51,11, -1, 51, 11, 50, block.GLASS.id)
    mc.setBlocks(51,13, -1, 51, 13, 50, block.GLASS.id)
    mc.setBlocks(51,16, -1, 51, 16, 50, block.GLASS.id)
    mc.setBlocks(51,18, -1, 51, 18, 50, block.GLASS.id)
    mc.setBlocks(51,21, -1, 51, 21, 50, block.GLASS.id)
    mc.setBlocks(51,23, -1, 51, 23, 50, block.GLASS.id)


def main():
	mc = init()
	x, y, z = mc.player.getPos()
	board(mc)
	while True:
		x, y, z = mc.player.getPos()
		mc.setBlock(x, y-1, z, block.AIR.id)
		sleep(0.65)			

main()

	
