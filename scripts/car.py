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

		self.v_angle1 = -vertex_angle
		self.v_angle2 = vertex_angle
		self.v_angle3 = 180 - vertex_angle
		self.v_angle4 = 180 + vertex_angle

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

		# TODO: Simplify this code
		# Conversion of Polar Coordinates to Cartesian Coordinates for rendering
		x1 = cos(radians(self.vertices_polar[0][0])) * self.vertices_polar[0][1] + self.x
		y1 = sin(radians(self.vertices_polar[0][0])) * self.vertices_polar[0][1] + self.y

		x2 = cos(radians(self.vertices_polar[1][0])) * self.vertices_polar[1][1] + self.x
		y2 = sin(radians(self.vertices_polar[1][0])) * self.vertices_polar[1][1] + self.y

		x3 = cos(radians(self.vertices_polar[2][0])) * self.vertices_polar[2][1] + self.x
		y3 = sin(radians(self.vertices_polar[2][0])) * self.vertices_polar[2][1] + self.y

		x4 = cos(radians(self.vertices_polar[3][0])) * self.vertices_polar[3][1] + self.x
		y4 = sin(radians(self.vertices_polar[3][0])) * self.vertices_polar[3][1] + self.y

		self.vertices_cartesian = [
			(x1, y1),
			(x2, y2),
			(x3, y3),
			(x4, y4)
		]

	def render(self, window):
		# TODO: Render car tires

		# Render Car
		pygame.draw.polygon(window, self.color, self.vertices_cartesian)