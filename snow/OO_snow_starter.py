"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class Snowflake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    def __init__(self, size, position_x, position_y, wind):
        self.size = size
        self.position_x = position_x
        self.position_y = position_y
        self.wind = wind
    
    
    def fall(self):
       self.position_y += random.randint(2, 5)

    """
    Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
    A positive integer will have the snowflake falling down the screen. 
    A negative integer will have the snowflake falling up the screen. 
        
    If wind = True
    - the x direction of the snowflake changes
     """
        
    def draw(self):
        snow = pygame.draw.circle(screen, WHITE,(self.position_x, self.position_y), 3, 0)
      
        # """
        # Uses pygame and the global screen variable to draw the snowflake on the screen
        # """

    def slant(self):
        if self.wind == True:
            self.position_x += 1

        if self.position_x >= 700:
            position_x = 0

        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
 


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = []

y = 0 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    # background = os.path.join("C:\Users\GWC4\Documents\Snow\joshua_tree_winter.jpg")
    # background_surface = pygame.image.load(background)
    # screen.blit(background_surface, (0,0))

    # --- Drawing code should go here
    #snow = pygame.draw.circle(screen, WHITE, (random_x, y) , size, 0)
    # Begin Snow
    random_x = random.randint(0,700)
   
    snowy = Snowflake(3, random_x, 0, True)
    snow_list.append(snowy)
    
    for snow in snow_list:
        snow.draw()
        snow.fall()
        snow.slant()

    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
