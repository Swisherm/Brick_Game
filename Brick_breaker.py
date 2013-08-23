## Brick Breaking Game
## v1.0




####Notes



##imports

from livewires import games, color
import random



#create window
games.init(screen_width = 1000, screen_height = 800, fps = 50)


class Paddle(games.Sprite):
    """The Paddle"""
    image = games.load_image("paddle.bmp")

    def __init__(self):
        """ start paddle and begin score keeping"""
        super(Paddle, self).__init__(image = Paddle.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height - 80)
        

    def update(self):
        """move with the mouse. """
        self.x = games.mouse.x

        if self.left < 25:
            self.left = 25
            
        if self.right > (games.screen.width - 25):
            self.right = (games.screen.width - 25)

        for ball in self.overlapping_sprites:
            ball.bounce()
            
class Brick(games.Sprite):

    NUM_BRICKS = 4
    brick_color = int(random.randrange(NUM_BRICKS))
    if brick_color == 0:
        new_brick = games.load_image("blue_brick.bmp")
    elif brick_color == 1:
        new_brick = games.load_image("green_brick.bmp")
    elif brick_color == 2:
        new_brick = games.load_image("red_brick.bmp")
    elif brick_color == 3:
        new_brick = games.load_image("yellow_brick.bmp")
    brick_image = new_brick
    
    
    def __init__(self, x, y):
        NUM_BRICKS = 4
        brick_color = int(random.randrange(NUM_BRICKS))
        if brick_color == 0:
            new_brick = games.load_image("blue_brick.bmp")
        elif brick_color == 1:
            new_brick = games.load_image("green_brick.bmp")
        elif brick_color == 2:
            new_brick = games.load_image("red_brick.bmp")
        elif brick_color == 3:
            new_brick = games.load_image("yellow_brick.bmp")
        brick_image = new_brick
        self._surface = brick_image
        self._rect = self._surface.get_rect()
        self.position = (x, y)
        self._tickable = 0
        self._next = 0
        self._gone = 0
        

        self.score = games.Text(value = 0, size = 50, color = color.white,
                                top = 750, right = games.screen.width - 60)
        games.screen.add(self.score)
        
        
        
    def update(self):
        
        for ball in self.overlapping_sprites:
            self.contact()
            self.bounce()
            self.score.value += 25
            self.score.right = games.screen.width -60
            

    def contact(self):
        self.destroy()


    def __del__(self):
        if screen and not self._gone:
            self.destroy()
class Ball(games.Sprite):
    """The Pong Ball"""
    def update(self):
        if self.right > (games.screen.width - 25) or self.left < 25:
            self.dx = -self.dx

        if self.top < 15:
            self.dy = -self.dy

        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
            
    def end_game(self):
        "end of game"
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        
    def bounce(self):
        self.dy = -self.dy
        

def main():
    """ Playing the game"""
    #background
    wall_image = games.load_image("lrg_back.jpg", transparent = False)
    games.screen.background = wall_image

    #inserting new bricks
    '''
    insert the first level of brick pattern here
    '''
    ## Group of bricks
    bricks = []

    ##Locations
    bricks.append(Brick(70, 50))
    bricks.append(Brick(140, 50))
    
    ## add bricks to window
    #for brick in bricks:
        #games.screen.add(brick)

    brick1 = Brick(300, 200)
    games.screen.add(brick1)

    #the ball
    
    ball_image = games.load_image("ball.bmp")
    the_ball = Ball(image = ball_image,
                    x = games.screen.width/2,
                    y = games.screen.height/2 + 120,
                    dx = 2,
                    dy = -2)
    games.screen.add(the_ball)

    #the paddle

    the_paddle = Paddle()
    games.screen.add(the_paddle)

    games.mouse.is_visible = False

    games.screen.event_grab = True


    games.screen.mainloop()

main()
