#MenuTitle: Add component into selected glyphs
# -*- coding: utf-8 -*-
__doc__="""
Glyphs script for inserting component into selected glyphs
"""
# Author : Yun Hyunjin
# Date : 2019/01/04

from GlyphsApp import *

glyphInsert = Glyphs.font.glyphs['_part.LC_Giyeok1']
posToInsert = NSMakePoint(0, 0)

print 'Glpyh : %s' % glyphInsert
print 'Position  : %s\n' % posToInsert

for layer in Glyphs.font.selectedLayers:
	layer.components.append(GSComponent(glyphInsert, NSMakePoint(0, 0)))
	print '%s done.' % layer
