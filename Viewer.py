import time
import math
import pygame

from quaternion import Quaternion
from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3

# Define a main function
def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 1280
    res_y = 720

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Spawns the camera back 2 units
    scene.camera.position = Vector3(0, 0, -5)

    # Angle of the rotation and default axis
    angle = 15
    axis = Vector3(0, 1, 0)

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    # Create a test pyramid
    pyramid = Object3d("Tespyramid")
    pyramid.scale = Vector3(1, 1, 1)
    pyramid.positon = Vector3(0, 0, 0)
    pyramid.mesh = Mesh.create_pyramid(4)
    pyramid.material= Material(Color(0,0,1), "Blue World")
    scene.add_object(pyramid)

    # Game loop
    while True:
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_LEFT:
                    axis= Vector3(0, 1, 0)
                elif event.key == pygame.K_RIGHT:
                    axis= Vector3(0, -1, 0)
                elif event.key == pygame.K_UP:
                    axis= Vector3(1, 0, 0)
                elif event.key == pygame.K_DOWN:
                    axis = Vector3(-1, 0, 0)
                elif event.key == pygame.K_PAGEUP:
                    axis = Vector3(0, 0, 1)
                elif event.key == pygame.K_PAGEDOWN:
                    axis = Vector3(0, 0, -1)
                axis.normalize()

        # Clears the screen
        screen.fill((0, 0, 0))
        
        # Key press value
        keys = pygame.key.get_pressed()

        # Returns the correct rotation value
        rotation=Quaternion.AngleAxis(axis, math.radians(angle)*delta_time)

        # Handle the movement
        if keys[pygame.K_LEFT]:
            pyramid.rotation*=rotation
        if keys[pygame.K_RIGHT]:
            pyramid.rotation*=rotation
        if keys[pygame.K_UP]:
            pyramid.rotation*=rotation
        if keys[pygame.K_DOWN]:
            pyramid.rotation*=rotation
        if keys[pygame.K_PAGEUP]:
            pyramid.rotation*=rotation
        if keys[pygame.K_PAGEDOWN]:
            pyramid.rotation*=rotation

        # Get the pressed keys     
        # Up
        if keys[pygame.K_w]:
            pyramid.position = Vector3(pyramid.position.x+0.1, pyramid.position.y, pyramid.position.z)
        # Dowm
        if keys[pygame.K_s]:
            pyramid.position = Vector3(pyramid.position.x-0.1, pyramid.position.y, pyramid.position.z)
        # Right
        if keys[pygame.K_a]:
            pyramid.position = Vector3(pyramid.position.x, pyramid.position.y-0.1, pyramid.position.z)
        # Left
        if keys[pygame.K_d]:
            pyramid.position = Vector3(pyramid.position.x, pyramid.position.y+0.1, pyramid.position.z)
        # Forwards
        if keys[pygame.K_q]:
            pyramid.position = Vector3(pyramid.position.x, pyramid.position.y, pyramid.position.z+0.1)
        # Backwards
        if keys[pygame.K_e]:
            pyramid.position = Vector3(pyramid.position.x, pyramid.position.y, pyramid.position.z-0.1)

        # Render the scene
        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()

        # Limits frame rate
        while time.time() -prev_time < 0.0069:
            continue

# Run the main function
main()
