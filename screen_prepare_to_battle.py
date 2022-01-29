import tkinter

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        # displays users info
        tkinter.Label(self, text = "You").grid(row = 0, column = 0)
        imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label(self, image = imageLarge)
        w.photo = imageLarge
        w.grid(row = 1, column = 0)
        
        tkinter.Label(self, text = f"{self.player1.hit_points} HPS").grid(row = 2, column = 0)
        tkinter.Label(self, text = f"{self.player1.dexterity} Dexterity").grid(row = 3, column = 0)
        tkinter.Label(self, text = f"{self.player1.strength} Strength").grid(row = 4, column = 0)


        # displays computer info
        tkinter.Label(self, text = "Computer").grid(row = 0, column = 1)
        image_large = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label(self, image = image_large)
        w.photo = image_large
        w.grid(row = 1, column = 1)
        
        tkinter.Label(self, text = f"{self.player2.hit_points} HPS").grid(row = 2, column = 1)
        tkinter.Label(self, text = f"{self.player2.dexterity} Dexterity").grid(row = 3, column = 1)
        tkinter.Label(self, text = f"{self.player2.strength} Strength").grid(row = 4, column = 1)

        # button to proceed to next screen
        tkinter.Button(self, command = self.commence_battle_clicked, text = "Commence Battle!", bg = "red").grid(row = 4, column = 2)

        
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        