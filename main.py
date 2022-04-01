speed = 3 #steps per sec

import pygame, random, math, keyboard
import time as t


win = pygame.display
display = win.set_mode((1200, 600))
allTime = []
eachTime = []


def litterlyFreakingEverything():
    
    class Circle:
        def __init__(self):

            self.pos = [random.randint(900, 1200), random.randint(50, 450)] #every unit = 1/25 a step. Tennis court is ~ 48 steps by 24 steps 
            locations.append(self.pos)
            self.stray = [random.randint(0, 800), random.randint(0, 600)]
            self.color = (0,255, 0)
            self.radius = 10


        def draw(self, i):
            pygame.draw.line(display, (0,0,0), (600,600), (600,0), 3)
            pygame.draw.circle(display,  (0,0,255), (600,600), self.radius)
            randint = random.randint(12, 15)
            print(randint)
            print('i ' + str(i))
            if i <= randint:
                pygame.draw.circle(display, self.color, (self.pos[0], self.pos[1]), self.radius)
            else:
                pygame.draw.circle(display, self.color, (self.stray[0], self.stray[1]), self.radius)


    ballTimes = []
    ballDropped = []
    ballNotDropped = []

    def calculations(ball):
        length = len(locations) - 1
        numero = ball
        #print(numero)
        for i in range(length - numero):
            #print(numero)
            x1 = locations[ball][0]
            x2 = locations[numero + 1][0]
            y1 = locations[ball][1]
            y2 = locations[numero + 1][1]
            
            dist = distance(x1, x2, y1, y2)
            time = timePerBall(dist)

            
            #print(str(time) + ' seconds')   
            lowest.append(time)
            numero += 1
            #print(numero)

        
        #print(lowest)
        #print(seconds)
        if len(lowest) > 0:
            seconds.append(min(lowest))
            dropage = randomBallDropage()
            if dropage == True:
                ballTimes.append(time)
            #print(min(lowest))
        #print(min(test))
        lowest.clear()

    def pathing():
            for ball in range(len(locations) - 1):
                calculations(ball)
            #print(len(lowest))
    
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


    def firstBall():
        x1 = 600 
        x2 = locations[0][0]
        y1 = 600
        y2 = locations[0][1]
        dist = distance(x1, x2, y1, y2)
        time = timePerBall(dist)
        #print(time + ' seconds') 
        #print('1')
        seconds.append(time)

    circles = []
    locations = []
    seconds = []
    lowest = []

    for i in range(20):
        circles.append(Circle())

    def distance(x1, x2, y1, y2):
        distExact = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))/25
        dist = round(distExact)
        return dist

    def timePerBall(dist):
        time = round(dist/speed)
        return time

    def timeAll():
        #print(len(locations))
        #print(locations[19][0])
        x1 = 600 
        x2 = locations[19][0]
        y1 = 600
        y2 = locations[19][1]
        dist = distance(x1, x2, y1, y2)
        time = timePerBall(dist)
        total = sum(seconds) + time + sum(ballTimes)
        return total

    def timeEach():
        hardCode = [6, 12, 18]
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

    def average():
        firstBall()
        pathing()
        totalAll = timeAll()
        totalEach = timeEach()
        allTime.append(totalAll)
        eachTime.append(totalEach)
        
    display.fill((255, 255, 255))
    pygame.event.get()
    i = 0
    for circle in circles:
        circle.draw(i)
        i += 1
        #print(i)
    average()
    #print(locations[19][0])
    win.flip()
    
               

litterlyFreakingEverything()
t.sleep(5)
print("On average if you picked up all the balls at once it would take: " + str(round(sum(allTime)/len(allTime))) + ' seconds to pick up the balls')
print("On average if you picked up 6 balls at a time it would take: " + str(round(sum(eachTime)/len(eachTime))) + ' seconds to pick up the balls')





    



