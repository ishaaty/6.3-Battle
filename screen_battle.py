import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''

        tkinter.Button(self, text = "Attack", bg = "red", command = self.attack_clicked).grid(row = 0, rowspan = 3, column = 0)

        self.player1_attack_lbl = tkinter.Label(self, text = "")
        self.player1_attack_lbl.grid(row = 0, column = 1)

        self.player2_attack_lbl = tkinter.Label(self, text = "")
        self.player2_attack_lbl.grid(row = 1, column = 1)


        tkinter.Label(self, text = "You").grid(row = 3, column = 0)
        imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label(self, image = imageLarge)
        w.photo = imageLarge
        w.grid(row = 4, column = 0)
        self.player1_hp_lbl = tkinter.Label(self, text = f"{self.player1_max_hp}/{self.player1_max_hp} HPS")
        self.player1_hp_lbl.grid(row = 5, column = 0)

        tkinter.Label(self, text = "Computer").grid(row = 3, column = 1)
        imageLarge = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label(self, image = imageLarge)
        w.photo = imageLarge
        w.grid(row = 4, column = 1)
        self.player2_hp_lbl = tkinter.Label(self, text = f"{self.player2_max_hp}/{self.player2_max_hp} HPS")
        self.player2_hp_lbl.grid(row = 5, column = 1)
        

        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''  

        result1 = self.player1.attack(self.player2)
        self.player1_attack_lbl["text"] = result1


        result2 = self.player2.attack(self.player1)
        self.player2_attack_lbl["text"] = result2


        if self.player1_max_hp <= 0:
            tkinter.Label(self, text = f"{self.player2.name} is victorious!", fg = "red").grid(row = 2, column = 1)
        elif self.player2_max_hp <= 0:
            tkinter.Label(self, text = f"{self.player1.name} is victorious!", fg = "red").grid(row = 2, column = 1)    

                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            