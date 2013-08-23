#Brick_lvl1
'''
design a brick pattern
'''
import Brick_breaker

##loading bricks





def hello():
    hello = games.Message(value = "Level One",
                          size = 90,
                          color = color.red,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          lifetime = 5 * games.screen.fps)
    games.screen.add(hello)
    
def populate():
    bricks = []
    bricks.append(Brick_breaker.Brick(70, 50))
    bricks.append(Brick_breaker.Brick(140, 50))
    games.screen.add(bricks)
                  
                  
    
                          
        

if __name__ == "__main__":
    print("this is original module running on its own")
    input("\n\nPress enter to exit")
    
