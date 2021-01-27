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

    # Create a test sphere
    tsphere = Object3d("TestSphere")
    tsphere.scale = Vector3(1, 1, 1)
    tsphere.positon = Vector3(0, 0, 0)
    tsphere.mesh = Mesh.create_sphere((1, 1, 1), 5, 5)
    tsphere.material= Material(Color(0,0,1), "Blue World")
    scene.add_object(tsphere)

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

        # Get the pressed keys 
        keys=pygame.key.get_pressed()

        # Returns the correct rotation value
        rotation=Quaternion.AngleAxis(axis, math.radians(angle)*delta_time)

        # Handle the movement
        if keys[pygame.K_LEFT]:
            tsphere.rotation*=rotation
        if keys[pygame.K_RIGHT]:
            tsphere.rotation*=rotation
        if keys[pygame.K_UP]:
            tsphere.rotation*=rotation
        if keys[pygame.K_DOWN]:
            tsphere.rotation*=rotation
        if keys[pygame.K_PAGEUP]:
            tsphere.rotation*=rotation
        if keys[pygame.K_PAGEDOWN]:
            tsphere.rotation*=rotation

        # Render the scene
        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
