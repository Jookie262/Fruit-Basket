# Import Pygame
import pygame

# Created Class to implement OOP
class FruitBasket:

    # Constructor of the class
    def __init__(self):

        # Initialize Pygame
        pygame.init()

        # Size of the Screen
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

        # Max Number of fruits to Pick 
        self.max_fruit = 8
        
        # Array for Storing the Fruits Pick
        self.fruit_stack = []

        # Change of Scene in Screen
        self.scene_menu = 0             # For Main Menu Section
        self.scene_pick = 1             # For Pick Section
        self.scene_eat = 2              # For Eat Section
        self.scene_last = 3             # For Last Section
        self.scene_info = 4             # For Info Section
        self.scene = self.scene_menu    # Holds the Current Scene

        # Loop each scene and look for any changes
        while True:
            if self.scene == self.scene_menu:
                self.scene = self.mainMenu()
            elif self.scene == self.scene_pick:
                self.scene = self.pickGame()
            elif self.scene == self.scene_eat:
                self.scene = self.eatGame()
            elif self.scene == self.scene_congrats:
                self.scene = self.lastGame()
            elif self.scene == self.scene_info:
                self.scene = self.menuInfo()

    # =========================================================================== #

    # Method for the Main Menu Section
    def mainMenu(self):
        
        # Loop each events
        while True:

            # Get the Mouse Position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Get all the events
            for event in pygame.event.get():

                # If the user click the x button
                if event.type == pygame.QUIT:
                    quit() # Exits the game

                # If the user presses or releases a mouse button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # If the user click any of those buttons
                    if self.play_rec.collidepoint(mouse_x, mouse_y):    # Play button
                        return self.scene_pick # Change the self.scene value to 1

                    elif self.info_rec.collidepoint(mouse_x, mouse_y):  # Info Button
                        return self.scene_info # Change the self.scene value to 4

                    elif self.quit_rec.collidepoint(mouse_x, mouse_y):  # Quit Button
                        quit() # Exits the game

            # Set the Background
            self.screen.blit(self.background,(0,0))

            # Show the Logo
            self.screen.blit(self.logo,self.logo_rec)

            # Show the Play Button
            self.screen.blit(self.play,self.play_rec)

            # Show the Info Button
            self.screen.blit(self.info,self.info_rec)

            # Show the Quit Button
            self.screen.blit(self.quit,self.quit_rec)
    
            # Update the Screen 
            pygame.display.update()

    # =========================================================================== #

    # Method for the Pick Section
    def pickGame(self):
        
        # Loop each events
        while True:

            # Get the Mouse Position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Get all the events
            for event in pygame.event.get():

                # If the user click the x button
                if event.type == pygame.QUIT:
                    quit() # Exit the game

                # If the user presses or releases a mouse button
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Proceed to Eat Section when Selected a Minimum of 1 Fruit
                    if self.max_fruit <= 7:
                         if self.proceed_rect.collidepoint(mouse_x, mouse_y):
                            return self.scene_eat
                    
                    # Can only accepts with a max of 8 fruits
                    if self.max_fruit > 0:

                        # If the user click the image of apple
                        if self.apple_rect.collidepoint(mouse_x, mouse_y):
                            self.insertShowPick("Apple") # Call the Method InsertShowPick

                         # If the user click the image of Guava 
                        elif self.guava_rect.collidepoint(mouse_x, mouse_y):
                            self.insertShowPick("Guava") # Call the Method InsertShowPick

                         # If the user click the image of Mango
                        elif self.mango_rect.collidepoint(mouse_x, mouse_y):
                            self.insertShowPick("Mango") # Call the Method InsertShowPick

                         # If the user click the image of Orange
                        elif self.orange_rect.collidepoint(mouse_x, mouse_y):
                            self.insertShowPick("Orange") # Call the Method InsertShowPick

                    else:
                        # Prints this statement when exceed the num of fruits pick
                        self.pick = self.font.render('Exceed Num of Fruits', False, (0, 0, 0))

            # Set the Background
            self.screen.blit(self.background,(0,0))

            # Show the Choose Fruits Image Text
            self.screen.blit(self.choose_fruit, self.choose_fruit_rect)

            # Set the Location and Show Apple Image
            self.apple_rect.center = 350 // 2 , 600 // 2
            self.screen.blit(self.apple, self.apple_rect)

            # Set the Location and Show Guava Image
            self.guava_rect.center = 650 // 2, 600 // 2
            self.screen.blit(self.guava, self.guava_rect)

            # Set the Location and Show Mango Image
            self.mango_rect.center = 950 // 2, 600 // 2
            self.screen.blit(self.mango, self.mango_rect)

            # Set the Location and Show Orange Image
            self.orange_rect.center = 1250 // 2, 600 // 2
            self.screen.blit(self.orange, self.orange_rect)

            # Set the Location and Show the Dynamic Pick Fruits Text
            self.screen.blit(self.pick, (580 // 2, 400))

            # Set the Location and Show the Number of Fruits you Pick
            self.screen.blit(self.num_fruits, (510 // 2, 440))

            # Show the Proceed button if you pick a minimum of 1 fruit 
            if self.max_fruit <= 7:
                self.screen.blit(self.proceed, self.proceed_rect)

            # Update the Screen 
            pygame.display.update()

    # =========================================================================== #

    # Method for the Eat Section
    def eatGame(self):
        
        # Loop each events
        while True:
            
            # Get all the events
            for event in pygame.event.get():

                # If the user click the x button
                if event.type == pygame.QUIT:
                    quit() # Exit the game

        # Update the Screen 
        pygame.display.update()

    # =========================================================================== #

    # Method for the Last Section
    def lastGame(self):
        
        # Loop each events
        while True:
            
            # Get all the events
            for event in pygame.event.get():

                # If the user click the x button
                if event.type == pygame.QUIT:
                    quit() # Exit the game

        # Update the Screen 
        pygame.display.update()

    # =========================================================================== #

    # Method for the Info Section
    def menuInfo(self):
        
        # Loop each events
        while True:
            
            # Get all the events
            for event in pygame.event.get():

                # If the user click the x button
                if event.type == pygame.QUIT:
                    quit() # Exit the game

        # Update the Screen 
        pygame.display.update()

    # =========================================================================== #

    # Method to used in the Pick Section since there is a repetitive in the statements
    # This append the fruit to the list and display the text dynamically in the Pick Section
    def insertShowPick(self, fruit):

        # Append to the List
        self.fruit_stack.append(fruit)

        # Display the Fruit Pick
        self.pick = self.font.render('You Choose: ' + fruit, False, (0, 0, 0)) 

        # Minus the max_fruit variable Everytime the fruit is pick
        self.max_fruit -= 1 

        # Display the number of fruits you pick decrementally
        self.num_fruits = self.font.render('Maximum of 8 Fruits only: ' + str(self.max_fruit), False, (0, 0, 0)) 

    # =========================================================================== #

# Call the Class
FruitBasket()