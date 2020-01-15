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

		self.vertex_distance = 20
		vertex_angle = 32
		forward_bend = 8

		self.v_angle1 = -vertex_angle + forward_bend
		self.v_angle2 = vertex_angle - forward_bend
		self.v_angle3 = 180 - vertex_angle
		self.v_angle4 = 180 + vertex_angle

		self.vertices_polar = []

		self.vertices_cartesian = []

		self.color = color
		self.tire_width = 10
		self.tire_height = 26

		self.collider_lines = []


	def handle_collision(self):
		self.x = self.old_x
		self.y = self.old_y
		self.speed = 0

	
	def update_vertices(self):
		# Vertices in Polar Coordinates for easier rotation 
		self.vertices_polar = [
			(self.v_angle1 + self.hdg, self.vertex_distance),
			(self.v_angle2 + self.hdg, self.vertex_distance),
			(self.v_angle3 + self.hdg, self.vertex_distance),
			(self.v_angle4 + self.hdg, self.vertex_distance)
		]

		self.vertices_cartesian = []

		# Conversion of Polar Coordinates to Cartesian Coordinates for rendering
		for vertex in self.vertices_polar:
			x = cos(radians(vertex[0])) * vertex[1] + self.x
			y = sin(radians(vertex[0])) * vertex[1] + self.y
			self.vertices_cartesian.append((x, y))


	def update_colliders(self):
		v = self.vertices_cartesian
		self.collider_lines = []
		
		for i in range(len(v)):
			if i == len(v) - 1:
				point1 = (v[i][0], v[i][1])
				point2 = (v[0][0], v[0][1])
			else:
				point1 = (v[i][0], v[i][1])
				point2 = (v[i+1][0], v[i+1][1])

			line = (point1, point2)
			self.collider_lines.append(line)


	def rotate(self, angle):
		self.hdg += angle


	def update(self):
		self.old_x = self.x
		self.old_y = self.y
		self.old_hdg = self.hdg

		self.x_vel = cos(radians(self.hdg)) * self.speed
		self.y_vel = sin(radians(self.hdg)) * self.speed

		self.x += self.x_vel
		self.y += self.y_vel

		self.update_vertices()
		self.update_colliders()


	def render(self, window):
		# Render Car
		pygame.draw.polygon(window, self.color, self.vertices_cartesian)

		# Render car tires
		tire_radius = self.vertex_distance * 0.2
		for vertex in self.vertices_cartesian:
			pygame.draw.ellipse(window, (0, 0, 0), (vertex[0]-tire_radius, vertex[1]-tire_radius, tire_radius * 2, tire_radius * 2))