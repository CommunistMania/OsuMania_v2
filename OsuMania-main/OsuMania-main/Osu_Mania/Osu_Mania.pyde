# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!

from __future__ import division, print_function

#add_library("sound")
import game

window = None

def setup():
    #global sf
    #sf = SoundFile(this, "hitsound.wav")
    global window
    frameRate(120)
    size(game.WIDTH, game.HEIGHT)
    rectMode(CORNERS)
    imageMode(CENTER)
    ellipseMode(CENTER)
    #font = loadFont("ArialRoundedMTBold-48.vlw")
    #textFont(font)
    textMode(CENTER)
    textAlign(CENTER, CENTER)
    window = game.Window()
    
    
    

    

def draw():
    background(game.BACKGROUND_COLOR)
    window.on_draw()
    window.on_update()

def keyPressed():
    #sf.play()
    if key == CODED:
        window.on_key_press(keyCode)
    else:
        window.on_key_press(key)
        

def keyReleased():
    if key == CODED:
        window.on_key_release(keyCode)
    else:
        window.on_key_release(key)
        
def mouseClicked():
    window.on_mouse_clicked(mouseX, mouseY)


"""def mousePressed():
    window.on_mouse_press(mouseX, mouseY, mouseButton)
    #clicking is for noobs


def mouseReleased():
    window.on_mouse_release(mouseX, mouseY, mouseButton)
