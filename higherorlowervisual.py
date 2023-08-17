import wx
import random


class HigherLowerGame(wx.Frame):
    def __init__(self, parent, title):
        super(HigherLowerGame, self).__init__(parent, title=title, size=(400, 200))

        self.lives = 10
        self.random_number = random.randint(1, 100)

        self.panel = wx.Panel(self)

        self.title_text = wx.StaticText(self.panel, label="Welcome to the 'Higher or Lower' game!", pos=(50, 20))
        self.lives_text = wx.StaticText(self.panel, label=f"You have {self.lives} lives left.", pos=(50, 50))
        self.input_label = wx.StaticText(self.panel, label="Guess a number between 1 and 100:", pos=(50, 80))
        self.input_box = wx.TextCtrl(self.panel, pos=(50, 100), size=(100, -1))
        self.button = wx.Button(self.panel, label="Guess", pos=(180, 100))

        self.button.Bind(wx.EVT_BUTTON, self.check_guess)

        self.Show()

    def check_guess(self, event):
        input_value = self.input_box.GetValue()
        
        try:
            number = int(input_value)
            if number == self.random_number:
                wx.MessageBox("You guessed the correct number!")
                self.Close()
            elif number < self.random_number:
                wx.MessageBox(f"{number} is smaller than the chosen number.")
            elif number > self.random_number:
                wx.MessageBox(f"{number} is larger than the chosen number.")
            
            self.lives -= 1
            self.lives_text.SetLabel(f"You have {self.lives} lives left.")

            if self.lives <= 0:
                wx.MessageBox(f"You failed! The correct number was {self.random_number}")
                self.Close()
        except ValueError:
            wx.MessageBox("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    app = wx.App()
    HigherLowerGame(None, title="Higher or Lower Game")
    app.MainLoop()