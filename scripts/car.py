import pygame
from math import cos, sin, radians

class Car:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.old_x = x
		self.old_y = y

		self.x_vel = 0
		self.y_vel = 0
		self.hdg = 0
		self.speed = 0

		self.vertex_distance = 35
		vertex_angle = 32
		forward_bend = 8

		self.v_angle1 = -vertex_angle + forward_bend
		self.v_angle2 = vertex_angle - forward_bend
		self.v_angle3 = 180 - vertex_angle
		self.v_angle4 = 180 + vertex_angle

		# Vertices in Polar Coordinate format for easier rotation 
		self.vertices_polar = [
			(self.v_angle1 + self.hdg, self.vertex_distance),
			(self.v_angle2 + self.hdg, self.vertex_distance),
			(self.v_angle3 + self.hdg, self.vertex_distance),
			(self.v_angle4 + self.hdg, self.vertex_distance)
		]

		self.vertices_cartesian = []

		self.color = color
		self.tire_width = 10
		self.tire_height = 26

	def rotate(self, angle):
		self.hdg += angle

	def update(self):
		self.old_x = self.x
		self.old_y = self.y

		self.x_vel = cos(radians(self.hdg)) * self.speed
		self.y_vel = sin(radians(self.hdg)) * self.speed

		self.x += self.x_vel
		self.y += self.y_vel

		# Vertices in Polar Coordinate format for easier rotation 
		self.vertices_polar = (
			(self.v_angle1 + self.hdg, self.vertex_distance),
			(self.v_angle2 + self.hdg, self.vertex_distance),
			(self.v_angle3 + self.hdg, self.vertex_distance),
			(self.v_angle4 + self.hdg, self.vertex_distance)
		)

		self.vertices_cartesian = []

		# Conversion of Polar Coordinates to Cartesian Coordinates for rendering
		for vertex in self.vertices_polar:
			x = cos(radians(vertex[0])) * vertex[1] + self.x
			y = sin(radians(vertex[0])) * vertex[1] + self.y
			self.vertices_cartesian.append((x, y))

	def render(self, window):
		# Render Car
		pygame.draw.polygon(window, self.color, self.vertices_cartesian)

		# Render car tires
		tire_radius = self.vertex_distance * 0.2
		for vertex in self.vertices_cartesian:
			pygame.draw.ellipse(window, (0, 0, 0), (vertex[0]-tire_radius, vertex[1]-tire_radius, tire_radius * 2, tire_radius * 2))