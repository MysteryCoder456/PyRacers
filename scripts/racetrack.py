import pygame


class RaceTrack:
    def __init__(self, inner_points, outer_points):
        self.inner_points = inner_points
        self.outer_points = outer_points
        self.color = (70, 70, 70)

        # Calculate inner collider lines
        self.inner_collider_lines = []
        
        for i in range(len(inner_points)):
            if i == len(inner_points) - 1:
                x1 = inner_points[i][0]
                y1 = inner_points[i][1]

                x2 = inner_points[0][0]
                y2 = inner_points[0][1]
            else:
                x1 = inner_points[i][0]
                y1 = inner_points[i][1]

                x2 = inner_points[i+1][0]
                y2 = inner_points[i+1][1]

            point1 = (x1, y1)
            point2 = (x2, y2)
            self.inner_collider_lines.append((point1, point2))

        # Calculate outer collider lines
        self.outer_collider_lines = []

        for j in range(len(outer_points)):
            if j == len(outer_points) - 1:
                x1 = outer_points[j][0]
                y1 = outer_points[j][1]

                x2 = outer_points[0][0]
                y2 = outer_points[0][1]
            else:
                x1 = outer_points[j][0]
                y1 = outer_points[j][1]

                x2 = outer_points[j+1][0]
                y2 = outer_points[j+1][1]

            point1 = (x1, y1)
            point2 = (x2, y2)
            self.outer_collider_lines.append((point1, point2))


    def render(self, window, background):
        pygame.draw.polygon(window, self.color, self.outer_points)
        pygame.draw.polygon(window, background, self.inner_points)