import turtle  # Turtle Library
import time  # Time Library
import keyboard  # Keyboad Library
import re  # Re Library
from tkinter import *  # TK Library
import tkinter as tk
import calendar  # Calendar Library
import datetime  # Datetime Library

# Overall Refrences:
# Python Documentation https://docs.python.org/3/library/turtle.html
# Hex Color Codes from https://htmlcolorcodes.com/
# Planet colors referenced from https://spaceplace.nasa.gov/gallery-solar-system/en/
# Orbit data https://people.southwestern.edu/~kamenm/auburn/w00harris.html
# Turtle.write() - https://www.geeksforgeeks.org/turtle-write-function-in-python/
# Metomatics https://pypi.org/project/meteomatics/
# pythontime documentation https://docs.python.org/3/library/time.html#functions
# Start date - aligning of planets
# https://www.sciencefocus.com/space/do-the-planets-ever-align-with-one-another/#:~:text=Because%20of%20the%20orientation%20and,again%20until%206%20May%202492.


def may6():
    global starttime
    starttime = 16483651200
    root.destroy()


root = tk.Tk()
# All info for Tkinter I learned on my own time and decided to add into the program, the tutorial I used is
root.title("Solar System")
buttonhit = False  # https://www.youtube.com/watch?v=YXPyB4XeYLA
# Tkinter documentation https://docs.python.org/3/library/tk.html
root.configure(bg='#414143')
starttime = 0


yearq = Label(root, text='Year:', bg='#414143', fg='#FFFFFF')
yearq.grid(row=1, column=1)
year = Entry(root, width=10)
year.grid(row=1, column=2)
monthq = Label(root, text='Month:', bg='#414143', fg='#FFFFFF')
monthq.grid(row=1, column=3)
month = Entry(root, width=10)
month.grid(row=1, column=4)
dayq = Label(root, text='Day:', bg='#414143', fg='#FFFFFF')
dayq.grid(row=1, column=5)
day = Entry(root, width=10)
day.grid(row=1, column=6)
epochl = Label(root, text='Unix Epoch Timecode:', bg='#414143', fg='#FFFFFF')
epochl.grid(row=3, column=3, columnspan=2)
beginallign = Button(root, text='Begin At Solar Allignment',
                     command=may6, bg='#000000', fg='#FFFFFF')
beginallign.grid(row=9, column=1, columnspan=6)
alligndate = Label(root, text='(6 May 2492)', bg='#414143', fg='#FFFFFF')
alligndate.grid(row=10, column=1, columnspan=6)


def destroy():
    root.destroy()


def Continue():
    global buttonhit  # https://thispointer.com/python-how-to-use-global-variables-in-a-function/
    buttonhit = True
    if buttonhit == True:
        daya = int(day.get())
        montha = int(month.get())
        yeara = int(year.get())
        dateunixepoch = datetime.datetime(yeara, montha, daya)
        epochtime = Label(root, text=str(
            (calendar.timegm(dateunixepoch.timetuple()))), bg='#414143', fg='#FFFFFF')
        epochtime.grid(row=4, column=1, columnspan=6)
        beginsolar = Button(root, text='Begin Solar System',
                            command=destroy, bg='#000000', fg='#FFFFFF')
        beginsolar.grid(row=5, column=1, columnspan=6)
        warning = Label(
            root, text='This will cause the simulation to run very slowly due to the calculations taking a longer time', bg='#414143', fg='#FFFFFF')
        warning.grid(row=6, column=1, columnspan=6)
        warning2 = Label(
            root, text='Main purpose is to show planet positions at given date', bg='#414143', fg='#FFFFFF')
        warning2.grid(row=7, column=1, columnspan=6)
        spacer = Label(root, bg='#414143', fg='#FFFFFF')
        spacer.grid(row=8, column=1, columnspan=6)
        global starttime
        starttime = calendar.timegm(dateunixepoch.timetuple())

    else:
        print("Error")


submit = Button(root, text="Submit", command=Continue,
                bg='#000000', fg='#FFFFFF')
submit.grid(row=2, column=3, columnspan=2)

root.mainloop()

print("success")

# Mercury Color (#3874B1)mercury-blue, (#ECB532),mercury-orange
mercury_blue = '#3874B1'
mercury_orange = '#ECB532'
# Venus Colors (#F68232)venus-orange, (#EEDCCF)venus-white
venus_orange = '#F68232'
venus_white = '#EEDCCF'
# Earth Colors (#2260A7)earth-blue, (#D1E3F8)earth-white, (#76AF5C)earth-green
earth_blue = '#2260A7'
earth_white = '#D1E3F8'
earth_green = '#76AF5C'
# Mars Colors (#E47D65)mars-red, (#444867)mars-black
mars_red = '#E47D65'
mars_black = '#444867'
# Jupiter Colors (#E7B54F)jupiter-brown, (#F6E6C6)jupiter-white
jupiter_brown = '#E7B54F'
jupiter_white = '#F6E6C6'
# Saturn Colors (#EECA82)saturn-brown, (#FBF1DC)saturn-white
saturn_brown = '#EECA82'
saturn_white = '#FBF1DC'
# Uranus Colors (#0F7490)uranus-blue
uranus_blue = '#0F7490'
# Neptune Colors (#0779BA)neptune-blue
neptune_blue = '#0779BA'
# Sun (#FFC300)sun
sun_orange = '#FFC300'

# Creates Turtles

sc = turtle.Screen()  # -speeds up animation, looks smoother https://www.reddit.com/r/learnpython/comments/b2c2ft/turtle_graphics_speed_up_to_almost_instantaneous/
sc.tracer(0)
b = turtle.Turtle()
b.hideturtle()
b.speed(0)
s = turtle.Turtle()
s.hideturtle()
s.speed(0)
m = turtle.Turtle()
m.hideturtle()
m.speed(0)
v = turtle.Turtle()
v.hideturtle()
v.speed(0)
e = turtle.Turtle()
e.hideturtle()
e.speed(0)
a = turtle.Turtle()
a.hideturtle()
a.speed(0)
j = turtle.Turtle()
j.hideturtle()
j.speed(0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
u = turtle.Turtle()
u.hideturtle()
u.speed(0)
n = turtle.Turtle()
n.hideturtle()
n.speed(0)
w = turtle.Turtle()
w.hideturtle()
w.speed(0)
z = turtle.Turtle()
z.hideturtle()
z.speed(0)
c = turtle.Turtle()
c.hideturtle()
c.speed(0)
q = turtle.Turtle()
q.hideturtle()
q.color('#FFFFFF')
q.speed(0)
p = turtle.Turtle()
p.hideturtle()
p.speed(0)
days = (16483651200-starttime) / 86400
daysr = 0

for i in range(1, 9):  # Orbit lines
    b.goto(0, 0)
    b.setheading(0)
    b.fd(30 + 30*i)
    b.setheading(90)
    b.circle(30 + 30*i, 360)


def sun(x, y, sz):
    s.up()
    s.fillcolor(sun_orange)
    s.color(sun_orange)
    s.goto(x, y)
    s.setheading(270)
    s.fd(sz)
    s.setheading(0)
    s.down()
    s.begin_fill()
    s.circle(sz, 360)
    s.end_fill()
    s.setheading(90)
    s.fd(sz)


def mercury(o, sz, days):  # for each planet the <Planet Name> function draws the planet and the <Planet Name>info function writes information about whichever planet was last clicked on
    m.up()
    m.fillcolor(mercury_blue)
    m.color(mercury_blue)
    m.goto(0, 0)
    m.setheading(0)
    m.fd(o)
    m.setheading(270)
    m.fd(sz)
    m.setheading(90)
    m.circle(60, (4.090909*days)%360)
    m.setheading(0)
    m.down()
    m.begin_fill()
    m.circle(sz, 360)
    m.end_fill()
    m.setheading(90)
    m.fd(sz)


def mercuryinfo(x, y):  # Planet info from https://solarsystem.nasa.gov/planets/overview/
    p.up()
    p.goto(x, y)
    p.write("Mercury", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: 430°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 2,439.7km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 0", font=("Verdana", 15, "normal"))


def venus(o, sz, days):
    v.up()
    v.fillcolor(venus_orange)
    v.color(venus_orange)
    v.goto(0, 0)
    v.setheading(0)
    v.fd(o)
    v.setheading(270)
    v.fd(sz)
    v.setheading(90)
    v.circle(90, (1.602136*days)%360)
    v.setheading(0)
    v.down()
    v.begin_fill()
    v.circle(sz, 360)
    v.end_fill()
    v.setheading(90)
    v.fd(sz)


def venusinfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Venus", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: 480°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 12,100km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 0", font=("Verdana", 15, "normal"))


def earth(o, sz, days):
    e.up()
    e.fillcolor(earth_blue)
    e.color(earth_blue)
    e.goto(0, 0)
    e.setheading(0)
    e.fd(o)
    e.setheading(270)
    e.fd(sz)
    e.setheading(90)
    e.circle(120, (.9863013*days)%360)
    e.setheading(0)
    e.down()
    e.begin_fill()
    e.circle(sz, 360)
    e.end_fill()
    e.setheading(90)
    e.fd(sz)


def earthinfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Earth", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: 13.9°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 12,542km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 1", font=("Verdana", 15, "normal"))


def mars(o, sz, days):
    a.up()
    a.fillcolor(mars_red)
    a.color(mars_red)
    a.goto(0, 0)
    a.setheading(0)
    a.fd(o)
    a.setheading(270)
    a.fd(sz)
    a.setheading(90)
    a.circle(150, (.5240174*days)%360)
    a.setheading(0)
    a.down()
    a.begin_fill()
    a.circle(sz, 360)
    a.end_fill()
    a.setheading(90)
    a.fd(sz)


def marsinfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Mars", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: -81°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 6,780km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 2", font=("Verdana", 15, "normal"))


def jupiter(o, sz, days):
    j.up()
    j.fillcolor(jupiter_brown)
    j.color(jupiter_brown)
    j.goto(0, 0)
    j.setheading(0)
    j.fd(o)
    j.setheading(270)
    j.fd(sz)
    j.setheading(90)
    j.circle(180, (.0828729*days)%360)
    j.setheading(0)
    j.down()
    j.begin_fill()
    j.circle(sz, 360)
    j.end_fill()
    j.setheading(90)
    j.fd(sz)


def jupiterinfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Jupiter", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: -110°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 142,984km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 53", font=("Verdana", 15, "normal"))


def saturn(o, sz, days):
    t.up()
    t.fillcolor(saturn_brown)
    t.color(saturn_brown)
    t.goto(0, 0)
    t.setheading(0)
    t.fd(o)
    t.setheading(270)
    t.fd(sz)
    t.setheading(90)
    t.circle(210, (.03343239*days)%360)
    t.setheading(0)
    t.down()
    t.begin_fill()
    t.circle(sz, 360)
    t.end_fill()
    t.setheading(90)
    t.fd(sz)


def saturninfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Saturn", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: -178°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 116,434km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 82", font=("Verdana", 15, "normal"))


def uranus(o, sz, days):
    u.up()
    u.fillcolor(uranus_blue)
    u.color(uranus_blue)
    u.goto(0, 0)
    u.setheading(0)
    u.fd(o)
    u.setheading(270)
    u.fd(sz)
    u.setheading(90)
    u.circle(240, (.011741168*days)%360)
    u.setheading(0)
    u.down()
    u.begin_fill()
    u.circle(sz, 360)
    u.end_fill()
    u.setheading(90)
    u.fd(sz)


def uranusinfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Uranus", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: -195°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 50,724km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 27", font=("Verdana", 15, "normal"))


def neptune(o, sz, days):
    n.up()
    n.fillcolor(neptune_blue)
    n.color(neptune_blue)
    n.goto(0, 0)
    n.setheading(0)
    n.fd(o)
    n.setheading(270)
    n.fd(sz)
    n.setheading(90)
    n.circle(270, (.00598483*days)%360)
    n.setheading(0)
    n.down()
    n.begin_fill()
    n.circle(sz, 360)
    n.end_fill()
    n.setheading(90)
    n.fd(sz)


def neptuneinfo(x, y):
    p.up()
    p.goto(x, y)
    p.write("Neptune", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 20)
    p.down()
    p.write("Planet Surface Temp: -200°C", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 40)
    p.down()
    p.write("Planet Diameter: 49,244km", font=("Verdana", 15, "normal"))
    p.up()
    p.goto(x, y - 60)
    p.down()
    p.write("Number of Moons: 14", font=("Verdana", 15, "normal"))


def eraseall():  # erases all planets
    s.clear()
    v.clear()
    m.clear()
    e.clear()
    a.clear()
    j.clear()
    t.clear()
    u.clear()
    n.clear()


def write(x, y, txt, color, num):
    if num == 0:  # Writes elapsed days positive or negative
        w.up()
        w.goto(x, y)
        w.color(color)
        w.down()
        w.write("Days: " + txt, font=("Verdana", 15, "normal"))
    elif num == 1:
        z.up()
        z.goto(x, y)
        z.color(color)
        z.down()
        z.write("Days per cycle: " + txt, font=("Verdana", 15, "normal"))
    else:
        c.up()
        c.goto(x, y)
        x = re.split(',|\=', txt)
        c.color(color)
        c.down()
        c.write("Date: " + "Year " + x[1] + ", Month " + x[3] +
                ", Day " + x[5], font=("Verdana", 15, "normal"))


gosystem = True
dysprs = 1

while gosystem == True:
    daysr += dysprs
    s.clear()
    # calls planet functions to calculate position and records x and y coordinates in a list
    sun(0, 0, 30)
    scor = [s.xcor()]
    scor.append(s.ycor())
    m.clear()
    mercury(60, 10, days)
    mcor = [m.xcor()]
    mcor.append(m.ycor())
    v.clear()
    venus(90, 10, days)
    vcor = [v.xcor]
    vcor.append(v.ycor)
    e.clear()
    earth(120, 10, days)
    ecor = [e.xcor]
    ecor.append(e.ycor)
    a.clear()
    mars(150, 10, days)
    acor = [a.xcor]
    acor.append(a.ycor)
    j.clear()
    jupiter(180, 10, days)
    jcor = [j.xcor]
    jcor.append(j.ycor)
    t.clear()
    saturn(210, 10, days)
    tcor = [t.xcor]
    tcor.append(t.ycor)
    u.clear()
    uranus(240, 10, days)
    ucor = [u.xcor]
    ucor.append(u.ycor)
    n.clear()
    neptune(270, 10, days)
    ncor = [n.xcor]
    ncor.append(n.ycor)
    w.clear()

    # Writes info in the bottom-left
    write(-400, -300, str(round(daysr, 2)), 'black', 0)
    z.clear()
    write(-400, -320, str(round(dysprs, 3)), 'black', 1)
    c.clear()
    write(-400, -340, str(time.gmtime((daysr*86400)+starttime)), 'black', 2)

    if keyboard.is_pressed('up_arrow'):  # changes speed
        dysprs += .2
        time.sleep(.1)
    if keyboard.is_pressed('down_arrow'):
        dysprs -= .2
        time.sleep(.1)
    if keyboard.is_pressed('w'):
        dysprs += .05
        time.sleep(.1)
    if keyboard.is_pressed('s'):
        dysprs -= .05
        time.sleep(.1)
    sc.onclick(q.goto)  # turtle follows mouse clicks

    # adds information about planets when there are clicked
    # recommeded by Jackson Baldwin 11 March 2022 and for planet names and info
    if (q.xcor() >= m.xcor() - 10 and q.xcor() <= m.xcor() + 10) and (q.ycor() >= m.ycor() - 10 and q.ycor() <= m.ycor() + 10):
        p.clear()
        mercuryinfo(-400, 300)
    if (q.xcor() >= v.xcor() - 10 and q.xcor() <= v.xcor() + 10) and (q.ycor() >= v.ycor() - 10 and q.ycor() <= v.ycor() + 10):
        p.clear()
        venusinfo(-400, 300)
    if (q.xcor() >= e.xcor() - 10 and q.xcor() <= e.xcor() + 10) and (q.ycor() >= e.ycor() - 10 and q.ycor() <= e.ycor() + 10):
        p.clear()
        earthinfo(-400, 300)
    if (q.xcor() >= a.xcor() - 10 and q.xcor() <= a.xcor() + 10) and (q.ycor() >= a.ycor() - 10 and q.ycor() <= a.ycor() + 10):
        p.clear()
        marsinfo(-400, 300)
    if (q.xcor() >= j.xcor() - 10 and q.xcor() <= j.xcor() + 10) and (q.ycor() >= j.ycor() - 10 and q.ycor() <= j.ycor() + 10):
        p.clear()
        jupiterinfo(-400, 300)
    if (q.xcor() >= t.xcor() - 10 and q.xcor() <= t.xcor() + 10) and (q.ycor() >= t.ycor() - 10 and q.ycor() <= t.ycor() + 10):
        p.clear()
        saturninfo(-400, 300)
    if (q.xcor() >= u.xcor() - 10 and q.xcor() <= u.xcor() + 10) and (q.ycor() >= u.ycor() - 10 and q.ycor() <= u.ycor() + 10):
        p.clear()
        uranusinfo(-400, 300)
    if (q.xcor() >= n.xcor() - 10 and q.xcor() <= n.xcor() + 10) and (q.ycor() >= n.ycor() - 10 and q.ycor() <= n.ycor() + 10):
        p.clear()
        neptuneinfo(-400, 300)
    if keyboard.is_pressed('escape'):
        sc.bye()
    sc.update()

    days += dysprs

time.sleep(3)