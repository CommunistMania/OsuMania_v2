class Slider:
    def __init__(self, row, duration, game):
        self.row = row
        self.d =  duration
        self.game = game
        self.y = 0
        self.file = ""
        self.v = self.game.scrollspeed
        self.v1 = 0
        self.hit = False
        self.miss = False
        self.k = ""
        self.d *= self.game.scrollspeed
        
        if self.row == 1:
            self.file = loadImage("ArrowLeft1.png")
        if self.row == 2:
            self.file = loadImage("ArrowDown1.png")
        if self.row == 3:
            self.file = loadImage("Arrow_UP.png")
        if self.row == 4:
            self.file = loadImage("ArrowRight1.png")
        
        
    def on_draw(self):
        if self.row == 1:
            stroke(255, 255, 255)
            strokeWeight(115)
            line(300, self.y, 300, self.y - self.d)
            image(self.file, 300, self.y, 150, 150)
            self.y += self.v
            self.d += self.v1
        if self.row == 2:
            stroke(255, 255, 255)
            strokeWeight(115)
            line(500, self.y, 500, self.y -self.d)
            image(self.file, 500, self.y, 150, 150)
            self.y += self.v
            self.d += self.v1
        if self.row == 3:
            stroke(255, 255, 255)
            strokeWeight(115)
            line(700, self.y, 700, self.y -self.d)
            image(self.file, 700, self.y, 150, 150)
            self.y += self.v
            self.d += self.v1
        if self.row == 4:
            stroke(255, 255, 255)
            strokeWeight(115)
            line(900, self.y, 900, self.y - self.d)
            image(self.file, 900, self.y, 150, 150)
            self.y += self.v
            self.d += self.v1
            
        if self.hit:
            fill(150, 242, 71)
            text("Perfect", 600, 300)
            
        if self.miss:
            fill(242, 71, 125)
            text("Miss", 600, 300)
    
    def on_update(self):
        if self.y >= 1100:
            self.miss = True
        if self.y >= 1200:
            self.game.objects.remove(self)
            self.game.combo = 0
            self.game.hp += 30
        if self.hit:
            if self.d < 0:
                self.game.objects.remove(self)
    def on_key_press(self, key):
        if 750 < self.y < 1050 and self.game.play:
            self.y = 900
            self.v = 0
            self.v1 = -self.game.scrollspeed
            self.hit = True
            self.game.combo += 1
            self.game.score += 20
            self.game.hits += 1
            self.k = key
    
    def on_key_release(self, key):
        pass
        """
        if (key == self.k and self.hit) and (self.d > 40):
            self.v = self.game.scrollspeed
            self.hit = False
            self.miss = True
        """
