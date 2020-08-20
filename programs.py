global programlist, program, tSize

#program [text label, image file, xText, xpos, ypox, p_cost, p_necce, p_freq]
seating = [1, "SEATING", "1_seating.png", 40, 40, 765, 0, 7, 8]
bikeShare = [2,"BIKE SHARE", "2_bike-share.png", 180, 180, 765, 4, 3, 3]
art = [3,"POP-UP ART", "3_popup-art.png", 320, 320, 770, 7, 2, 1]
communityCenter = [4,"COMMUNITY CENTER", "4_community-center.png", 460, 460, 765, 0, 8, 6]
plaza = [5,"PLAZA", "5_plaza.png", 600, 600, 765, 0, 5, 7]
library = [6,"LIBRARY", "6_library.png", 740, 740, 765, 1, 5, 3]
restaurant = [7,"RESTAURANT", "7_restaurant.png", 880, 880, 765, 10, 2, 4]
groceryStore = [8,"GROCERY STORE", "8_grocery-store.png", 1020, 1020, 765, 5, 10, 5]
recreation = [9,"RECREATION", "9_basketball.png", 1160, 1160, 765, 0, 6, 6]
new = [10,"NEW PROGRAM", "10_custom.png", 5000, 1400, 370, 5, 5, 5]

class Program(object):
    def __init__(self, programName):
        self.programName = programName
        self.programId = self.programName[0]
        self.programText = self.programName[1]
        self.xText = self.programName[3]
        self.xpos = self.programName[4]
        self.ypos = self.programName[5]
        self.p_cost = self.programName[6]
        self.p_necc = self.programName[7]
        self.p_freq = self.programName[8]
        
        
        global overBox, box_size, pressed
        box_size = 100
        overBox = False
        pressed = 0
        self.position = [(self.xpos+box_size/2),(self.ypos+box_size/2)]
    
    def display(self):  # Display method
        
        global overBox, box_size, pressed
        self.programImg = loadImage(self.programName[2])
        self.position = [(self.xpos+box_size/2),(self.ypos+box_size/2)]
        
        image(self.programImg, self.xpos, self.ypos, box_size, box_size)
        textAlign(CENTER)
        textSize(15)
        fill(0)
        text(self.programText, self.xText+box_size/2, 880)    
        
    def hover(self): #hover over   
        global overBox, box_size, pressed             
        if (mouseX > self.xpos and mouseX < self.xpos + box_size
            and mouseY > self.ypos and mouseY < self.ypos + box_size):
            overBox = True
            tint(200)
            
            pushMatrix()
            if mouseX > 1300:
                if mouseY < 250:
                    translate(self.position[0]-250, self.position[1]+200)
                else:
                    translate(self.position[0]-250, self.position[1]-50)    
            else:
                if mouseY < 250:
                    translate(self.position[0]+50, self.position[1]+200)
                else:    
                    translate(self.position[0]+50, self.position[1]-50)
            
            #draw hover-over here
            stroke(0)
            strokeWeight(2)
            fill(255,255,255,200)    
            rect(0,0,200,-200)    
            fill(0)
            textAlign(LEFT)
            textSize(18)
            text(self.programText, 10, -180)
            
            textSize(15)
            text('Cost', 10, -150)
            text('Neccessity', 10, -100)
            text('Frequency', 10, -50)
            
            fill(255)
            rect(10,-130,180,-10)
            rect(10,-80,180,-10)
            rect(10,-30,180,-10)
            
            fill(100)
            rect(10, -130, self.p_cost/10.0*180, -10)
            rect(10, -80, self.p_necc/10.0*180, -10)
            rect(10, -30, self.p_freq/10.0*180, -10)
    
            popMatrix()
            
        else:
            overBox = False
            noTint()

        if mousePressed == True:
            if overBox == True:
                pressed = self.programId
                tint(100) 
                            
            if self.programId == pressed:   
                self.xpos = mouseX - (box_size/2)
                self.ypos = mouseY - (box_size/2)
        else: 
            pressed = 0 
        noTint()



        
