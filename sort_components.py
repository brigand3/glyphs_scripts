#MenuTitle: Sort components of selected glyphs
# -*- coding: utf-8 -*-
__doc__="""
Glyphs script for sorting component of selected glyphs
"""
# Author : Yun Hyunjin
# Date : 2019/01/23

from GlyphsApp import *
import copy

def sortComponents(components):
	for i in range(0, len(components)):
		print 'before %d - %s' % (i, components[i].componentName)

	bModified = False

	while True:
		bBreak = True		
		for i in range(0, len(components) - 1):
			if (components[i].componentName > components[i+1].componentName):
				component = copy.copy(components[i])
				del(components[i])
				components.append(component)
				bModified = True
				bBreak = False
		
		if bBreak == True:
			break
			
	if (bModified == True):
		for i in range(0, len(components)):
			print 'after %d - %s' % (i, components[i].componentName)
	
for layer in Glyphs.font.selectedLayers:
	if len(layer.components) > 0:
		print '*****************************************'
		print layer.parent
		print '*****************************************'
		sortComponents(layer.components)
