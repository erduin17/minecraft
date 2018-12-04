# Make sure to keep up on the slime anime it is super good! -noah
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

air = 0
flower = 38

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  
zz = z + 1

mc.setBlocks(-100,-100, -100, 100, 100, 100, block.AIR.id)
mc.setBlocks(-200,-200, -200, 200, 200, 200, block.AIR.id)

mc.setBlocks(0,0, 0, 50, 0, 50, block.GLOWSTONE_BLOCK.id)
mc.setBlocks(0,5, 0, 50, 5, 50, block.GLOWSTONE_BLOCK.id)
mc.setBlocks(0,10, 0, 50, 10, 50, block.GLOWSTONE_BLOCK.id)
mc.setBlocks(0,15, 0, 50, 15, 50, block.GLOWSTONE_BLOCK.id)
mc.setBlocks(0,20, 0, 50, 20, 50, block.GLOWSTONE_BLOCK.id)


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

mc.player.setPos(25, 25,25 )


while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y-1, z, block.AIR.id)
    sleep(0.65)		

	
	

#API Blocks
#====================
#	AIR                   0
#	STONE                 1
#	GRASS                 2
#	DIRT                  3
#	COBBLESTONE           4
#	WOOD_PLANKS           5
#	SAPLING               6
#	BEDROCK               7
#	WATER_FLOWING         8
#	WATER                 8
#	WATER_STATIONARY      9
#	LAVA_FLOWING         10
#	LAVA                 10
#	LAVA_STATIONARY      11
#	SAND                 12
#	GRAVEL               13
#	GOLD_ORE             14
#	IRON_ORE             15
#	COAL_ORE             16
#	WOOD                 17
#	LEAVES               18
#	GLASS                20
#	LAPIS_LAZULI_ORE     21
#	LAPIS_LAZULI_BLOCK   22
#	SANDSTONE            24
#	BED                  26
#	COBWEB               30
#	GRASS_TALL           31
#	WOOL                 35
#	FLOWER_YELLOW        37
#	FLOWER_CYAN          38
#	MUSHROOM_BROWN       39
#	MUSHROOM_RED         40
#	GOLD_BLOCK           41
#	IRON_BLOCK           42
#	STONE_SLAB_DOUBLE    43
#	STONE_SLAB           44
#	BRICK_BLOCK          45
#	TNT                  46
#	BOOKSHELF            47
#	MOSS_STONE           48
#	OBSIDIAN             49
#	TORCH                50
#	FIRE                 51
#	STAIRS_WOOD          53
#	CHEST                54
#	DIAMOND_ORE          56
#	DIAMOND_BLOCK        57
#	CRAFTING_TABLE       58
#	FARMLAND             60
#	FURNACE_INACTIVE     61
#	FURNACE_ACTIVE       62
#	DOOR_WOOD            64
#	LADDER               65
#	STAIRS_COBBLESTONE   67
#	DOOR_IRON            71
#	REDSTONE_ORE         73
#	SNOW                 78
#	ICE                  79
#	SNOW_BLOCK           80
#	CACTUS               81
#	CLAY                 82
#	SUGAR_CANE           83
#	FENCE                85
#	GLOWSTONE_BLOCK      89
#	BEDROCK_INVISIBLE    95
#	STONE_BRICK          98
#	GLASS_PANE          102
#	MELON               103
#	FENCE_GATE          107
#	GLOWING_OBSIDIAN    246
#	NETHER_REACTOR_CORE 247

