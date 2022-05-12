# encoding: utf-8

###########################################################################################################
#
#
#	General Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class MergeLayer(FilterWithoutDialog):

	def processGlyph_withArguments_(self, glyph, arguments):
		print("__arguments", arguments)

		try:
			sourceMasterName = arguments[1]
			targetMasterName = arguments[2] # instance.customParameters["MergeLayer"]
			font = glyph.parent
			sourceMaster = font.fontMasterForName_(sourceMasterName)
			targetMaster = font.fontMasterForName_(targetMasterName)
			if not sourceMaster or not targetMaster:
				print("!master")
				return
			sourceLayer = glyph.layers[sourceMaster.id]
			if len(sourceLayer.shapes) == 0:
				return
			targetLayer = glyph.layers[targetMaster.id]
			targetLayer.removeOverlap()

			for copyShape in sourceLayer.shapes:
				copyShape = copyShape.copy()
				copyShape.reverse()
				targetLayer.shapes.append(copyShape)
			print("done")
		except Exception as e:
			import traceback
			print(traceback.format_exc())

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	