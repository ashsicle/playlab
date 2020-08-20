def setup(): 
    size(800, 800)
    background(55)
    
    global pg
    

def draw(): 
    fill(255)
    
    pg.beginDraw()

    #pg.background(102)
    if (mousePressed == True):
        stroke(0)
        pg.line(mouseX,mouseY, pmouseX, pmouseY)
    pg.stroke(0)
    #pg.line(pg.width*0.5, pg.height*0.5, mouseX, mouseY)
    pg.endDraw()
    image(pg, 50, 50)
