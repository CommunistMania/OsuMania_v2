class Note:
    def __init__(self, row, time, game):
        self.row = row
        self.time = time
        self.game = game
        self.y = 0
        self.file = ""
        self.hit = False
        self.miss = False
        self.count = 10
        
        if self.row == 1:
            self.file = loadImage("ArrowLeft1.png")
        if self.row == 2:
            self.file = loadImage("ArrowDown2.png")
        if self.row == 3:
            self.file = loadImage("ArrowUp2.png")
        if self.row == 4:
            self.file = loadImage("ArrowRight1.png")
        
        
    def on_draw(self):
        if self.row == 1 and self.hit == False:
            image(self.file, 300, self.y, 150, 150)
            self.y += self.game.scrollspeed
        if self.row == 2 and self.hit == False:
            image(self.file, 500, self.y, 150, 150)
            self.y += self.game.scrollspeed
        if self.row == 3 and self.hit == False:
            image(self.file, 700, self.y, 150, 150)
            self.y += self.game.scrollspeed
        if self.row == 4 and self.hit == False:
            image(self.file, 900, self.y, 150, 150)
            self.y += self.game.scrollspeed
            
            
        
        if self.hit:
            self.count -= 1
            fill(150, 242, 71)
            text("Perfect", 600, 300)
            if self.count < 0:
                self.game.objects.remove(self)
                
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
            
    def on_key_press(self, key):
        if 750 < self.y < 1050 and self.game.play:
            self.hit = True
            self.game.combo += 1
            self.game.score += 10
            self.game.hits += 1
    def on_key_release(self, key):
        pass
    
        
