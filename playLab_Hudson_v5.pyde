import math
import random
from behaviors import *
from programs import *
from slider import *

#active map area
mapX = 1300
mapY = 750

import math

class Agent(object):
    type = ('high', 'low', 'tourist')
    agentColors = (color(145, 204, 130), color(1, 153, 154), color(243, 123, 128))

    def __init__(self):
        self.position = [random.randrange(extent[0],extent[2]), random.randrange(extent[1],extent[3])]
        self.speed = 2
        self.direction = random.random() * 2.0 * math.pi
        self.turnrate = 0
        
        #assign identity
        chance = random.random()
        if chance < high:
            identity = 0
        elif chance < low+high:
            identity = 1
        else:
            identity = 2
            
        self.agentColor = Agent.agentColors[identity]
        self.type = Agent.type[identity]
        self.id = identity
       
        
    def move(self):
        global allagents, behaviors
        state = {}
        state2 = {}
        state3 = {}        
        
        for agent in allagents:
            for behavior in behaviors:
                if agent.id == 0:
                    behavior.setup(self, agent, high_attraction, state)
                elif agent.id == 1:
                    behavior.setup(self, agent, low_attraction, state2)
                else:
                    behavior.setup(self, agent, tourist_attraction, state3)
                
        for behavior in behaviors:
            if self.id == 0:
                s = state
            elif self.id == 1:
                s = state2    
            else:
                s = state3
            strokeWeight(1)
            behavior.apply(self, s)
            stroke(self.agentColor)
            if toggleView == 1:
                behavior.draw(self, s)
        
    def draw(self):
        pushMatrix()

        translate(*self.position)
        rotate(self.direction)
        #draw people here
        stroke(self.agentColor)
        fill(self.agentColor)
        ellipse(0,0,9,9)
        noFill()
        strokeWeight(2)
        arc(0,0,20,20, 0.75*PI, PI/2+0.75*PI)
        fill(150)
        textSize(20)
        
        popMatrix()

#create Program classes
p1_seating = Program(seating)
p2_bikeShare = Program(bikeShare)
p3_art = Program(art)
p4_communityCenter = Program(communityCenter)
p5_plaza = Program(plaza)
p6_library = Program(library)
p7_restaurant = Program(restaurant)
p8_groceryStore = Program(groceryStore)
p9_recreation = Program(recreation)

programlist = [p1_seating,
            p2_bikeShare,
            p3_art,
            p4_communityCenter,
            p5_plaza,
            p6_library,
            p7_restaurant,
            p8_groceryStore,
            p9_recreation,
            ]
    
#button functions [text label, image file, background color, population color]
left = ["", "left.png"]
slider = ["", "slider.png"]
right = ["", "right.png"]
trash = ["TRASH", "box.png"]
reset = ["RESET", "reset.png"]
create = ["", "create.png"]
view = ["VIEW", "view.png"]

#button class
class Button(object):
    def __init__(self, bSize, bX, bY):
        self.bSize = bSize
        self.bX = bX
        self.bY = bY        
        
    def display(self, function):
        global mouseOver
        self.function = function
        self.bText = function[0]
        self.bImg = loadImage(function[1])
        
        if (mouseX > self.bX 
            and mouseX < self.bX + self.bSize
            and mouseY > self.bY 
            and mouseY < self.bY + self.bSize):
            mouseOver = True
        else:
            mouseOver = False
        if mouseOver == True:
            tint(200)
        image(self.bImg, self.bX, self.bY, self.bSize, self.bSize)
        fill(0)
        textAlign(CENTER)
        text(self.bText, self.bX+self.bSize/2, self.bY+self.bSize+20)
        noTint()

#create buttons
buttonTime = Button(50, 1375, 270)
buttonView = Button(50, 1475, 270)
buttonTrash = Button(80, 1350, 780)
buttonReset = Button(80, 1475, 780)
buttonCreate = Button(150, 1375, 460)

#create sliders
sliderCost = Slider(1365, 600, 180, 20, "COST")
sliderNecc = Slider(1365, 660, 180, 20, "NECCESSITY")
sliderFreq = Slider(1365, 720, 180, 20, "FREQUENCY")

def setup():
    size(1600, 900)
    frameRate(30)
    cursor(HAND)
    bold = loadFont("YuGothicUI-Bold-60.vlw")
    textFont(bold)
    
    #simulation extent    
    global extent, behaviors, population, allagents
    global high_count, low_count, tourist_count, high, low, tourist
    global attraction, high_attraction, low_attraction, tourist_attraction
    global imgPlayLab, toggleTime, toggleView, textDay, timeDay, timeNight, dayBlocks, dayBldgs, nightBldgs, nightBlocks
    global sumCost, sumNecc, sumFreq
    
    extent = [ 0, 0, mapX, mapY]
    
    # How many agent you want in the simulation.
    number_of_people = 50
    
    # Set population demographics
    sumCost = 0
    sumNecc = 0
    sumFreq = 0
    
    high_count = 0
    low_count = 0
    tourist_count = 0
    
    population = [["RESIDENT, HIGH INCOME", 145, 204, 130], #high
              ["RESIDENT, LOW INCOME", 1, 153, 154], #low
              ["VISITOR", 243, 123, 128] #tourist
              ]
    
    high = 0.3
    low = 0.3
    tourist = 0.4
    
    high_attraction = [p1_seating, p2_bikeShare, p3_art, p5_plaza, p6_library, p7_restaurant, p8_groceryStore, p9_recreation]
    low_attraction = [p1_seating, p2_bikeShare, p4_communityCenter, p8_groceryStore, p9_recreation]
    tourist_attraction = [p1_seating, p2_bikeShare, p3_art]
    
    # Add all the agent behaviors and their parameters.
    behaviors = (
        MoveTowardsAttraction(threshold=200.0, speedfactor=1.0, weight=60.0), 
        Swim(speedlimit=10.0, turnratelimit=math.pi / 20.0)
        )
            
    # Make some agents!
    population_count = 0
    allagents = []
    for i in xrange(0, number_of_people):
        allagents.append(Agent())
        
    for agent in allagents:
        if agent.id == 0:
            high_count += 1
        elif agent.id == 1:
            low_count += 1
        elif agent.id == 2:
            tourist_count += 1
        population_count += 1
    
    #button functions [text label, image file, background color, population color]
    dayBlocks = loadImage("day_blocks.png")
    dayBldgs = loadImage("day_bldgs.png")
    nightBlocks = loadImage("night_blocks.png")
    nightBldgs = loadImage("night_bldgs.png")
    timeDay = ["DAY", "day.png", 255, 0, dayBlocks, dayBldgs]
    timeNight = ["NIGHT", "night.png", 50, 255, nightBlocks, nightBldgs]
    toggleTime = timeDay
    toggleView = -1
     
    #sidebar
    imgPlayLab = loadImage("playLab.Hudson.png")
    

def draw():
    global high_count, low_count, tourist_count, sumCost, sumNecc, sumFreq
    noStroke()
    background(toggleTime[2])
    image(toggleTime[4], 0, 0, mapX, mapY)
    stroke(toggleTime[3])
    strokeWeight(1)
    #buildings img
    image(toggleTime[5], 0, 0, mapX, mapY)
    
    #mouse location
    if mouseX < mapX and mouseY < mapY:
        line(0, mouseY, mapX, mouseY)
        line(mouseX, 0, mouseX, mapY)

    #regenerate agents    
    for agent in allagents:
        agent.move()
        agent.draw()
        if (agent.position[0] > extent[2] or agent.position[0] < 0 
            or agent.position[1] > extent[3] or agent.position[1] < 0):
            if agent.id == 0:
                high_count -= 1
            elif agent.id == 1:
                low_count -= 1
            elif agent.id == 2:
                tourist_count -= 1
            
            allagents.pop(allagents.index(agent))
            newAgent = Agent()
            allagents.append(newAgent)
            
            if newAgent.id == 0:
                high_count += 1
            elif newAgent.id == 1:
                low_count += 1
            elif newAgent.id == 2:
                tourist_count += 1    
                                                
    #navbar
    fill(255,255,255)
    stroke(0)
    noStroke()
    strokeWeight(3)
    textSize(16)
    rect(0, mapY, mapX, 150)
    
    #status bar
    rect(0, 0, mapX, 80)
   
    #sidebar
    rect(mapX, 0, 300, height)
    rect(0,0, 50, height)
    
    #map frame
    stroke(0)
    strokeWeight(2)
    noFill()
    rect(50,80,mapX-50,mapY-80)
    
    #sidebar objects
    image(imgPlayLab, 1350, 10, 200, 67)
    
    #program creator
    stroke(0)
    fill(250)
    strokeWeight(3)
    rect(1375,350,150,150)
    
    #display buttons
    buttonTime.display(toggleTime)
    buttonView.display(view)
    buttonTrash.display(trash)
    buttonReset.display(reset)
    buttonCreate.display(create)
    
    #display sliders
    sliderCost.display()
    sliderNecc.display()
    sliderFreq.display()  
    
    #sidebar people counter
    sbOffset = 60
    sbOrigin = 110
    sbLength = 180
    population[0].append(high_count)
    population[1].append(low_count)
    population[2].append(tourist_count)
    total_population = high_count + low_count + tourist_count
    
    for p in range (0,3):
        textSize(18)
        textAlign(LEFT)
        noStroke()
        pLength = 180 * population[p][-1]/ total_population
        fill(population[p][1], population[p][2], population[p][3])
        rect(1375, sbOrigin-3 + p * sbOffset, pLength, 25)
        fill(0)
        text(population[p][0], 1350, (sbOrigin -10) + p * sbOffset)
        fill(255)
        text(population[p][-1], 1380, (sbOrigin + 15) + p * sbOffset)
        
        pushMatrix()
        translate(1360, sbOrigin + 10 + p * sbOffset)
        scale(.5)
        stroke(population[p][1], population[p][2], population[p][3])
        fill(population[p][1], population[p][2], population[p][3])
        ellipse(0,0,18,18)
        noFill()
        arc(0,0,50,50,0.75*PI, (PI/2+0.75*PI))
        popMatrix()
        
    #display programs
    p_cost = 0
    p_necc = 0
    p_freq = 0
    for program in programlist:
        program.display()
        program.hover()
        
        #activate
        if (program.position[0] < 1330 and program.position[1] < height-150):
            p_cost += program.p_cost
            p_necc += program.p_necc
            p_freq += program.p_freq            
        
        #trashcan
        if (program.position[0] > 1330 and program.position[0] < 1420
            and program.position[1] > 775 and program.position[1] < 865):
            program.xpos = program.programName[4]
            program.ypos = program.programName[5]       
    
    #status bar objects
    sumCost = "COST    " + str(p_cost)
    sumNecc = "NECCESSITY    " + str(p_necc)
    sumFreq = "FREQUENCY    " + str(p_freq)
    textAlign(LEFT)
    textSize(20)
    text(sumCost,800,50)
    text(sumNecc,950,50)
    text(sumFreq,1150,50)
    
    #global program setting
    
   
#click button toggle
def mouseClicked(): 
    global toggleTime, toggleView, slider1, slider2, slider3
    
    sliderCost.onClick()
    sliderNecc.onClick()
    sliderFreq.onClick()
    
    if (buttonTime.bX < mouseX < buttonTime.bX+buttonTime.bSize 
        and buttonTime.bY < mouseY < buttonTime.bY+buttonTime.bSize
        and toggleTime == timeDay):
        toggleTime = timeNight
    elif (buttonTime.bX < mouseX < buttonTime.bX+buttonTime.bSize
          and buttonTime.bY < mouseY < buttonTime.bY+buttonTime.bSize  
          and toggleTime == timeNight):
            toggleTime = timeDay
            
    if (buttonView.bX < mouseX < buttonView.bX+buttonView.bSize
          and buttonView.bY < mouseY < buttonView.bY+buttonView.bSize):
            toggleView = toggleView * -1
            print toggleView
            
    #create custom program
    if (buttonCreate.bX < mouseX < buttonCreate.bX+buttonCreate.bSize 
            and buttonCreate.bY < mouseY < buttonCreate.bY+buttonCreate.bSize):
        new[0] += 1
        new[6] = sliderCost.val
        new[7] = sliderNecc.val
        new[8] = sliderFreq.val
        newList = Program(new)
        programlist.append(newList)
        high_attraction.append(newList)
        low_attraction.append(newList)
        tourist_attraction.append(newList)           
        
    #reset
    if (buttonReset.bX < mouseX < buttonReset.bX+buttonReset.bSize
            and buttonReset.bY < mouseY < buttonReset.bY+buttonReset.bSize):
        print 'button'
        for program in programlist:
            program.xpos = program.programName[4]
            program.ypos = program.programName[5]
