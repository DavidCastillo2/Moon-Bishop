#!/usr/bin/python
# -*- coding: UTF-8 -*-
import SideBar
import Button
import TextBox
import Slide

class Drawable(SideBar, Button, TextBox, Slide):
	def draw(self):
		pass

	def getX(self):
		pass

	def getY(self):
		pass

	def getWidth(self):
		return self.___width

	def getHeight(self):
		return self.___height

	def getVisible(self):
		pass

	def getType(self):
		pass

	def __init__(self):
		self.___float_x = None
		self.___float_y = None
		self.___width = None
		self.___height = None
		self.___boolean_visible = None
		self.___enum_Type = None
		self._unnamed_Drawable_ = None
		"""@AttributeType Drawable
		# @AssociationType Drawable"""

