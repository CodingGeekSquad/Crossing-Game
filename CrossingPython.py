#Gain acces to pygame library
import pygame

#screen size
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
#Color in rgb code
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)
SCREEN_WIDTH_MENU = 600
SCREEN_HEIGHT_MENU = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)


class Game:
    game_lvl = 1
    
    TICK_RATE = 60

    def __init__(self, image_path,  title, width, height):
        self.title = title
        self.width = width
        self.height = height

        #create the window
        self.game_screen = pygame.display.set_mode((width, height))
        #set game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

            
    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = playerCharacter('player.png', 420, 775, 50, 50)
        enemy_0 = nonPlayerCharacter('enemy.png', 175, 325, 50, 50)
        enemy_0.SPEED *= level_speed

        enemy_1 = nonPlayerCharacter('enemy.png', 850, 175, 50, 50)

        enemy_1.SPEED *= level_speed

        enemy_2 = nonPlayerCharacter('enemy.png', 650, 500, 50, 50)
        enemy_2.SPEED *= level_speed

        enemy_3 = nonPlayerCharacter('enemy.png', 20, 675, 50, 50)
        enemy_3.SPEED *= level_speed

        
        treasure = GameObject('treasure.png', 420, 50, 50, 50)

        
        pygame.display.update()
        clock.tick(1)
        #Main game loop, update all movement, graphics, ect.
        while not is_game_over:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_game_over = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            direction = 1
                        elif event.key == pygame.K_DOWN:
                            direction = -1
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame. K_UP or event.key == pygame.K_DOWN:
                             direction = 0
              
                        
                #print(event)

                self.game_screen.fill(WHITE_COLOR)
                self.game_screen.blit(self.image, (0, 0))
                
                treasure.draw(self.game_screen)
                

                player_character.move(direction, self.height)
                player_character.draw(self.game_screen)

                enemy_0.move(self.width)
                enemy_0.draw(self.game_screen)

                if level_speed > 1:
                     enemy_1.move(self.width)
                     enemy_1.draw(self.game_screen)
                if level_speed > 2.5:
                     enemy_2.move(self.width)
                     enemy_2.draw(self.game_screen)
                if level_speed > 4:
                     enemy_3.move(self.width)
                     enemy_3.draw(self.game_screen)


                if player_character.detect_collision(enemy_0):
                    is_game_over = True
                    did_win = False
                    text = font.render('You Lose!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (300,350))
                    pygame.display.update()
                    clock.tick(1)
                    break

                if player_character.detect_collision(enemy_1):
                    is_game_over = True
                    did_win = False
                    text = font.render('You Lose!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (300,350))
                    pygame.display.update()
                    clock.tick(1)
                    break

                if player_character.detect_collision(enemy_2):
                    is_game_over = True
                    did_win = False
                    text = font.render('You Lose!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (300,350))
                    pygame.display.update()
                    clock.tick(1)
                    break

                if player_character.detect_collision(enemy_3):
                    is_game_over = True
                    did_win = False
                    text = font.render('You Lose!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (300,350))
                    pygame.display.update()
                    clock.tick(1)
                    break

                elif player_character.detect_collision(treasure):
                    is_game_over = True
                    did_win = True
                    text = font.render('You Win!', True, BLACK_COLOR)
                    self.game_screen.blit(text, (300,350))
                    self.game_lvl += 1
                    pygame.display.update()
                    clock.tick(1)
                    break
                
                level = font.render('Level: %d' % self.game_lvl, True, BLACK_COLOR)
                self.game_screen.blit(level, (150,740))
                #update all game graphics
                pygame.display.update()
                clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

    def play_again(self):
        text = bigfont.render('Play again?', 13, (0, 0, 0))
        textx = SCREEN_WIDTH_MENU / 2 - text.get_width() / 2
        texty = SCREEN_HEIGHT_MENU / 2 - text.get_height() / 2
        textx_size = text.get_width()
        texty_size = text.get_height()
        pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                                (textx_size + 10, texty_size +
                                                    10)))

        screen.blit(text, (SCREEN_WIDTH_MENU / 2 - text.get_width() / 2,
                        SCREEN_HEIGHT_MENU / 2 - text.get_height() / 2))

        clock = pygame.time.Clock()
        pygame.display.flip()
        in_main_menu = True
        while in_main_menu:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_main_menu = False
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x >= textx - 5 and x <= textx + textx_size + 5:
                        if y >= texty - 5 and y <= texty + texty_size + 5:
                            in_main_menu = False
                            self.game_lvl = 1
                            return 1
                            break        
            
class GameObject:


    def __init__(self, image_path, x, y, width, height):
        
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
    
        
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class playerCharacter(GameObject):

    SPEED = 6

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50
        elif self.y_pos <= 20:
            self.y_pos = 20


    def detect_collision(self, other_body_0):
        if self.y_pos > other_body_0.y_pos + other_body_0.height:
            return False
        elif self.y_pos + self.height < other_body_0.y_pos:
            return False

        if self.x_pos > other_body_0.x_pos + other_body_0.width:
            return False
        elif self.x_pos + self.width < other_body_0.x_pos:
            return False

        return True
 
            

class nonPlayerCharacter(GameObject):

    SPEED = 2.5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 60:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED



#initializing pygame
pygame.init()
new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
ret = 1
while ret:
    new_game.run_game_loop(1)
    ret = new_game.play_again()

#quit pygame and the program    
pygame.quit()
quit()





                    #player_image = pygame.image.load('player.png')
                    #player_image = pygame.transform.scale(player_image, (50, 50))
                    #enemy_image = pygame.image.load('enemy.png')

                #pygame.draw.rect(game_screen, BLACK_COLOR, [450, 450, 100, 100])
                #pygame.draw.circle(game_screen, BLACK_COLOR, (500, 400), 50)

                #game_screen.blit(player_image, (475, 475))







