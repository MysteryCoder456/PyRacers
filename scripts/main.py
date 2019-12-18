# Import modules
from math import cos, sin, radians
import pygame
pygame.init()

# Import classes
from car import Car


class PyRacers:
	def __init__(self, width, height):
		version = "v0.1alpha1"

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
		self.p1 = Car(self.width / 2, self.height / 2, (255, 0, 0))

		self.friction = 0.97


	def input(self, keys):
		rotate_speed = 3.4
		acceleration = 0.6
		brake_power = 0.917

		if keys[pygame.K_LEFT]:
			self.p1.rotate(-rotate_speed)
		if keys[pygame.K_RIGHT]:
			self.p1.rotate(rotate_speed)
		
		if keys[pygame.K_UP]:
			self.p1.speed += acceleration
		if keys[pygame.K_DOWN]:
			self.p1.speed *= brake_power


	def logic(self):
		# Handle collision between cars and walls
		for vertex in self.p1.vertices_cartesian:
			if not self.win_rect.collidepoint(vertex[0], vertex[1]):
				self.p1.x = self.p1.old_x
				self.p1.y = self.p1.old_y
				self.p1.speed = 0

		# Apply Friction to Cars
		self.p1.speed *= self.friction

		# Update Car variables
		self.p1.update()


	def render(self, window):
		self.win.fill(self.background)

		self.p1.render(window)

		pygame.display.update()






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
