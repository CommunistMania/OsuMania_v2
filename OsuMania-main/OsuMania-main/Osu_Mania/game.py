from __future__ import division, print_function
import Note
import random
import Slider



WIDTH = 1920
HEIGHT = 1080 # height of screen in pixels

BACKGROUND_COLOR = color(30)  # (0black), 255(white)


class Window:    
    def __init__(self):
        self.pleft = loadImage("shellleft.png")
        self.pdown = loadImage("shelldown.png")
        self.pup = loadImage("shellup.png")
        self.pright = loadImage("shellright.png")
        self.notecount = 0
        self.hits = 0
        self.left = loadImage("pressleft.png")
        self.down = loadImage("pressdown.png")
        self.up = loadImage("pressup.png")
        self.right = loadImage("pressright.png")
        self.hp = 500
        self.combo = 0
        self.score = 0
        self.g = 10
        self.z = False
        self.x = False
        self.n = False
        self.m = False
        self.objects = []
        self.count = 0
        self.hit = False
        #for x in range(300):
            #self.objects.append(Note.Note(1, x, self))
        self.menu = True
        self.select = False
        self.play = False
        self.endscreen = False
        self.fail = False
        self.difficulty = ""
        self.Background = loadImage("Menu2.png")
        self.Sora = loadImage("Sora.png")
        self.Sorasize = 600
        self.go = True
        self.kb1 = "z"
        self.kb2 = "x"
        self.kb3 = "."
        self.kb4 = "/"
        self.msg = "Keybinds"
        self.kbc1 = False
        self.kbc2 = False
        self.kbc3 = False
        self.kbc4 = False
        self.maxcombo = 0
        self.j = []
        self.i = []
        self.scrollspeed = 50
        
        with open("Helblinde - Heaven's Fall (Kaito-kun) [Hard].osu.txt") as file:
            u=[]
            for row in file:
                row = row.strip()
                self.j = row.split(",")
                for c in range(len(self.j)):
                    self.j[c] = self.j[c]
                self.j[2] = float(self.j[2])
                self.j[2] = self.j[2] / 50
                u = self.j[5].split(":")
                self.j[5]=int(u[0])
                self.j[5] /= 50
                self.j[2] = int(self.j[2])
                self.j[5] = int(self.j[5])
                self.i.append(self.j)
            print(self.i)
        
        
    def reset(self):
        self.endscreen = False
        self.fail = False
        self.hp = 500
        self.count = 0
        self.notes = []
        self.difficulty = ""
        self.go = False
        self.notecount = 0
        self.hits = 0
        self.score = 0
        self.combo = 0
        self.maxcombo = 0
        
    def on_draw(self):
        if self.play:
            self.count += 1
            if self.difficulty == "easy":
                fill(76, 216, 204)
                noStroke()
                rect(0, 20, self.count / 2, 30, 30)
                if self.count / 2 > 1200:
                    self.go = False
                    if self.count / 2 > 1300:
                        self.play = False
                        self.endscreen = True
            
            if self.difficulty == "hard":
                fill(76, 216, 204)
                noStroke()
                rect(0, 20, self.count / 3, 30, 30)
                if self.count / 3 > 12000:
                    self.go = False
                    if self.count / 3 > 13000:
                        self.play = False
                        self.endscreen = True
                
            a = 0
            b = 0
            
            fill(115, 240, 252)
            textSize(20)
            text("HP", 1005, 470)
            noStroke()
            rect(1000, self.hp, 1010, 900, 30)
            self.hp -= 0.2
            if self.hp < 500:
                self.hp = 500
            if self.hp > 900:
                self.hp = 900
                self.play = False
                self.fail = True
            
            fill(255, 255, 255)
            textSize(30)
            text(self.combo, 600, 200)
            text(frameRate, 200, 200)
            text(self.score, 200, 300)
            text(self.count, 200, 400)
            
            image(self.left, 300, 900, 150, 150)
            image(self.down, 500, 900, 150, 150)
            image(self.up, 700, 900, 150, 150)
            image(self.right, 900, 900, 150, 150)
            
            if self.z:
                image(self.pleft, 300, 900, 150, 150)
            if self.x:
                image(self.pdown, 500, 900, 150, 150)
            if self.n:
                image(self.pup, 700, 900, 150, 150)
            if self.m:
                image(self.pright, 900, 900, 150, 150)
            
            if self.difficulty == "easy" and self.go:
                if self.notecount > 0:
                    text(float((self.hits/self.notecount)*100), 200, 250)
                if self.count % random.randrange(10, 40, 20) == 0:
                    a = random.randint(1, 5)
                    self.objects.append(Note.Note(a, 1, self))
                    self.notecount += 1
            
            if self.difficulty == "hard" and self.go:
                self.j = []
                for n in self.i:
                    self.j = n
                    if self.count - 0.2 < self.j[2] < self.count + 0.2:
                        if 0 <= float(self.j[0]) < 127:
                            if int(self.j[3]) == 1:
                                self.objects.append(Note.Note(1, 1, self))
                            else:
                                self.objects.append(Slider.Slider(1, int(self.j[5])-self.count, self))
                            #break
                        if 128 <= float(self.j[0]) < 255:
                            if int(self.j[3]) == 1:
                                self.objects.append(Note.Note(2, 1, self))
                            else:
                                self.objects.append(Slider.Slider(2, int(self.j[5])-self.count, self))
                            #break
                        if 256 <= float(self.j[0]) < 383:
                            if int(self.j[3]) == 1:
                                self.objects.append(Note.Note(3, 1, self))
                            else:
                                self.objects.append(Slider.Slider(3, int(self.j[5])-self.count, self))
                            #break
                        if 384 <= float(self.j[0]) < 511:
                            if int(self.j[3]) == 1:
                                self.objects.append(Note.Note(4, 1, self))
                            else:
                                self.objects.append(Slider.Slider(4, int(self.j[5])-self.count, self))
                            #break
                            
                """
                if self.notecount > 0:
                    text(float((self.hits/(self.notecount))*100), 200, 250)
                if self.count % random.randrange(10, 40, 20) == 0:
                    a = random.randint(1, 5)
                    self.objects.append(Note.Note(a, 1, self))
                    #self.objects.append(Slider.Slider(a, random.randint(50, 200), self))
                    self.notecount += 1
                    
                    b = random.randint(1, 5)
                    if b == a:
                        if b == 4:
                            b = random.randint(1, 3)
                        else:
                            b += 1
                    if self.count % random.randrange(30, 80, 20) == 0:
                        self.objects.append(Slider.Slider(b, random.randint(50, 200), self))
                        self.notecount += 1
                """
                
        
                
            #if self.count % random.randint(10, 31) == 0:
                #self.objects.append(Note.Note(random.randint(1, 5), 1, self))
            
            for notes in self.objects:
                notes.on_draw()
                
        if self.menu:
            image(self.Background, 960, 540)
            image(self.Sora, 650, 540, self.Sorasize, self.Sorasize)
            textSize(60)
            text("Click the Circle!", 650, 100)
            textSize(50)
            self.Sorasize -= 2
            if self.Sorasize < 580:
                self.Sorasize = 600
                
        if self.select:
            textSize(60)
            fill(255, 255, 255)
            text("Select a difficulty", 650, 100)
            textSize(50)
            
            noStroke()
            fill(255, 255, 255)
            rect(300, 200, 600, 300, 30)
            fill(10, 165, 73)
            rect(305, 205, 595, 295, 25)
            fill(255, 255, 255)
            text("Easy", 450, 245)
            
            noStroke()
            fill(255, 255, 255)
            rect(700, 200, 1000, 300, 30)
            fill(165, 10, 93)
            rect(705, 205, 995, 295, 25)
            fill(255, 255, 255)
            text("Hard", 850, 245)
            
            text(self.msg, 650, 700)
            
            text(self.kb1, 500, 800)
            image(self.left, 500, 900, 50, 50)
            text(self.kb2, 600, 800)
            image(self.down, 600, 900, 50, 50)
            text(self.kb3, 700, 800)
            image(self.up, 700, 900, 50, 50)
            text(self.kb4, 800, 800)
            image(self.right, 800, 900, 50, 50)
            
            if 475 < mouseX < 525 and 800 < mouseY < 900:
                fill(255, 255, 255, 100)
                rect(475, 790, 525, 930)
                
            if 575 < mouseX < 625 and 800 < mouseY < 900:
                fill(255, 255, 255, 100)
                rect(575, 790, 625, 930)
                
            if 675 < mouseX < 725 and 800 < mouseY < 900:
                fill(255, 255, 255, 100)
                rect(675, 790, 725, 930)
                
            if 775 < mouseX < 825 and 800 < mouseY < 900:
                fill(255, 255, 255, 100)
                rect(775, 790, 825, 930)
                
        if self.endscreen:
            textSize(60)
            text("Score: "+str(self.score), 300, 300)
            text("Max Combo: "+str(self.maxcombo), 300, 500)
            textSize(30)
            fill(98, 218, 250)
            rect(25, 50, 150, 50+75, 30)
            fill(39, 77, 88)
            rect(30, 55, 145, 45+75, 25)
            fill(255, 255, 255)
            text("Back", 85, 50+35)
            
        if self.fail:
            textSize(60)
            text("You Failed!", 300, 300)
            textSize(30)
            fill(98, 218, 250)
            rect(25, 50, 150, 50+75, 30)
            fill(39, 77, 88)
            rect(30, 55, 145, 45+75, 25)
            fill(255, 255, 255)
            text("Back", 85, 50+35)
                
        
    def on_update(self):
        for notes in self.objects:
            notes.on_update()
            
        if self.combo > self.maxcombo:
                self.maxcombo = self.combo

        
        
    def on_key_press(self, key):
        for notes in self.objects:
            notes.on_key_press(key)
        if self.play:
            if key == self.kb1:
                self.z = True
            if key == self.kb2:
                self.x = True
            if key == self.kb3:
                self.n = True
            if key == self.kb4:
                self.m = True
        if self.select:
            if self.kbc1:
                self.kb1 = key
                self.msg = "Keybinds"
                self.kbc1 = False
                self.kbc2 = False
                self.kbc3 = False
                self.kbc4 = False
            
            if self.kbc2:
                self.kb2 = key
                self.msg = "Keybinds"
                self.kbc1 = False
                self.kbc2 = False
                self.kbc3 = False
                self.kbc4 = False
            
            if self.kbc3:
                self.kb3 = key
                self.msg = "Keybinds"
                self.kbc1 = False
                self.kbc2 = False
                self.kbc3 = False
                self.kbc4 = False
                
            if self.kbc4:
                self.kb4 = key
                self.msg = "Keybinds"
                self.kbc1 = False
                self.kbc2 = False
                self.kbc3 = False
                self.kbc4 = False
            
            
    def on_key_release(self, key):
        for notes in self.objects:
            notes.on_key_release(key)
        if self.play:
            if key == self.kb1:
                self.z = False
            if key == self.kb2:
                self.x = False
            if key == self.kb3:
                self.n = False
            if key == self.kb4:
                self.m = False
            
    def on_mouse_clicked(self, mouseX, mouseY):
        if 300 < mouseX < 900 and 240 < mouseY < 840 and self.menu:
            self.menu = False
            self.select = True
            
        if 300 < mouseX < 600 and 200 < mouseY < 300 and self.select:
            self.difficulty = "easy"
            self.menu = False
            self.play = True
            self.select = False
            self.notes = []
            self.count = 0
            self.notecount = 0
            self.hits = 0
            self.go = True
            
        if 700 < mouseX < 1000 and 200 < mouseY < 300 and self.select:
            self.difficulty = "hard"
            self.menu = False
            self.play = True
            self.select = False
            self.notes = []
            self.count = 0
            self.notecount = 0
            self.hits = 0
            self.go = True
            self.hp = 500
        if 475 < mouseX < 525 and 800 < mouseY < 900 and self.select:
            self.kbc1 = True
            self.msg = "Enter a new bind"
            
        if 575 < mouseX < 625 and 800 < mouseY < 900 and self.select:
            self.kbc2 = True
            self.msg = "Enter a new bind"
        
        if 675 < mouseX < 725 and 800 < mouseY < 900 and self.select:
            self.kbc3 = True
            self.msg = "Enter a new bind"
            
        if 775 < mouseX < 825 and 800 < mouseY < 900 and self.select:
            self.kbc4 = True
            self.msg = "Enter a new bind"
            
        if 25 < mouseX < 150 and 50 < mouseY < 50+75 and (self.endscreen or self.fail):
            self.reset()
            self.select = True
            self.menu = False
            self.endscreen = False
            self.fail = False
            
            
        
        
