import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_vectors = [
            self.velocity.rotate(angle),
            self.velocity.rotate(-angle)
        ]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroids = [
            Asteroid(self.position.x, self.position.y, new_radius),
            Asteroid(self.position.x, self.position.y, new_radius)
        ]
        for asteroid, vector in zip(new_asteroids, new_vectors):
            asteroid.velocity = vector * 1.2
