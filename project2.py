import pygame


SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
red = (255,0,0)
difficulty = ""

# Below we changed the caption change is below
pygame.display.set_caption("Kailey's Pong")
# Above we changed the caption change above

pygame.font.init()
clock = pygame.time.Clock()
FPS = 60


class Player():
        def __init__(self, name):
                if name == "player":
                        self.x, self.y = 16, SCR_HEI/2
                else:
                        self.x, self.y = SCR_WID-48, SCR_HEI/2 
                self.speed = 3
                self.padWid, self.padHei = 32, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
                self.img = pygame.image.load("paddle.jpg")
                self.paddle = pygame.transform.scale(self.img, (self.padWid, self.padHei))
                self.rect = self.paddle.get_rect()
       
        def scoring(self, name):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 0, 0))
                if name == "player":
                        screen.blit(scoreBlit, (32, 16))
                        if self.score == 10:
                                print ("player  wins!")
                                exit()
                else:
                        screen.blit(scoreBlit, (SCR_HEI+92, 16))
                        if self.score == 10:
                                print ("Enemy wins!")
                                exit()
                        
       
        def movement(self, name):
                if name == "player":
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_w]:
                                self.y -= self.speed
                        elif keys[pygame.K_s]:
                                self.y += self.speed
               
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
                if name == "enemy":
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                                self.y -= self.speed
                        elif keys[pygame.K_DOWN]:
                                self.y += self.speed
       
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
       
        def draw(self):
                pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.padWid, self.padHei))
                screen.blit(self.paddle, (self.x, self.y))
 
##class Enemy():
##        def __init__(self):
##                self.x, self.y = SCR_WID-16, SCR_HEI/2
##                self.speed = 3
##                self.padWid, self.padHei = 8, 64
##                self.score = 0
##                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
##       
##        def scoring(self):
##                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 0, 0))
##                screen.blit(scoreBlit, (SCR_HEI+92, 16))
##                if self.score == 10:
##                        print ("Player 2 wins!")
##                        exit()
##       
##        def movement(self):
##                keys = pygame.key.get_pressed()
##                if keys[pygame.K_UP]:
##                        self.y -= self.speed
##                elif keys[pygame.K_DOWN]:
##                        self.y += self.speed
##       
##                if self.y <= 0:
##                        self.y = 0
##                elif self.y >= SCR_HEI-64:
##                        self.y = SCR_HEI-64
##       
##        def draw(self):
##                pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.padWid, self.padHei))
 
class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.x2, self.y2 = SCR_WID/2, SCR_HEI/2
                self.speed_x2 = -3
                self.speed_y2 = -3
                self.size = 8
       
        def movement(self, player, enemy):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x = 3
                        player.score += 1
                ##wall col
                #paddle col
                        
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x:
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col

                for n in range(-self.size, player.padHei):
                        if self.y == wall.y + n:
                                if self.x == wall.x - wall.padWid:
                                        self.speed_x *= -1
                                        break

        def movement2(self, player, enemy):
                self.x += self.speed_x2
                self.y += self.speed_y2
 
                #wall col
                if self.y <= 0:
                        self.speed_y2 *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y2 *= -1
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x2 = 3
                        player.score += 1
                ##wall col
                #paddle col
                        
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x2 *= -1
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x:
                                        self.speed_x2 *= -1
                                        break
                        n += 1
                ##paddle col

                for n in range(-self.size, player.padHei):
                        if self.y == wall.y + n:
                                if self.x == wall.x - wall.padWid:
                                        self.speed_x *= -1
                                        break
 
        def draw(self):
                pygame.draw.rect(screen, (255, 0,0), (self.x, self.y, 8, 8))

class Wall():
        def __init__(self):
                self.x, self.y = (SCR_WID/2)-4, (SCR_HEI/2)-50
                self.speed = 4
                self.padWid, self.padHei = 8, 100
                self.size = 8
                self.img = pygame.image.load("brick.jpg")
                self.wall = pygame.transform.scale(self.img, (self.padWid, self.padHei))
                self.rect = self.wall.get_rect()
                
        def move(self):
                self.y += self.speed
                if self.y <= 0:
                        self.speed *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed *= -1
                
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
                screen.blit(self.wall, (self.x, self.y))

wall = Wall()
                
def difficulty():
        smallfont = pygame.font.SysFont(None, 25)
        difficulty = True
        text = smallfont.render("Would you like to play on easy, or hard? Type E for easy, and H for hard!",True , red)
        screen.blit(text, [15,220])
        pygame.display.update()
        clock.tick(15)
        while difficulty == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_e]:
                                global difficulty
                                difficulty = "easy"
                                intro = False
                        
                        elif keys[pygame.K_h]:
                                global difficulty
                                difficulty = "hard"
                                intro = False


# below we added the main
def main():
        player = Player("player")
        enemy = Player("enemy")
        ball = Ball()
        ball2 = Ball()
        while True:
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        exit()
                if difficulty == "easy":
                        ball.movement(player, enemy)
                        player.movement("player")
                        enemy.movement("enemy")
                        bkg = pygame.image.load("background.png")
                        trubg = pygame.transform.scale(bkg,(SCR_WID, SCR_HEI))
                        screen.blit(trubg,[0,0])
                        ball.draw()
                        player.draw( )
                        player.scoring("player")
                        enemy.draw()
                        enemy.scoring("enemy")
                        pygame.display.flip()
                        clock.tick(FPS)

                elif difficulty == "hard":
                        ball.movement(player, enemy)
                        ball2.movement2(player, enemy)
                        player.movement("player")
                        enemy.movement("enemy")
                        bkg = pygame.image.load("background.png")
                        trubg = pygame.transform.scale(bkg,(SCR_WID, SCR_HEI))
                        screen.blit(trubg,[0,0])
                        ball.draw()
                        ball2.draw()
                        player.draw( )
                        player.scoring("player")
                        enemy.draw()
                        enemy.scoring("enemy")
                        wall.draw()
                        wall.move()
                        pygame.display.flip()
                        clock.tick(FPS)

difficulty()
main()
# above we added the main

