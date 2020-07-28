# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:54:51 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,["營隊規矩","注意:拍手","木頭人:舉手"])