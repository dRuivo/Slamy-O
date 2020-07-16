   
# import os
from math import cos, sin, pi, floor
#import pygame
from adafruit_rplidar import RPLidar
    
x_size = 6 * 320
y_size = 5 * 240
scale = int(min([x_size, y_size]) / 2) - 1

#pygame.init()
#window = pygame.display.set_mode((x_size,y_size))
#pygame.mouse.set_visible(False)
#window.fill((0,0,0))
#pygame.display.update()
    
# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)
    
# used to scale data to fit on the screen
max_distance = 0
    
#pylint: disable=redefined-outer-name,global-statement
def process_data(data):
    global max_distance
    window.fill((0,0,0))
    for angle in range(360):
        distance = data[angle]
        if distance > 0:                  # ignore initially ungathered data points
            max_distance = max([min([5000, distance]), max_distance])
            radians = angle * pi / 180.0
            x = distance * cos(radians)
            y = distance * sin(radians)
            point = (int(x_size / 2) + int(x / max_distance * scale), 
            int(y_size / 2) + int(y / max_distance * scale))
            #window.set_at(point, pygame.Color(255, 255, 255))
            #pygame.draw.line(window, pygame.Color(255, 255, 255), (int(x_size / 2), int(y_size / 2)), point)
    #pygame.display.update()
    
    
scan_data = [0]*360
    
try:
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        #process_data(scan_data)
        print(scan_data)
    
except KeyboardInterrupt:
    print('Stoping.')
lidar.stop()
lidar.disconnect()