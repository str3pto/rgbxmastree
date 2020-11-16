from tree import RGBXmasTree
from colorzero import Color, Hue
import random
import time
from time import sleep
import cherrypy

tree = RGBXmasTree()

tree.brightness = 0.1



class Xmas_Tree(object):
	@cherrypy.expose
	def index(self):
		return """<html>
			<head></head>
			<body>
			<form method="get" action="RGBXhue">
			  <label for="RGBXmashue">HUE:</label><br>
			  <input type="text" value="red" name="RGBXmashue" />
			  <button type="submit">GO HUE</button>
			</form>
			<form method="get" action="generate">
			  <input type="text" value="8" name="length" />
			  <button type="submit">Give it now!</button>
			</form>
			<form method="get" action="generate">
			  <input type="text" value="8" name="length" />
			  <button type="submit">Give it now!</button>
			</form>
		  </body>
		</html>"""

	@cherrypy.expose
	def RGBXhue(RGBXmashue):
		timeout = 150
		timeout_start = time.time()
		tree.brightness = 0.1

		tree.color = Color(RGBXmashue)

		while time.time() < timeout_start + timeout:
				tree.color += Hue(deg=1)
		"""except KeyboardInterrupt:
			tree.brightness = 0.0
			tree.close()"""

	@cherrypy.expose
	# starts one by one
	def OneByOne():
		timeout_start = time.time()
		tree.brightness = 0.1
		colors = [Color('red'), Color('green'), Color('blue')]  # add more if you like

		try:
			while time.time() < timeout_start + timeout:
				for color in colors:
					for pixel in tree:
						pixel.color = color
		except KeyboardInterrupt:
			tree.brightness = 0.0
			tree.close()


	# starts randomsparkles
	@cherrypy.expose
	def random_lights():
		timeout_start = time.time()
		tree.brightness = 0.1

		def random_color():
			r = random.random()
			g = random.random()
			b = random.random()
			return (r, g, b)

		try:
			while time.time() < timeout_start + timeout:
				pixel = random.choice(tree)
				pixel.color = random_color()
		except KeyboardInterrupt:
			tree.brightness = 0.0
			tree.close()

	@cherrypy.expose
	# starts rgb
	def RuBeGe():
		timeout_start = time.time()
		tree.brightness = 0.1
		colors = [Color('red'), Color('green'), Color('blue')]  # add more if you like

		try:
			while time.time() < timeout_start + 10:
				for color in colors:
					tree.color = color
					sleep(1)
		except KeyboardInterrupt:
			tree.brightness = 0.0
			tree.close()

if __name__ == '__main__':
	cherrypy.quickstart(Xmas_Tree)