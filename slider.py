#slider class
class Slider(object):
    def __init__(self, sX, sY, sLen, sHeight, sName):
        self.sX = sX
        self.sY = sY
        self.sLen = sLen
        self.sHeight = sHeight
        self.val = 5
        self.mouseOver_left = False
        self.mouseOver_right = False
        self.sName = sName
        
    def display(self):
        stroke(0)
        strokeWeight(3)
        fill(255)
        rect(self.sX, self.sY, self.sLen, self.sHeight)
        
        if (self.sX-25 < mouseX < self.sX-10) and (self.sY < mouseY < self.sY+self.sHeight):
            fill(200)
            self.mouseOver_left = True
        else:
            fill(255)
            self.mouseOver_left = False
        triangle(self.sX-10, self.sY, self.sX-10, self.sY+self.sHeight, self.sX-25, self.sY+self.sHeight/2)
    
        if (self.sX+self.sLen+10 < mouseX < self.sX+self.sLen+25) and (self.sY < mouseY < self.sY+self.sHeight):
            fill(200)
            self.mouseOver_right = True
        else:
            fill(255)
            self.mouseOver_right = False
        triangle(self.sX+self.sLen+10, self.sY, self.sX+self.sLen+10, self.sY+self.sHeight, self.sX+self.sLen+25, self.sY+self.sHeight/2)    
        
        fill(180)
        rect(self.sX, self.sY, self.sLen*(self.val/10.0), self.sHeight)
        fill(0)
        textSize(18)
        textAlign(LEFT)  
        value = '['+str(self.val)+']'
        fill(0)
        text(self.sName+' '+value, self.sX, self.sY-10)
    
    def onClick(self):
        if self.mouseOver_left == True:
            if self.val > 0:
                self.val -= 1
        elif self.mouseOver_right == True:
            if self.val < 10:
                self.val += 1
