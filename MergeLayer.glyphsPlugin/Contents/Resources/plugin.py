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

class MergeLayer(GeneralPlugin):
	def settings(self):
		GSCallbackHandler.addCallback_forOperation_(self, "GSPrepareLayerCallback")

	def processLayer_originalGlyph_withInstance_(self, layer, glyph, instance):
		try:
			addLayerName = instance.customParameters["MergeLayer"]
			if not addLayerName:
				return
		
			font = glyph.parent
			master = font.fontMasterForName_(addLayerName)
			if not master:
				return
			layer.removeOverlap()
			addLayer = glyph.layers[master.id]
			for addPath in addLayer.paths:
				copyPath = addPath.copy()
				copyPath.reverse()
				layer.paths.append(copyPath)
			for addComp in addLayer.components:
				copyComp = addComp.copy()
				copyComp.reverse()
				layer.components.append(copyComp)
		except Exception as e:
			import traceback
			print traceback.format_exc()

	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	