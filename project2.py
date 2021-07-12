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

def difficulty():
        smallfont = pygame.font.SysFont(None, 25)
        intro = True
        text = smallfont.render("Would you like to play on easy, or hard? Type E for easy, and H for hard!",True , red)
        screen.blit(text, [15,220])
        pygame.display.update()
        clock.tick(15)
        while intro == True:
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


class Player():
        def __init__(self, name):
                if name == "player":
                        self.x, self.y = 16, SCR_HEI/2
                else:
                        self.x, self.y = SCR_WID-16, SCR_HEI/2 
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
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
                                if self.x >= enemy.x - enemy.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col
 
        def draw(self):
                pygame.draw.rect(screen, (255, 0,0), (self.x, self.y, 8, 8))




#player = Player()

# below we added the main
def main():
        difficultySetting = difficulty()
       
        if difficultySetting == 'e':
                print("This prints if the difficulty level was set to easy.")
                

        elif difficultySetting == 'm':
                print("This prints if the difficulty level was set to medium.")


        elif difficultySetting == 'h':
                print("This prints if the difficulty level was set to hard.")
                

        player = Player("player")
        enemy = Player("enemy")
        ball = Ball()
        while True:
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        exit()
                ##process
                #logic
                ball.movement(player, enemy)
                player.movement("player")
                enemy.movement("enemy")
                ##logic
                #draw
                
                #insert an image in to the background
                bkg = pygame.image.load("pong_table.png")
                trubg = pygame.transform.scale(bkg,(SCR_WID, SCR_HEI))
                screen.blit(trubg,[0,0])
                #insert an image in to the background
                
                #screen.fill((0, 0, 0))
                ball.draw()
                player.draw( )
                player.scoring("player")
                enemy.draw()
                enemy.scoring("enemy")
                ##draw
                #_______
                pygame.display.flip()
                clock.tick(FPS)

difficulty()
main()
