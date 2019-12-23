# Import modules
from math import cos, sin, radians, sqrt
import pygame
pygame.init()

# Import classes
from car import Car


class PyRacers:
	def __init__(self, width, height):
		version = "v0.1alpha2"

		self.width = width
		self.height = height
		self.win = pygame.display.set_mode((width, height))
		pygame.display.set_caption("PyRacers " + version)
		self.win_rect = pygame.Rect(0, 0, width, height)

		icon = pygame.image.load("icon.png")
		pygame.display.set_icon(icon)

		self.clock = pygame.time.Clock()
		self.running = True
		self.FPS = 60
		self.background = (200, 200, 200)









	def start(self):
		self.p1 = Car(self.width / 2, self.height / 2 - 100, (255, 0, 0))
		self.p2 = Car(self.width / 2, self.height / 2 + 100, (0, 0, 255))

		self.friction = 0.975


	def input(self, keys):
		rotate_speed = 3.4
		acceleration = 0.6
		brake_power = 0.917

		# Player 1 Controls
		if keys[pygame.K_a]:
			self.p1.rotate(-rotate_speed)
		if keys[pygame.K_d]:
			self.p1.rotate(rotate_speed)
		
		if keys[pygame.K_w]:
			self.p1.speed += acceleration
		if keys[pygame.K_s]:
			self.p1.speed *= brake_power

		# Player 2 Controls
		if keys[pygame.K_LEFT]:
			self.p2.rotate(-rotate_speed)
		if keys[pygame.K_RIGHT]:
			self.p2.rotate(rotate_speed)
		
		if keys[pygame.K_UP]:
			self.p2.speed += acceleration
		if keys[pygame.K_DOWN]:
			self.p2.speed *= brake_power


	def logic(self):
		# Handle collision between cars and walls
		for vertex in self.p1.vertices_cartesian:
			if not self.win_rect.collidepoint(vertex[0], vertex[1]):
				self.p1.x = self.p1.old_x
				self.p1.y = self.p1.old_y
				self.p1.speed = 0

		for vertex in self.p2.vertices_cartesian:
			if not self.win_rect.collidepoint(vertex[0], vertex[1]):
				self.p2.x = self.p2.old_x
				self.p2.y = self.p2.old_y
				self.p2.speed = 0

		# Handle collision between cars
		mult = 0.7
		if self.collide_circle(self.p1.x, self.p1.y, self.p1.vertex_distance*mult, self.p2.x, self.p2.y, self.p2.vertex_distance*mult):
			self.p1.x = self.p1.old_x
			self.p1.y = self.p1.old_y
			self.p1.speed = 0

			self.p2.x = self.p2.old_x
			self.p2.y = self.p2.old_y
			self.p2.speed = 0

		# Apply Friction to Cars
		self.p1.speed *= self.friction
		self.p2.speed *= self.friction

		# Update Car variables
		self.p1.update()
		self.p2.update()


	def render(self, window):
		self.win.fill(self.background)

		self.p1.render(window)
		self.p2.render(window)

		pygame.display.update()

	







	# ################################
	# ###### GAMEPLAY FUNCTIONS ######
	# ################################

	@staticmethod
	def dist(x1, y1, x2, y2):
		"""Returns the distance between two points using the Pythagorean Theorem.
		a^2 + b^2 = c^2
		
		Arguments:
			x1 {int} -- x coordinate of first point
			y1 {int} -- x coordinate of first point
			x2 {int} -- x coordinate of second point
			y2 {int} -- y coordinate of second point

		Returns:
			int -- Distance between the points.
		"""

		a = x1 - x2
		b = y1 - y2
		c = sqrt((a**2) + (b**2))
		return c

	@staticmethod
	def collide_circle(x1, y1, r1, x2, y2, r2):
		"""Finds out whether two circle are colliding or not.
		
		Arguments:
			x1 {int} -- x coordinate of center of first circle
			y1 {int} -- y coordinate of center of first circle
			r1 {int} -- radius of first circle
			x2 {int} -- x coordinate of center of second circle
			y2 {int} -- y coordinate of center of second circle
			r2 {int} -- radius of second circle
		
		Returns:
			bool -- Whether the circles are colliding or not.
		"""

		d = PyRacers.dist(x1, y1, x2, y2)

		if d <= r1 + r2:
			return True









def main():
	game = PyRacers(1024, 720)
	game.start()

	while game.running:
		game.clock.tick(game.FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.running = False

		game.input(pygame.key.get_pressed())
		game.logic()
		game.render(game.win)
		
		
if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
