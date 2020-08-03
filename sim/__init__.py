import numpy as np
import matplotlib.pyplot as plt
import time
from sensing import Ray, Lidar2D
from environment import Boundry, Environment, procedural_environment

env = procedural_environment()

env.draw()
lidar = Lidar2D(env, [6000, 5000], 0)
start_time = time.time()
hits = lidar.get_frame()
print(time.time()- start_time)
lidar.draw(hits)
env.show()




