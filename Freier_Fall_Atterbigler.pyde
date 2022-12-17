planeten = ["Erde","Mond","Sonne"]
g_planeten = [9.81, 1.62, 274.0]
s_werte = [0,0,0]
v_werte = [0,0,0]
stein = None
counter = 1
fallen = [0,0,0,0]
auswahl = [0]

def setup():
    global stein
    size(500, 500)
    background(250, 250, 250)  
    textSize (12)
    stein = loadImage ("stein.png")
    frameRate (60)
    
def draw ():
    ueberschriften ()
    
#if keyPressed:
#        if key == "e" or key == "E":
#            text("Erde", 203, 25)
#            redraw()
#        if key == "m" or key == "M":
#            text("Mond", 203, 25)
#        if key == "s" or key == "S":
#            text("Sonne", 203, 25)
    if fallen [2] > 0:
        fill(0,136,0)
        stroke (0,0,0)
        strokeWeight (2)
        rect (395,45,75,50)
        fill (255,255,255)
        textSize (24)
        text ("DROP", 403,75)
    textSize (12)
    fill (0,0,0)
    if fallen[0] == 1:
        if fallen[2] <= 350:
            ueberschriften()
            zeichenfunktion (fallen[1], fallen[2])
            fallen[2] = fallen[2] + 1
        if fallen[2] == 350:
            berechenfunktion (fallen[1], fallen[3]) 
            fallen[0] = 0
            fallen[2] = 0
       
def zeichenfunktion(xPos, yPos):
    background(250, 250, 250)
    #noFill()
    
    #image (stein, 100, yPos, 40, 40)
    image (stein, 150, yPos, 40, 40)
    #image (stein, 300, yPos, 40, 40)
    #rect (100, yPos, 40, 40, 12)
    #rect (200, yPos, 40, 40, 12)
    #rect (300, yPos, 40, 40, 12)
    fill (0,0,0)
    ueberschriften()
    text ((350-yPos)/5, 70, 20)
    
def berechenfunktion (xPos, yPos):
    s_werte[auswahl[0]] = sqrt(2*((500-yPos)/10)/g_planeten[auswahl[0]])
    v_werte[auswahl[0]] = g_planeten[auswahl[0]] * s_werte[auswahl[0]] * 3.6
    
    text (planeten[auswahl[0]], 150, 400)
    text (s_werte[auswahl[0]], 150, 430)
    text (v_werte[auswahl[0]], 150, 460)
    
#    for i in range (0, len(planeten),1):
#        s_werte[i] = sqrt(2*((500-yPos)/10)/g_planeten[i])
#        v_werte[i] = g_planeten[i] * s_werte[i] * 3.6
      
#    for j in range (0, len(planeten), 1):
#        text (planeten[j], (j+1)*100, 400)
#        text (s_werte[j], (j+1)*100, 430)
#        text (v_werte[j], (j+1)*100, 460)
        

    
def mouseClicked(): 
    print (mouseX, mouseY)
    if mouseY < 350 and mouseY > 50 and mouseX > 100 and mouseX < 350:
        zeichenfunktion(mouseX, mouseY)
        fallen[2] = mouseY
        fallen[3] = mouseY
    if mouseX > 395 and mouseX < 460 and mouseY > 45 and mouseY < 95:
        #zeichenfunktion(mouseX, 350)
        berechenfunktion(mouseX, mouseY)
        fallen[0] = 1
        fallen[1] = mouseX
        frameRate((350-fallen[3])/(sqrt(2*((500-fallen[3])/10)/g_planeten[auswahl[0]])))
        print((350-fallen[3])/(sqrt(2*((500-fallen[3])/10)/g_planeten[auswahl[0]])))
        print((350-fallen[3]))
        print((sqrt(2*((500-fallen[3])/10)/g_planeten[auswahl[0]])))
        #fallen[2] = mouseY

def keyPressed():
    if key == "e" or key == "E":
        auswahl[0] = 0
    if key == "m" or key == "M":
        auswahl[0] = 1
    if key == "s" or key == "S":
        auswahl[0] = 2
        
                 
def ueberschriften():
    textSize(16)
    text ("E(rde), M(ond), S(onne) ", 110, 25)
    textSize(12)
    if auswahl[0] == 0:
        fill(99,184,235)
        stroke (0,0,0)
        strokeWeight (2)
        ellipse (325,45,85,50)
        fill (0,0,0)
        textSize (24)
        text (planeten[0],300,50)
        textSize(12)
    else:
        if auswahl[0] == 1:
            fill(255,250,240)
            stroke (0,0,0)
            strokeWeight (2)
            ellipse (325,45,85,50)
            fill (0,0,0)
            textSize (24)
            text (planeten[1], 300,50)
            textSize(12)
        else:
            fill(255,255,0)
            stroke (0,0,0)
            strokeWeight (2)
            ellipse (325,45,85,50)
            fill (0,0,0)
            textSize (24)
            text (planeten[2], 298,50)
            textSize(12)
    strokeWeight (2)
    line (100, 385, 350, 385)
    text ("Hoehe (m)", 10, 20)
    text ("Zeit (s)", 10, 430)
    text ("Geschw. (km/h)", 10, 460) 
    
