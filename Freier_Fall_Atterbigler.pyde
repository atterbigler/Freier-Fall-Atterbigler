planeten = ["Erde","Mond","Sonne"]                # Variable für die ausgesuchten Planeten     
g_planeten = [9.81, 1.62, 274.0]                  # Variable für die Gravitation der Planeten
s_werte = [0,0,0]                                 # Variable für die Ergebnisse
v_werte = [0,0,0]                                 # Variable für die Ergebnisse
stein = None                                      
fallen = [0,0,0,0]
auswahl = [0]

# Standardeinstellungen im Setup treffen
def setup():
    global stein                                   # Variable für das Stein-Bild festlegen
    size(500, 500)                                 # Fesntergroesse
    background(250, 250, 250)                      # Hintergrund grau
    textSize (12)
    stein = loadImage ("stein.png")                # Bild des Steines laden
    frameRate (60)                                 # FrameRate festlegen (wird spaeter angepasst)

# Funktion draw, hier spielt die FrameRate eine Rolle bezueglich der Fall-Animation
def draw ():
    ueberschriften ()                                 # Beschriftungen setzen (noch kein DROP-Button, da kein Stein gesetzt)          
    if fallen [2] > 0:                                # MouseClick ist passiert -> DROP-BUTTON gezeichnet
        fill(0,136,0)                                 # grüne Farbe
        stroke (0,0,0)
        strokeWeight (2)
        rect (395,45,75,50)                           # DROP-Button
        fill (255,255,255)
        textSize (24)
        text ("DROP", 403,75)                         # Beschriftung
    textSize (12)
    fill (0,0,0)
    if fallen[0] == 1:                                 # DROP wurde ausgelöst 
        if fallen[2] <= 350:                           # solange bis die AUfprall-Linie erreicht ist ...
            ueberschriften()                           # NEU zeichnen mit erhoehter yPos
            zeichenfunktion (fallen[1], fallen[2])     # Stein zeichnen
            fallen[2] = fallen[2] + 1                  # yPos erhoehen
        if fallen[2] == 350:                           # AUFPRALL ist passiert
            berechenfunktion (fallen[1], fallen[3])    # Berechnung inklusive Ausgabe der Daten
            fallen[0] = 0                              # Neues Steinsetzen ermöglichen - kein DROP-Button
            fallen[2] = 0                              # Hoehe auf 0 sezten

# Funktion um die Zeichnung des Steines durchzufuehren und die Fallhoehe zu berechnen und auszugeben (uebergeben wird die yPos = Hoehe)           
def zeichenfunktion(xPos, yPos):
    background(250, 250, 250)
    image (stein, 150, yPos, 40, 40)                  # Stein zeichnen
    fill (0,0,0)
    ueberschriften()
    text ((350-yPos)/5, 70, 20)                       # Fallhoehe berechnen und anzeigen -> Y-Koordinaten : 5 ergibt die Hoehe in m

# Funktion zur Berechnung der Fallzeit und der Aufprallgeschwindigkeit (uebergeben wird die yPos = Hoehe) 
def berechenfunktion (xPos, yPos):
    s_werte[auswahl[0]] = sqrt(2*((500-yPos)/10)/g_planeten[auswahl[0]])                 # Berechnung der Zeit die der Stein zum Fallen braucht unter Einbezug des jeweiligen Planeten
    v_werte[auswahl[0]] = g_planeten[auswahl[0]] * s_werte[auswahl[0]] * 3.6             # Berechnung der Aufprallgeschwindigkeit
    
    text (planeten[auswahl[0]], 150, 400)                                                # Ausgabe der berechneten Werte
    text (s_werte[auswahl[0]], 150, 430)
    text (v_werte[auswahl[0]], 150, 460)
    
# Funktion für den Mausklick
def mouseClicked(): 
    #print (mouseX, mouseY)
    if mouseY < 350 and mouseY > 50 and mouseX > 100 and mouseX < 350:                    # Abfrage zum Setzen des Steines (nur in gewissem Bereich)
        zeichenfunktion(mouseX, mouseY)
        fallen[2] = mouseY                                                                # yPos merken - DROP-Button Klick folgt noch
        fallen[3] = mouseY                                                                # zweite Variable weil sich Stein bewegt (yPos)
    if mouseX > 395 and mouseX < 460 and mouseY > 45 and mouseY < 95:                     # Abfrage für den DROP-Button
        #zeichenfunktion(mouseX, 350)
        berechenfunktion(mouseX, mouseY)                                                  # Berechnungsfunktion aufrufen, mit entsprechenden yPos (Hoehe)
        fallen[0] = 1                                                                     # Marker für DROP-Button setzen (Start der Animation)
        fallen[1] = mouseX                                                                # xPos merken
        frameRate((350-fallen[3])/(sqrt(2*((500-fallen[3])/10)/g_planeten[auswahl[0]])))  # FrameRate anpassen fuer die Fallgeschwindigkeit (Pixel durch die Falldauer ergibt die FrameRate)
        #print((350-fallen[3])/(sqrt(2*((500-fallen[3])/10)/g_planeten[auswahl[0]])))
        #print((350-fallen[3]))
        #print((sqrt(2*((500-fallen[3])/10)/g_planeten[auswahl[0]])))
        #fallen[2] = mouseY

# Funktion fuer den Tastendruck und die Zuordnung des jeweiligen Planeten
def keyPressed():
    if key == "e" or key == "E":                             # Erde
        auswahl[0] = 0
    if key == "m" or key == "M":                             # Mond
        auswahl[0] = 1
    if key == "s" or key == "S":                             # Sonne
        auswahl[0] = 2
        
# Funktion zur Ausgabe der Ueberschriften und Auswahl des Planeten                                
def ueberschriften():
    textSize(16)
    text ("E(rde), M(ond), S(onne) ", 110, 25)                # Ausgabe der Tastenbelegung
    textSize(12)
    if auswahl[0] == 0:                                       # Erde
        fill(99,184,235)                                      # blaue Ellipse
        stroke (0,0,0)
        strokeWeight (2)
        ellipse (325,45,85,50)
        fill (0,0,0)
        textSize (24)
        text (planeten[0],300,50)                              # Beschriftung "Erde"
        textSize(12)
    else:
        if auswahl[0] == 1:                                    # Mond
            fill(255,250,240)                                  # weisse Ellipse
            stroke (0,0,0)
            strokeWeight (2)
            ellipse (325,45,85,50)
            fill (0,0,0)
            textSize (24)
            text (planeten[1], 300,50)                          # Beschriftung "Mond"
            textSize(12)
        else:                                                   # Sonne
            fill(255,255,0)                                     # gelbe Ellipse
            stroke (0,0,0)
            strokeWeight (2)
            ellipse (325,45,85,50)
            fill (0,0,0)
            textSize (24)
            text (planeten[2], 298,50)                           # Beschriftung "Sonne"
            textSize(12)
    strokeWeight (2)
    line (100, 385, 250, 385)                                    # AUFPRALL-Linie
    text ("Hoehe (m)", 10, 20)                                   # Restliche Beschriftungen
    text ("Zeit (s)", 10, 430)
    text ("Geschw. (km/h)", 10, 460) 
    
