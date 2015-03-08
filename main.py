from kivy.core.window import Window
import json
 # KIVY STUFF

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Canvas
from kivy.uix.popup import Popup
from random import *
from time import time
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.carousel import Carousel
from kivy.animation import Animation
from pygame.examples.scroll import scroll_view
Config.set('graphics','resizable',0)
Window.clearcolor = [.2, .2, .2, 1]


button_color = [.7, .8, 1, 1]


class MyButton(Button):
    """
    My Button class inherits a kivy button and creates uniform buttons
    to use on the menue when needed
    """
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.018
       
        
class SmartMenu(Widget):
    """"
    SmartMenu class is used as a base class for each other menu
    """
    buttonList = []
    
    def __init__(self, **kwargs):
    #create custom events first
        self.register_event_type('on_button_release')
        super(SmartMenu, self).__init__(**kwargs)
      
 
    def on_button_release(self, *args):
        pass
 
    def callback(self,instance):
        print('The button %s is being pressed' % instance.text)
        self.buttonText = instance.text
        self.dispatch('on_button_release') 
 
    def addButtons(self):
        for k in self.buttonList:
            tmpBtn = MyButton(text = k)
            tmpBtn.background_color = button_color
            tmpBtn.font_size = 20
            tmpBtn.bind(on_release = self.callback)
            self.layout.add_widget(tmpBtn)
     
    def buildUp(self):
    #self.colorWindow()
        self.addButtons()
        
class StartMenu(SmartMenu):
#setup the menu button names
    """ 
    This is a start menu class. It inherits from the Smart Menu Class. 
    It is the first screen the user sees after running the game.
    The Start Game button goes to the character selecter
    The 'How To' button creates a popup that is dismissed by clicking anywhere outside it
    """
    buttonList = ['Card Creation', 'Head To Head', 'Party Mode']
    def __init__(self, **kwargs):
        super(StartMenu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = (Window.height/2 - self.layout.height/2)-50
        self.add_widget(self.layout)
 
        #self.add_widget(self.msg)
        # Add the buttons
        tmpBtn = MyButton(text = 'p')
        tmpBtn.size = (50,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(10,10)
        self.add_widget(tmpBtn)
        tmpBtn = MyButton(text = '?')
        tmpBtn.size = (50,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(Window.width-60,10)
        self.add_widget(tmpBtn)
        
        logo = Image(source = 'logo.png');
        logo.pos= (50,Window.height*0.66)
        logo.size = (220,150)
        self.add_widget(logo);
   
        
   
class Card(ButtonBehavior,Image):
    def __init__(self,card_num ,**kwargs):
        super(Card, self).__init__(**kwargs)
        self.text = "card_down"
        card_name = Label(text = "Card"+str(card_num),font_size = 24,x = 190,y=200)
        self.add_widget(card_name)

class Deck(Button):
    def __init__(self,**kwargs):
        super(Deck, self).__init__(**kwargs)
        cards = []
        card = Image(source = 'card.png',allow_stretch= True)
        self.text = "Demo"
        self.font_size = 0
        card.pos = self.pos
        self.size = (75,100)
        deck_name = Label(text = "Demo Deck",x = self.x -20, y=self.y +30,font_size = 10)
        
        
        self.add_widget(deck_name)
        
        
class CardViewer(Widget):
    def __init__(self, **kwargs):
        pass
    def scroll(self):
        pass
class DeckViewer(SmartMenu):

    def __init__(self,**kwargs):
        super(DeckViewer, self).__init__(**kwargs)
        cards = []
        i = 0
        x = 200
        carousel = Carousel(direction='right',pos = [-80,100],size =[480,270],loop = True)
        for _ in range(20):
            card = Card(source = 'card.png',allow_stretch = True,card_num = x)
            card.bind(on_release = self.change)
            card.bind(on_touch_down = self.fade)
            cards.append(card)
            carousel.add_widget(card)
            #self.add_widget(card)
            i+=1
            x-=10
            
        self.add_widget(carousel)
        tmpBtn = MyButton(text = 'Back')
        tmpBtn.size = (80,50)
        tmpBtn.background_color = button_color
        
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(10,10)
        self.add_widget(tmpBtn)
        
        deck_name = Label(text ='demo deck' ,font_size = 24,x=Window.width*0.25,y=Window.height*0.80)
        self.add_widget(deck_name)
    def add_card(self):
        pass
    def change(self,instance):
        print("ahhhhhhhhhhhhhh")
        instance.opacity = 1.0
    def fade(self,instance,hello):
        instance.opacity = 0.3
        
    
  
        
        
class CardCreation(SmartMenu):
#setup the menu button names
    """ 
    
    """
    buttonList = []
    def __init__(self, **kwargs):
        super(CardCreation, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
 
        self.msg = Label(text = 'Card Creation')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.35,Window.height*0.85)
        self.add_widget(self.msg)
        # Add the buttons
        tmpBtn = MyButton(text = '+')
        tmpBtn.size = (50,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(10,400)
        self.add_widget(tmpBtn)
        
        tmpBtn = MyButton(text = '?')
        tmpBtn.size = (50,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(Window.width-60,400)
        self.add_widget(tmpBtn)
        
        tmpBtn = MyButton(text = 'Back')
        tmpBtn.size = (80,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(10,10)
        self.add_widget(tmpBtn)
        
        temp_deck = Deck(pos = (20,280))
        temp_deck.bind(on_release = self.callback)
        self.add_widget(temp_deck)
    
    def on_button_release(self, *args):
        pass
 
    def callback(self,instance):
#print('The button %s is being pressed' % instance.text)
        self.buttonText = instance.text
        self.dispatch('on_button_release')

class CardCreator(Widget):
    def __init__(self, **kwargs):
        self.type = ''
        self.name = ''
        self.phrase = ''
        
class Profile(SmartMenu):
#setup the menu button names
  
    buttonList = []
    def __init__(self, **kwargs):
        super(Profile, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
 
        self.msg = Label(text = 'Profile')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.35,Window.height*0.75)
        self.add_widget(self.msg)
        
        tmpBtn = MyButton(text = 'Back')
        tmpBtn.size = (80,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = '20sp'
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(10,10)
        self.add_widget(tmpBtn)
        
        
        prof_pic = Image(source = 'cartman.jpg');
        prof_pic.pos= (Window.width/2-50,Window.height*0.55)
        prof_pic.size = (100,100)
        self.add_widget(prof_pic);
class Settings(SmartMenu):
#setup the menu button names
    """ 
    This is a start menu class. It inherits from the Smart Menu Class. 
    
    """
    buttonList = ["How to Play","Audio","Contact","About"]
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
 
        self.msg = Label(text = 'Settings')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.35,Window.height*0.75)
        self.add_widget(self.msg)
        # Add the buttons
        
        tmpBtn = MyButton(text = 'Back')
        tmpBtn.size = (80,50)
        tmpBtn.background_color = button_color
        tmpBtn.font_size = 20
        tmpBtn.bind(on_release = self.callback)
        tmpBtn.pos=(10,10)
        self.add_widget(tmpBtn)  
        
class MyApp(App):

    def build(self):
        self.title = "CLEVER, CRUEL, OR CRAZY"
        self.parent = Widget()
        
        self.sm = StartMenu()
        self.sm.buildUp()
        self.cc = CardCreation()
        self.cc.buildUp()
        self.p = Profile()
        self.p.buildUp()
        self.s = Settings()
        self.s.buildUp()
        self.dv = DeckViewer()
        #Begin by adding the start menu widget
        self.parent.add_widget(self.sm)
        def check_button(obj):
            "When a button is pressed in main menu screen this class checks the button that was pressed and acts appropriately"
            print(self.sm.buttonText + "yo")
            if self.sm.buttonText == 'Card Creation':
                self.parent.remove_widget(self.sm)
                self.parent.add_widget(self.cc)
            if self.sm.buttonText == 'p':
                self.parent.remove_widget(self.sm)
                self.parent.add_widget(self.p)
            if self.sm.buttonText == '?':
                self.parent.remove_widget(self.sm)
                self.parent.add_widget(self.s)
        def check_card_creation(obj):
            print(self.cc.buttonText + "yo")
            if self.cc.buttonText == 'Back':
                self.parent.remove_widget(self.cc)
                self.parent.add_widget(self.sm)
            if self.cc.buttonText == 'Demo':
                self.parent.remove_widget(self.cc)
                self.parent.add_widget(self.dv)
        def check_profile(obj):
            print(self.p.buttonText + "yo")
            if self.p.buttonText == 'Back':
                self.parent.remove_widget(self.p)
                self.parent.add_widget(self.sm)
        def check_settings(obj):
            print(self.s.buttonText + "yo")
            if self.s.buttonText == 'Back':
                self.parent.remove_widget(self.s)
                self.parent.add_widget(self.sm)
        def check_deck_viewer(obj):
            print(self.dv.buttonText)
            if self.dv.buttonText == 'Back':
                self.parent.remove_widget(self.dv)
                self.parent.add_widget(self.cc)
        self.sm.bind(on_button_release = check_button)
        self.cc.bind(on_button_release = check_card_creation)
        self.p.bind(on_button_release = check_profile)
        self.s.bind(on_button_release = check_settings)
        self.dv.bind(on_button_release = check_deck_viewer)
        return self.parent


if __name__ == '__main__':
    Config.set('graphics','resizable',0);
    Config.set('graphics', 'height', '470');
    Config.set('graphics', 'width', '320');
    Config.write()
    MyApp().run()