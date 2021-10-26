#Import Pygame
import pygame

# Created Class to implement OOP
class FruitBasket:

    # Constructor of the class
    def __init__(self):

        # Initialize Pygame
        pygame.init()

        # Setting Up the Screen
        self.screen = pygame.display.set_mode((800, 600))
        
        # Title of the Screen 
        pygame.display.set_caption("Fruit Basket v.1.0")

        # Icon of the Screen
        icon = pygame.image.load("assets/icon.png") 
        pygame.display.set_icon(icon)

        # Background Image
        self.background = pygame.image.load("assets/background.jpg")

        # Link all the Sound
        self.background_channel = pygame.mixer.Channel(0) # Background Music
        self.eat_channel = pygame.mixer.Channel(1) # Eating Fruits Sound Effect
        self.burp_channel = pygame.mixer.Channel(2) # Burp Sound Effect

        # Play the Background Music Repeatedly
        self.background_channel.play(pygame.mixer.Sound("assets/backgroundmusic.mp3"), loops=-1)

        # Link the Logo 
        self.logo = pygame.image.load("assets/logo.png")
        self.logo_rec = self.logo.get_rect()
        self.logo_rec.center = 800 // 2, 150

        # Link all the Buttons

        # Play Button (Main Menu Section)
        self.play = pygame.image.load("assets/play.png")
        self.play_rec = self.play.get_rect()
        self.play_rec.center = 800 // 2, 340

        # Info Button (Main Menu Section)
        self.info = pygame.image.load("assets/info.png")
        self.info_rec = self.info.get_rect()
        self.info_rec.center = 800 // 2, 420

        # Quit Button (Main Menu Section)
        self.quit = pygame.image.load("assets/quit.png")
        self.quit_rec = self.quit.get_rect()
        self.quit_rec.center = 800 // 2, 500

        # Proceed Button (Pick Section)
        self.proceed = pygame.image.load("assets/proceed.png")
        self.proceed_rect = self.proceed.get_rect()
        self.proceed_rect.center = 770 // 2, 520

        # Eat Button (Eat Section)
        self.eat = pygame.image.load("assets/eat.png")
        self.eat_rect = self.eat.get_rect()
        self.eat_rect.center = 760 // 2, 510

        # Play Again Button (Last Section)
        self.again = pygame.image.load("assets/playagain.png")
        self.again_rect = self.again.get_rect()
        self.again_rect.center = 800 // 2, 370

        # Back to Menu (Last Section) (Info Section)
        self.menu = pygame.image.load('assets/backtomenu.png')
        self.menu_rect = self.menu.get_rect()

        # Link all the Fruit Images

        # Apple
        self.apple = pygame.image.load('assets/apple.png')
        self.apple_rect = self.apple.get_rect()

        # Guava
        self.guava = pygame.image.load('assets/guava.png')
        self.guava_rect = self.guava.get_rect()

        # Mango
        self.mango = pygame.image.load('assets/mango.png')
        self.mango_rect = self.mango.get_rect()

        # Orange
        self.orange = pygame.image.load('assets/orange.png')
        self.orange_rect = self.orange.get_rect()

        # Link all the Text Images

        # Choose Fruit (Pick Section)
        self.choose_fruit =  pygame.image.load('assets/choosefruit.png')
        self.choose_fruit_rect = self.choose_fruit.get_rect()
        self.choose_fruit_rect.center = 800 // 2, 180

        # Basket Text (Eat Section)
        self.basket_text =  pygame.image.load('assets/baskettext.png')
        self.basket_text_rect = self.basket_text.get_rect()
        self.basket_text_rect.center = 800 // 2, 100

        # No More Fruits (Last Section)
        self.no_fruits =  pygame.image.load('assets/nomorefruits.png')
        self.no_fruits_rect = self.no_fruits.get_rect()
        self.no_fruits_rect.center = 800 // 2, 250

        # Actual Text

        # Font Reference
        self.font = pygame.font.SysFont('Arial Bold', 30)

        # Want to Eat Again (Last Section)
        self.again = self.font.render('Want to Eat Again?', False, (0, 0, 0))

        # Pick Fruits you want (Pick Section)
        self.pick = self.font.render('Pick Fruits you want', False, (0, 0, 0))

        # Number Indicator of Pick Fruits (Pick Section)
        self.num_fruits = self.font.render('Maximum of 8 Fruits only: 8', False, (0, 0, 0))


# Call the Class
FruitBasket()