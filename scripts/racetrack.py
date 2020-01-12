import pygame


class RaceTrack:
    def __init__(self, inner_points, outer_points):
        self.inner_points = inner_points
        self.outer_points = outer_points
        self.color = (0, 0, 0)

    def render(self, window, background):
        pygame.draw.polygon(window, self.color, self.outer_points)
        pygame.draw.polygon(window, background, self.inner_points)