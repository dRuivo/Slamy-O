import numpy as np
import matplotlib.pyplot as plt
from environment import Environment

class Ray:
    def __init__(self, pos, theta=0):
        self.pos = pos
        self.dir = [np.cos(theta), np.sin(theta)]

    def update_dir(self, theta):
        self.dir = [np.cos(theta), np.sin(theta)]

    def update_pos(self, pos):
        self.pos = pos

    def get_hit(self, p1, p2):
        den = (-self.dir[0]) * (p1[1] - p2[1]) - (-self.dir[1]) * (p1[0] - p2[0])
        
        if np.abs(den) > 0:
            t = ((self.pos[0] - p1[0]) * (p1[1] - p2[1]) - (self.pos[1] - p1[1]) * (p1[0] - p2[0])) / den
            d = -((-self.dir[0]) * (self.pos[1] - p1[1]) - (-self.dir[1]) * (self.pos[0] - p1[0])) / den

            if 0 <= d <= 1 and t > 0:
                hit = [self.pos[0] + t * self.dir[0],
                       self.pos[1] + t * self.dir[1]]
                return hit, t
        return None

    def draw(self, ray_end = None):
        plt.plot(self.pos[0],
                self.pos[1],
                'og')

        plt.plot([self.pos[0], self.pos[0] + self.dir[0]],
                [self.pos[1], self.pos[1] + self.dir[1]],
                'g')


class Lidar2D:
    def __init__(self, env:Environment, init_pos, init_heading, points_per_turn = 360):
        self.env = env
        self.pos = init_pos
        self.theta = init_heading
        self.ray = Ray(self.pos)
        self.points_per_turn = points_per_turn

    def update_pose(self, pose):
        self.pos = pose[0:1]
        self.theta = pose[2]
        self.ray.update_pos(self.pos)

    def get_frame(self):
        hits = []
        for t in np.arange(0., 2*np.pi, 2*np.pi/self.points_per_turn):
            best_hit = [t, np.inf]
            self.ray.update_dir(t + self.theta)
            for b in self.env.bounds:
                res = self.ray.get_hit(b.p1, b.p2)
                if res:
                    dist = res[1]
                    if best_hit[1] > dist:
                        best_hit[1] = dist 
            hits.append(best_hit)
        return hits

    def draw(self, hits):
        plt.plot(self.pos[0], self.pos[1], 'og')
        print(len(hits))
        for hit in hits:
            plt.plot(self.pos[0] + hit[1] * np.cos(hit[0]), 
                     self.pos[1] + hit[1] * np.sin(hit[0]), 
                     'ob')


    
