
#importing
from tkinter import N
import pygame, random, math, keyboard
import time as t


win = pygame.display #setup pygame
display = win.set_mode((1200, 600)) #setup pygame size

speed = 3 #steps per sec
allTime = [] #List For Speed Of Picking Up All Balls At Once
eachTime = []#List For Speed Of Picking Up 6 Balls At Once


def litterlyFreakingEverything():

    #All List Var
    ballTimes = []
    ballDropped = []
    ballNotDropped = []
    circles = []
    locations = []
    seconds = []
    lowest = [] 

    class Circle:
        def __init__(self):

            self.pos = [random.randint(900, 1200), random.randint(50, 450)] #every unit = 1/25 a step. Tennis court is ~ 48 steps by 24 steps 
            locations.append(self.pos) #append location of ball to a list
            self.stray = [random.randint(0, 800), random.randint(0, 600)] #stray balls (Balls that dont follow aggregation rules) balls that are missed/stray balls
            self.color = (0,255, 0) #Ball color
            self.radius = 10 #Ball size


        def draw(self, i):
            pygame.draw.line(display, (0,0,0), (600,600), (600,0), 3) #Draw net 
            pygame.draw.circle(display,  (0,0,255), (600,600), self.radius) #Draw origin point
            randint = random.randint(12, 15) #Generate random int
            
            #Decide if a ball is stray or not based on randomization 
            if i <= randint:
                pygame.draw.circle(display, self.color, (self.pos[0], self.pos[1]), self.radius)
            else:
                pygame.draw.circle(display, self.color, (self.stray[0], self.stray[1]), self.radius)


    def calculations(ball):
        length = len(locations) - 1
        numero = ball

        for i in range(length - numero):
            #X and Y of the begining ball and every possible ball it can go to (Not picked up balls)
            x1 = locations[ball][0]
            x2 = locations[numero + 1][0]
            y1 = locations[ball][1]
            y2 = locations[numero + 1][1]
            
            #distance & time from the beggining ball to every ball it can go to (Not picked up balls)
            dist = distance(x1, x2, y1, y2)
            time = timePerBall(dist)

            #Takes all the times of all the possible balls and adds them to a list
            lowest.append(time)
            #goes to the next possible ball 
            numero += 1

        
        #If the length of the lowest list is above 0 then add the lowest of the possible balls(the closest ball) to a list
        if len(lowest) > 0:
            seconds.append(min(lowest))
            #Randomly decides if a ball is dropped or not based on the number of balls picked up 
            dropage = randomBallDropage()
            #If ball dropped is true add the time to a list
            if dropage == True:
                #From my tests it took about 5 - 10 seconds to get a ball back on my raquet if I dropped it 
                ballTimes.append(random.randint(5, 10))
        #Clearing the list
        lowest.clear()

    #Checks every possible ball combination for the lowest one as outlined above 
    def pathing():
            for ball in range(len(locations) - 1):
                calculations(ball)
    
    #Horrible way of doing this but if the random number is above or below a certain number a ball is dropped. As there is more balls dropped (Length of seconds) the higher the chance
    def randomBallDropage():

        if len(seconds) <= 3:
            randNum1 = random.randint(0, 100)
            if randNum1 <= 0:
                ballDropped.append(randNum1)
                return True
            elif randNum1 >= 1:
                ballNotDropped.append(randNum1) 
                

        elif len(seconds) <= 6 and len(seconds) >= 3:  
            randNum2 = random.randint(0, 100)
            if randNum2 <= 2:
                ballDropped.append(randNum2)
                return True
            elif randNum2 >= 3:
                ballNotDropped.append(randNum2) 


        elif len(seconds) <= 12 and len(seconds) >= 6: 
            randNum3 = random.randint(0, 100)
            if randNum3 <= 5:
                ballDropped.append(randNum3)
                return True
            elif randNum3 >= 6:
                ballNotDropped.append(randNum3) 


        elif len(seconds) <= 18 and len(seconds) >= 12:
            randNum4 = random.randint(0, 100)
            if randNum4 <= 10:
                ballDropped.append(randNum4)
                return True
            elif randNum4 >= 11:
                ballNotDropped.append(randNum4) 

    #the first ball from the origin point
    def firstBall():
        #X and Y of the begining ball and every possible ball it can go to (Not picked up balls)
        for i in range(20):
            numero = 0
            x1 = 600
            x2 = locations[numero][0]
            y1 = 600
            y2 = locations[numero][1]
            
            #distance & time from the beggining ball to every ball it can go to (Not picked up balls)
            dist = distance(x1, x2, y1, y2)
            time = timePerBall(dist)

            #Takes all the times of all the possible balls and adds them to a list
            lowest.append(time)
            #goes to the next possible ball 
            numero += 1

        
        #If the length of the lowest list is above 0 then add the lowest of the possible balls(the closest ball) to a list
        if len(lowest) > 0:
            seconds.append(min(lowest))
            #Randomly decides if a ball is dropped or not based on the number of balls picked up 
            dropage = randomBallDropage()
            #If ball dropped is true add the time to a list
            if dropage == True:
                #From my tests it took about 5 - 10 seconds to get a ball back on my raquet if I dropped it 
                ballTimes.append(random.randint(5, 10))
        #Clearing the list
        lowest.clear()

    #adding all circles to a lsit
    for i in range(20):
        circles.append(Circle())

    #Takes the starting x point and the starting y point and caluclates the distance to the ending x point and the ending y point https://en.wikipedia.org/wiki/Distance
    def distance(x1, x2, y1, y2):
        distExact = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))/25
        dist = round(distExact)
        return dist

    #calculates the time by dividing the distance by the speed https://en.wikipedia.org/wiki/Speed
    def timePerBall(dist):
        time = round(dist/speed)
        return time

    #The amount of time it takes to take all the balls back to the basket + all the time it takes to pick up the dropped balls + all the time it takes to pick up all the balls in general 
    def timeAll():
        x1 = 600 
        x2 = locations[19][0]
        y1 = 600
        y2 = locations[19][1]
        dist = distance(x1, x2, y1, y2)
        time = timePerBall(dist)
        total = sum(seconds) + time + sum(ballTimes)
        return total

    #The amount of time it takes to drop off the balls every 6 balls + the total amount of time to pick up the balls
    def timeEach():
        hardCode = [6, 12, 18] #Should change to calculate multiples of 6 up to 3 iterations 
        extra = []
        for code in hardCode:
            x1 = 600 
            x2 = locations[code][0]
            y1 = 600
            y2 = locations[code][1]
            dist = distance(x1, x2, y1, y2)
            time = timePerBall(dist)
            extra.append(time)
        totalExtra = sum(extra)
        total = sum(seconds) + totalExtra 
        return total

    #All the calculations finally used, end product
    def average():
        firstBall()
        pathing()
        totalAll = timeAll()
        totalEach = timeEach()
        allTime.append(totalAll)
        eachTime.append(totalEach)
    
    #Creates Screen
    display.fill((255, 255, 255))
    pygame.event.get()
    #Draws Circles
    i = 0
    for circle in circles:
        circle.draw(i)
        i += 1
    average()
    #Refreshes Screen 
    win.flip()
    
               

litterlyFreakingEverything()
t.sleep(5)
print("On average if you picked up all the balls at once it would take: " + str(round(sum(allTime)/len(allTime))) + ' seconds to pick up the balls')
print("On average if you picked up 6 balls at a time it would take: " + str(round(sum(eachTime)/len(eachTime))) + ' seconds to pick up the balls')





    



