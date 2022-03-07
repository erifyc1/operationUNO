#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Button import Button
from Game import Game
import pygame
import pygame.mixer as mixer
from pygame.mixer import music as msound

class Difficulty:
    # This will let user change difficulty mode in pop-up menu screen
    def changeDifficulty(game_instance):
        # changeable constants -----
        screen_x = 800
        screen_y = 600
        background_size = (screen_x, screen_y)

        colors = {
            "white": (255, 255, 255),
            "grey": (230, 230, 230),
            "green": (0,255,0),
            "blue": (0,0,255),
            "red": (255,0,0),
            "dark_red": (139,0,0),
            "crimson": (246,26,26),
            "black": (0,0,0),
            "purple": (48,25,52),
            "yellow": (255,255,0)
        }

        background_color = colors["red"]

        # functions -------------------------

        def displayWindow(window):
            window.fill(background_color) # change color if you want

        def displayMessage(msg, color, dest, display):
            screen_text = font.render(msg, True, color)
            display.blit(screen_text, dest)

        # window set up
        pygame.init()
        window = pygame.display.set_mode(background_size)
        pygame.display.set_caption('Operation-Uno')

        # text and font
        font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', 60)
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', 22)
        png = pygame.image.load('Resources/Images/uno.png')

        easy_button = Button(colors["green"], [15, 175], [100, 50], button_font, "Easy", colors["green"], (37,186,176))
        medium_button = Button(colors["yellow"], [15, 250], [200, 50], button_font, "Medium", colors["yellow"], (37,186,176))
        hard_button = Button(colors["purple"], [15, 325], [200, 50], button_font, "Hard", colors["purple"], (37,186,176))
        
        # Have the background fanfare playing while the menu is running
        msound.load("Resources/Sounds/Fanfare-sound.wav")
        msound.play(-1)
        if (game_instance.getSoundEffects() == "off"):
            msound.pause()
        else:
            msound.play(-1)
            
        run = True
        while run:
            mouse_pos = pygame.mouse.get_pos()

            

            # ---------------- updates -----------------
            easy_button.updateButton(mouse_pos, window)
            medium_button.updateButton(mouse_pos, window)
            hard_button.updateButton(mouse_pos, window)

            for event in pygame.event.get(): 
                # ----------- ongoing checks (controls, updates, etc) ----------
                
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.isHovered():
                        game_instance.changeDifficulty('easy')
                        print('Pressed Easy Button')
                        return
                    if medium_button.isHovered():
                        game_instance.changeDifficulty('medium')
                        print('Pressed Medium Button')
                        return
                    if hard_button.isHovered():
                        game_instance.changeDifficulty('hard')
                        print('Pressed Hard Button')
                        return
            
            # ---------- renders --------------
            displayWindow(window)
            displayMessage("OPERATION UNO", colors["white"], [150, 25], window)
            easy_button.displayButton(window)
            medium_button.displayButton(window)
            hard_button.displayButton(window)
            window.blit(png, (225, 150))
            # pygame.display.flip() # Do we need this? I feel like this will change the layout of the window

            # ----------- final update --------------
            pygame.display.update()
