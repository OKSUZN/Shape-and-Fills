import turtle as turtle

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'black'] 

# set colors for turtle
turtle.color('red', 'blue')    # Red is de lijn kleur en Blue is de fill kleur daarom dat we de komma erachter gebruiken voor ze te onderscheiden van mekaar

# set pen size
turtle.pensize(5)   # Dit veranderd de size of de lijn van je pen tijdens het tekenen 

# Fill in shape with color
turtle.begin_fill()     # Dit command begint met het inkleuren van je cirkel
turtle.circle(60)       # Dit maakt een cirkel , 60 = de grote van u cirkel
turtle.end_fill()       # Dit eindigt het inkleuren van het cirkel

turtle.penup()      # Penup = is als je u pen wilt oppakken zo teken je niet verder
turtle.forward(150) 
turtle.pendown()    # Pendown = zet de pen op het papier om verder te tekenen

turtle.color('yellow', 'black')    # Geel is de lijn kleur en black is de de kleur dat word ingekleurd in het vierkant

turtle.begin_fill()
for x in range(4):      #Range is dat hij 4x het zelfde gaat uitvoeren in dit geval , 4x forward(100) en 4x right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()   # Dit beëindigt het vullen van de figuur.

turtle.mainloop()   # Je kan ook turtle.done() gebruiken
