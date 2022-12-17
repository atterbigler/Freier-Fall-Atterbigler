planeten = ["Erde","Mond","Sonne"]
g_planeten = [9.81, 1.62, 274.0]
s_werte = [0,0,0]
v_werte = [0,0,0]
stein = None
counter = 1

def setup():
    global stein
    size(500, 500)
    background(250, 250, 250)  
    textSize (12)

    stein = loadImage ("stein.png")
    #image (stein, 100, 100, 40, 40)
    ueberschriften ()
    

def draw ():
    ueberschriften ()
    fill(0,136,0)
    stroke (0,0,0)
    strokeWeight (2)
    rect (395,45,75,50)
    fill (255,255,255)
    textSize (24)
    text ("DROP", 403,75)
    textSize (12)
    fill (0,0,0)
    
def zeichenfunktion(xPos, yPos):
    background(250, 250, 250)
    #noFill()
    
    image (stein, 100, yPos, 40, 40)
    image (stein, 200, yPos, 40, 40)
    image (stein, 300, yPos, 40, 40)
    #rect (100, yPos, 40, 40, 12)
    #rect (200, yPos, 40, 40, 12)
    #rect (300, yPos, 40, 40, 12)
    fill (0,0,0)
    ueberschriften()
    text ((350-yPos)/5, 70, 20)
    
def berechenfunktion (xPos, yPos):
    for i in range (0, len(planeten),1):
        s_werte[i] = sqrt(2*((500-yPos)/10)/g_planeten[i])
        v_werte[i] = g_planeten[i] * s_werte[i] * 3.6
      
    for j in range (0, len(planeten), 1):
        text (planeten[j], (j+1)*100, 400)
        text (s_werte[j], (j+1)*100, 430)
        text (v_werte[j], (j+1)*100, 460)
        

    
def mouseClicked(): 
    if mouseY < 350 and mouseX > 100 and mouseX < 350:
        zeichenfunktion(mouseX, mouseY)
    if mouseX > 395 and mouseX < 460 and mouseY > 45 and mouseY < 95:
        zeichenfunktion(mouseX, 350)
        berechenfunktion(mouseX, mouseY)
                 
def ueberschriften():
    strokeWeight (2)
    line (100, 385, 350, 385)
    text ("Hoehe (m)", 10, 20)
    text ("Zeit (s)", 10, 430)
    text ("Geschw. (km/h)", 10, 460) 
    
