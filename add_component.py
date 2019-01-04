# Glyphs script for inserting component into selected glyphs

from GlyphsApp import *

glyphInsert = Glyphs.font.glyphs['_part.LC_Giyeok1']
posToInsert = NSMakePoint(0, 0)
componentNew = GSComponent(glyphInsert, NSMakePoint(0, 0))

print 'Glpyh : %s' % glyphInsert
print 'Position  : %s\n' % posToInsert

for layer in Glyphs.font.selectedLayers:
	layer.components.append(componentNew)
	print '%s done.' % layer
