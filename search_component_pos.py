#MenuTitle: Search component position from selected glyphs
# -*- coding: utf-8 -*-
__doc__="""
Glyphs script for searching component position from selected glyphs
"""
# Author : Yun Hyunjin
# Date : 2019/01/15

componentSearch = '_part.LC_Giyeok1'
if len(Glyphs.font.selectedLayers) <= 1:
	for glyph in Glyphs.font.glyphs:
		for layer in glyph.layers:
			for component in layer.components:
				if component.componentName == componentSearch:
					print 'Glyph:%s, X:%.1f, Y:%.1f' % (layer.parent.name, component.position.x, component.position.y)
else:
	for layer in Glyphs.font.selectedLayers:
		for component in layer.components:
			if component.componentName == componentSearch:
				print 'Glyph:%s, X:%.1f, Y:%.1f' % (layer.parent.name, component.position.x, component.position.y)
