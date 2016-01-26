import pygame, sys
from pygame.locals import *
pygame.init() #load pygame modules

size = width, height = 1140, 500 #size of window
screen = pygame.display.set_mode((size)) #make window

levelwidth = 10000


class Scrn:
    def __init__(self,width):
        self.sky = pygame.image.load("stars.gif")
        self.stars = pygame.image.load("midstars.gif")
        self.stars2 = pygame.image.load("frontstars.gif")
        self.planets = pygame.image.load("pics/planets.gif")
        self.scrolltimer = 60
        self.scroll = float(width)
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(" ", 1, (100, 100, 100))
    def ScrollAdjust(self, s):
        if self.scrolltimer > 0:
            self.scrolltimer -= 1
        if self.scrolltimer == 0 and p[0].rect.right > width * .6 and self.scroll < levelwidth - 1:
            p[0].rect = p[0].rect.move(-2, 0)
            self.Scroll(2)
        if self.scrolltimer == 0 and p[0].rect.left < width * .4 and self.scroll > width + 1:
            p[0].rect = p[0].rect.move(2, 0)
            self.Scroll(-2)
    def TimerReset(self, s):
        self.scrolltimer = 50
    def Scroll(self, acc):
        self.scroll += acc
        for i in range(len(platforms)):
            platforms[i].move(-acc)
        for i in range(len(floors)):
            floors[i].move(-acc)
        for i in range(len(b1)):
            b1[i].move(-acc)
        for i in range(len(b2)):
            b2[i].move(-acc)
        for i in range(len(g)):
            g[i].move(-acc)
        for i in range(len(flags)):
            flags[i].move(-acc)
    def display(self):
        screen.fill((10,10,10)) #make redraw background black
        screen.blit(s[0].sky,[(-self.scroll - 940)*.1, 0]) #render the surface into the rectangle
        screen.blit(s[0].stars,[(-self.scroll - 940)*.2, 0]) #render the surface into the rectangle
        screen.blit(s[0].planets,[(-self.scroll - 940)*.25, 0]) #render the surface into the rectangle
        screen.blit(s[0].stars2,[(-self.scroll - 940)*.3, 0]) #render the surface into the rectangle
        for i in range(len(p)):
            screen.blit(p[i].image,p[i].rect) #render the surface into the rectangle
        for i in range(len(platforms)):
            screen.blit(platforms[i].image,platforms[i].rect) #displays the bumper on the screen
        for i in range(len(floors)):
            screen.blit(floors[i].image,floors[i].rect) #displays the bumper on the screen
        for i in range(len(b1)):
            screen.blit(b1[i].image,b1[i].rect) #displays the bumper on the screen
        for i in range(len(b2)):
            screen.blit(b2[i].image,b2[i].rect) #displays the bumper on the screen
        for i in range(len(g)):
            screen.blit(g[i].image,g[i].rect) #displays the bumper on the screen
        for i in range(len(l)):
            screen.blit(l[i].image,l[i].rect) #displays the bumper on the screen
        for i in range(len(lb)):
            screen.blit(lb[i].image,lb[i].rect) #displays the bumper on the screen
        for i in range(len(flags)):
            screen.blit(flags[i].image,flags[i].rect) #displays the bumper on the screen
        screen.blit(self.text,[200,0]) #render the surface into the rectangle
        p[0].charge = pygame.transform.scale(p[0].charge, (45, 1 + (199 * p[0].lasertimer) / 500))
        screen.blit(p[0].charge,[width - 45,120 - (1 + (199 * p[0].lasertimer) / 500)]) #render the surface into the rectangle
        screen.blit(p[0].chargeplate,[width - 45,0]) #render the surface into the rectangle
        pygame.display.flip() #update the screen
    def MusicStart(self):
        pygame.mixer.music.load('cosmos_man_tsc.mid')
        pygame.mixer.music.play(-1, 0.0)
    def Win(self):
        sys.exit() #close cleanly


class Player:
    def __init__(self,pos):
        self.images = []
        self.images.append(load_image('pics/spaceman1.png'))
        self.images.append(load_image('pics/spaceman2.png'))
        self.images.append(load_image('pics/spaceman3.png'))
        self.images.append(load_image('pics/spaceman4.png'))
        self.images.append(load_image('pics/spaceman5.png'))
        self.images.append(load_image('pics/spaceman6.png'))
        self.images.append(load_image('pics/spaceman7.png'))
        self.images.append(load_image('pics/spaceman8.png'))
        self.images.append(load_image('pics/spaceman9.png'))
        self.images.append(load_image('pics/spaceman10.png'))
        self.images.append(load_image('pics/spaceman11.png'))
        self.animate = 0
        self.image = self.images[self.animate]
        self.rect = self.image.get_clip()
        self.rect = self.rect.move(pos[0], pos[1])
        self.feetimage = pygame.image.load("pics/feet.png")
        self.feetrect = self.rect.move(8, 36)
        self.rightimage = pygame.image.load("pics/side.png")
        self.rightrect = self.rect.move(26, 0)
        self.leftimage = pygame.image.load("pics/side.png")
        self.leftrect = self.rect.move(0, 0)
        self.chargeplate = pygame.image.load("pics/charge1.png")
        self.charge = pygame.image.load("pics/charge2.png")
        self.acc = 0.0
        self.grav = 0
        self.dropspeed = 6
        self.jump = 0
        self.jumpt = 0
        self.jumpleeway = 7
        self.jumpt2 = self.jumpleeway
        self.landed = 0
        self.maxspeed = 12
        self.lives = 3
        self.deatha = 0
        self.lasertime = 100
        self.lasertimer = 3 * self.lasertime
        self.grenadetimer = 0
        self.direction = 1
        self.pause = False
        self.pausetimer = 0
        self.jumpsound = pygame.mixer.Sound('jump.wav')
        self.lasersound = pygame.mixer.Sound('laser.wav')
        self.lasercharge = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.feetmask = pygame.mask.from_surface(self.feetimage)
        self.rightmask = pygame.mask.from_surface(self.rightimage)
        self.leftmask = pygame.mask.from_surface(self.leftimage)
        self.image.set_colorkey((255, 255, 255))
        self.feetimage.set_colorkey((255, 255, 255))
        self.rightimage.set_colorkey((255, 255, 255))
        self.leftimage.set_colorkey((255, 255, 255))
    def logic(self):
        self.Movement()
        if self.grenadetimer > 0:
            self.grenadetimer -= 1
        if self.lasertimer < self.lasertime * 3:
            self.lasertimer += 1
        if self.lasertimer == self.lasertime * 3:
            self.lasercharge = 3
        elif self.lasertimer >= self.lasertime * 2:
            self.lasercharge = 2
        elif self.lasertimer >= self.lasertime:
            self.lasercharge = 1
        else:
            self.lasercharge = 0
        if p[0].rect.top >= height:
            p[0].Death()
        if self.deatha > 0:
            self.Death()

        if self.deatha > 90:
            self.animate = 10
        elif self.deatha > 80:
            self.animate = 9
        elif self.deatha > 70:
            self.animate = 8
        elif self.deatha > 60:
            self.animate = 7
        elif self.deatha > 50:
            self.animate = 6
        elif self.deatha > 40:
            self.animate = 5
        elif self.deatha > 30:
            self.animate = 5
        elif self.deatha > 20:
            self.animate = 4
        elif self.deatha > 0 or self.grav >= 0:
            self.animate = 0
        elif self.grav < 0 + self.animate == 0:
            self.animate = 4
        elif self.grav < 0 + self.animate > 0:
            self.animate -= 1
        else:
            self.animate = 1
        self.update()
        if self.direction == 2:
            self.image = pygame.transform.flip(self.image, True, False)
    def keypress(self, keys):
        self.dropspeed = 6
        if keys[K_LEFT] and p[0].rect.left > 0:
            self.acc -= 2
            s[0].TimerReset(s)
            if self.direction == 1:
                self.direction = 2
            if self.acc < -self.maxspeed:
                self.acc = -self.maxspeed
        if keys[K_RIGHT] and p[0].rect.right < width:
            self.acc += 2
            if self.direction == 2:
                self.direction = 1
            s[0].TimerReset(s)
            if self.acc > self.maxspeed:
                self.acc = self.maxspeed
        if (keys[K_SPACE] or keys[K_UP]):
            self.dropspeed = 1
        if (keys[K_SPACE] or keys[K_UP]) and ((self.jump == 1)or(self.jump == 2 and self.jumpt2 > 0)) and self.jumpt == 0:
            self.jump -= 1
            self.jumpt = 12
            self.landed = 0
            if self.jump == 1:
                self.grav = -12
            if self.jump == 0:
                self.grav = -18
            self.jumpsound.play()
        if keys[K_LCTRL]:
            if self.lasertimer >= self.lasertime:
                if self.direction == 1:
                    l.append(Laser([self.rect.right, (self.rect.top + self.rect.bottom) / 2], self.direction, self.lasercharge))
                if self.direction == 2:
                    l.append(Laser([self.rect.left, (self.rect.top + self.rect.bottom) / 2], self.direction, self.lasercharge))
                self.lasertimer = 0
                self.lasersound.play()
        if keys[K_LSHIFT] and self.grenadetimer == 0:
            if self.direction == 1:
                g.append(Grenade([self.rect.right, (self.rect.top + self.rect.bottom) / 2], self.direction))
            if self.direction == 2:
                g.append(Grenade([self.rect.left, (self.rect.top + self.rect.bottom) / 2], self.direction))
            self.grenadetimer = 100
        if keys[K_RSHIFT]:
            for i in range(len(g)):
                g[i].explode(i)
        if keys[K_RETURN] and self.pausetimer == 0:
            self.pause = not self.pause
            self.pausetimer = 10

    def Movement(self):
        self.landed = 0
        for i in range(len(floors)):
            floors[i].landcheck(p)
        for i in range(len(platforms)):
            platforms[i].landcheck(p)
        if self.jumpt > 0:
            self.jumpt -= 1
        if self.landed == 1:
            self.grav = 0
            self.jump = 2
        else:
            self.rect=self.rect.move(0, self.grav)
            if self.grav <= self.dropspeed:
                self.grav += 1

        if self.landed == 1:
            self.jumpt2 = self.jumpleeway
        else:
            if self.jumpt2 > 0:
                self.jumpt2 -= 1

        if self.acc > 0:#if player is moving right
            if self.rect.right >= width * .8 and s[0].scroll < levelwidth:#if player is to the right of the screen
                if s[0].scroll + p[0].acc > levelwidth: #if the screen is to the right of the level
                    s[0].Scroll(levelwidth - s[0].scroll)
                    self.rect = self.rect.move(p[0].acc + s[0].scroll - levelwidth, 0)
                else:
                    s[0].Scroll(self.acc)
            else:
                if self.rect.right + self.acc < width:
                    self.rect = self.rect.move(self.acc, 0)
                else:
                    self.rect = self.rect.move(width-self.rect.right, 0)
            self.acc -= 1

        if self.acc < 0: #if player is moving left
            if self.rect.left <= width * .2 and s[0].scroll > width:
                if s[0].scroll + self.acc < width:
                    s[0].Scroll(width - s[0].scroll)
                    self.rect = self.rect.move(self.acc + s[0].scroll - width, 0)
                else:
                    s[0].Scroll(self.acc)
            else:
                if self.rect.left + self.acc > 0:
                    self.rect = self.rect.move(self.acc, 0)
                else:
                    self.rect = self.rect.move(-self.rect.left, 0)
            self.acc += 1

        #if running against a wall
        if self.rect.left + self.acc < 0:
            self.acc = self.rect.left
        if self.rect.right + self.acc > width:
            self.acc = width - self.rect.right

        for i in range(len(b1)):
            b1[i].collide(p)

        for i in range(len(flags)):
            flags[i].collide(p)


    def Death(self):
        self.grav = 0
        self.acc = 0
        if self.deatha == 0:
            self.deatha = 100
        if self.deatha > 70:
            self.rect = self.rect.move(0, -5)
            self.deatha -= 1
        if 90 >= self.deatha > 1:
            self.rect = self.rect.move(0, 7)
            self.deatha -= 1
        if self.deatha == 1:
            del s[:]
            s.append(Scrn(width))

            del l[:]

            del lb[:]

            del p[:]
            for i in range(len(playerpos)):
                p.append(Player(playerpos[i]))

            del floors[:]
            for i in range(len(floorpos)):
                floors.append(Floor(floorpos[i]))

            del platforms[:]
            for i in range(len(platpos)):
                platforms.append(Platform(platpos[i]))

            del flags[:]
            flags.append(flag(flagpos))

            del b1[:]
            for i in range(len(baddy1pos)):
                b1.append(baddy1(baddy1pos[i]))

            del b2[:]
            for i in range(len(baddy2pos)):
                b2.append(baddy2(baddy2pos[i]))

    def update(self):
        self.image = self.images[self.animate]


class Laser:
    def __init__(self, pos, direction, charge):
        self.charge = charge
        self.image = pygame.image.load("pics/laser1.jpg")
        if self.charge == 2:
            self.image = pygame.image.load("pics/laser2.png")
        elif self.charge == 3:
            self.image = pygame.image.load("pics/laser3.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])
        self.direction = direction
        if self.direction == 2:
            self.rect = self.rect.move(-self.rect.width, 0)
            self.image = pygame.transform.flip(self.image, True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.offset_x = 0
        self.offset_y = 0
        self.image.set_colorkey((255, 255, 255))
    def logic(self):
        self.move()
        for i in range(len(b1)):
            if self.rect.colliderect(b1[i].rect):
                self.offset_x = self.rect.left - b1[i].rect.left
                self.offset_y = self.rect.top - b1[i].rect.top
                if (b1[i].mask.overlap(self.mask, (self.offset_x, self.offset_y)) != None):
                    self.Death()
                    b1[i].health -= self.charge
                    b1[i].animate = 9
        for i in range(len(b2)):
            if self.rect.colliderect(b2[i].rect):
                self.mask = pygame.mask.from_surface(self.image)
                b2[i].mask = pygame.mask.from_surface(b2[i].image)
                self.offset_x = self.rect.left - b2[i].rect.left
                self.offset_y = self.rect.top - b2[i].rect.top
                if (b2[i].mask.overlap(self.mask, (self.offset_x, self.offset_y)) != None):
                    self.Death()
                    b2[i].health -= self.charge
                    b2[i].mode = 2
                    b2[i].animate = 11
        for i in range(len(floors)):
            if self.rect.colliderect(floors[i].rect):
                self.mask = pygame.mask.from_surface(self.image)
                floors[i].mask = pygame.mask.from_surface(floors[i].image)
                self.offset_x = self.rect.left - floors[i].rect.left
                self.offset_y = self.rect.top - floors[i].rect.top
                if (floors[i].mask.overlap(self.mask, (self.offset_x, self.offset_y)) != None):
                    self.Death()
    def move(self):
        for i in range(5):
            if self.direction == 1:
                self.rect = self.rect.move(5, 0)
            if self.direction == 2:
                self.rect = self.rect.move(-5, 0)
    def Death(self):
        self.rect = self.rect.move(0,1000)

class Grenade:
    def __init__(self, pos, direction):
        self.timer = 0
        self.grav = -20
        self.image = pygame.image.load("pics/energyball.gif")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])
        self.imageb = pygame.image.load("pics/energyballb.gif")
        self.rectb = self.rect.move(2, 17)
        self.imager = pygame.image.load("pics/energyballside.gif")
        self.rectr = self.rect.move(17, 2)
        self.imagel = pygame.image.load("pics/energyballside.gif")
        self.rectl = self.rect.move(0, 2)
        self.maskb = pygame.mask.from_surface(self.imageb)
        self.maskr = pygame.mask.from_surface(self.imager)
        self.maskl = pygame.mask.from_surface(self.imagel)
        self.imageb.set_colorkey((255, 255, 255))
        self.imager.set_colorkey((255, 255, 255))
        self.imagel.set_colorkey((255, 255, 255))
        if direction == 1:
            self.acc = 10
        if direction == 2:
            self.acc = -10
    def move(self, speed):
        self.rect = self.rect.move([speed, 0])
        self.rectb = self.rectb.move([speed, 0])
        self.rectr = self.rectr.move([speed, 0])
        self.rectl = self.rectl.move([speed, 0])
    def logic(self, i):
        self.timer += 1
        self.move(self.acc)
        if self.timer == 100:
            self.explode(i)
        self.rect = self.rect.move(0, self.grav)
        self.rectb = self.rectb.move(0, self.grav)
        self.rectr = self.rectr.move(0, self.grav)
        self.rectl = self.rectl.move(0, self.grav)
        self.grav += 1
        self.bouncecheck()
    def bouncecheck(self):
        for i in range(len(floors)):
            if self.rect.colliderect(floors[i].rect):
                self.offset_x = floors[i].rect.left - self.rectb.left #offset for bottom bound
                self.offset_y = floors[i].rect.top - self.rectb.top
                if (self.maskb.overlap(floors[i].mask, (self.offset_x, self.offset_y)) != None) and self.grav >= 0:
                    print "hit"
                    while (self.maskb.overlap(floors[i].mask, (self.offset_x, self.offset_y)) != None):
                        print ("under")
                        self.rect = self.rect.move(0, -1)
                        self.rectb = self.rectb.move(0, -1)
                        self.rectr = self.rectr.move(0, -1)
                        self.rectl = self.rectl.move(0, -1)
                        self.offset_x = floors[i].rect.left - self.rectb.left #offset for bottom bound
                        self.offset_y = floors[i].rect.top - self.rectb.top
                    self.rect = self.rect.move(0, -1)
                    self.rectb = self.rectb.move(0, -1)
                    self.rectr = self.rectr.move(0, -1)
                    self.rectl = self.rectl.move(0, -1)
    #                self.offset_x = floors[i].rect.left - self.rectr.left #offset for bottom bound
    #                self.offset_y = floors[i].rect.top - self.rectr.top
    #                self.grav = -.75 * self.grav
    #                self.offset_x = floors[i].rect.left - self.rectr.left #offset for bottom bound
    #                self.offset_y = floors[i].rect.top - self.rectr.top
    #            elif (self.maskr.overlap(floors[i].mask, (self.offset_x, self.offset_y)) != None) and self.acc > 0:
    #                self.rect = self.rect.move(-1, 0)
    #                self.rectb = self.rectb.move(-1, 0)
    #                self.rectr = self.rectr.move(-1, 0)
    #                self.rectl = self.rectl.move(-1, 0)
    #                self.acc = -self.acc
    #                self.offset_x = floors[i].rect.left - self.rectl.left #offset for bottom bound
    #                self.offset_y = floors[i].rect.top - self.rectl.top
    #            if (self.maskl.overlap(floors[i].mask, (self.offset_x, self.offset_y)) != None) and self.acc > 0:
    #                self.rect = self.rect.move(1, 0)
    #                self.rectb = self.rectb.move(1, 0)
    #                self.rectr = self.rectr.move(1, 0)
    #                self.rectl = self.rectl.move(1, 0)
    #                self.acc = -self.acc
    def explode(self, i):
        try:
            g.pop(i)
        except:
            pass


class Platform:
    def __init__(self,pos):
        self.image = pygame.image.load("bumper2.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])
        self.mask = pygame.mask.from_surface(self.image)
    def move(self, speed):
        self.rect = self.rect.move([speed, 0])
    def landcheck(self, p):
        p[0].feetrect = p[0].rect.move(8, 36)
        p[0].rightrect = p[0].rect.move(26, 0)
        p[0].leftrect = p[0].rect.move(0, 0)
        self.offset_x = self.rect.left - p[0].feetrect.left #offset for bottom bound
        self.offset_y = self.rect.top - p[0].feetrect.top
        self.offset_x2 = self.rect.left - p[0].rightrect.left #offset for right bound
        self.offset_y2 = self.rect.top - p[0].rightrect.top
        self.offset_x3 = self.rect.left - p[0].leftrect.left #offset for left bound
        self.offset_y3 = self.rect.top - p[0].leftrect.top
        if (p[0].feetmask.overlap(self.mask, (self.offset_x, self.offset_y)) != None) and p[0].grav >= 0 and p[0].deatha == 0:
            p[0].landed = 1
            while (p[0].feetmask.overlap(self.mask, (self.offset_x, self.offset_y)) != None):
                p[0].rect = p[0].rect.move(0, -1)
                p[0].feetrect = p[0].feetrect.move(0, -1)
                p[0].rightrect = p[0].rightrect.move(0, -1)
                self.offset_x = self.rect.left - p[0].feetrect.left
                self.offset_y = self.rect.top - p[0].feetrect.top
            p[0].rect = p[0].rect.move(0, 3)
            p[0].feetrect = p[0].feetrect.move(0, 3)
            p[0].rightrect = p[0].rightrect.move(0, 3)

class Floor:
    def __init__(self, pos):
        self.image = pygame.image.load("floor.gif")
        self.image = pygame.transform.scale(self.image, (pos[2], height - pos[1]))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])
        self.mask = pygame.mask.from_surface(self.image)
    def move(self, speed):
        self.rect = self.rect.move([speed, 0])
    def landcheck(self, p):
        if self.rect.colliderect(p[0].rect):
            p[0].feetrect = p[0].rect.move(8, 36)
            p[0].rightrect = p[0].rect.move(26, 0)
            p[0].leftrect = p[0].rect.move(0, 0)
            self.offset_x = self.rect.left - p[0].feetrect.left #offset for bottom bound
            self.offset_y = self.rect.top - p[0].feetrect.top
            self.offset_x2 = self.rect.left - p[0].rightrect.left #offset for right bound
            self.offset_y2 = self.rect.top - p[0].rightrect.top
            self.offset_x3 = self.rect.left - p[0].leftrect.left #offset for left bound
            self.offset_y3 = self.rect.top - p[0].leftrect.top
            if p[0].rightmask.overlap(self.mask, (self.offset_x2, self.offset_y2)) != None and p[0].deatha == 0 and p[0].acc > 0:
                p[0].acc = 0
                while p[0].rightmask.overlap(self.mask, (self.offset_x2, self.offset_y2)) != None:
                    p[0].rect = p[0].rect.move(-1, 0)
                    p[0].feetrect = p[0].feetrect.move(-1, 0)
                    p[0].rightrect = p[0].rightrect.move(-1, 0)
                    p[0].leftrect = p[0].leftrect.move(-1, 0)
                    self.offset_x2 = self.rect.left - p[0].rightrect.left
                    self.offset_y2 = self.rect.top - p[0].rightrect.top
                p[0].rect = p[0].rect.move(1, 0)
                p[0].feetrect = p[0].feetrect.move(1, 0)
                p[0].rightrect = p[0].rightrect.move(1, 0)
                p[0].leftrect = p[0].leftrect.move(1, 0)
                self.offset_x = self.rect.left - p[0].feetrect.left
                self.offset_y = self.rect.top - p[0].feetrect.top
                self.offset_x2 = self.rect.left - p[0].rightrect.left
                self.offset_y2 = self.rect.top - p[0].rightrect.top
                self.offset_x3 = self.rect.left - p[0].leftrect.left
                self.offset_y3 = self.rect.top - p[0].leftrect.top
            if p[0].leftmask.overlap(self.mask, (self.offset_x3, self.offset_y3)) != None and p[0].deatha == 0 and p[0].acc < 0:
                p[0].acc = 0
                while p[0].leftmask.overlap(self.mask, (self.offset_x3, self.offset_y3)) != None:
                    p[0].rect = p[0].rect.move(1, 0)
                    p[0].feetrect = p[0].feetrect.move(1, 0)
                    p[0].rightrect = p[0].rightrect.move(1, 0)
                    p[0].leftrect = p[0].leftrect.move(1, 0)
                    self.offset_x3 = self.rect.left - p[0].rightrect.left
                    self.offset_y3 = self.rect.top - p[0].rightrect.top
                p[0].rect = p[0].rect.move(-1, 0)
                p[0].feetrect = p[0].feetrect.move(-1, 0)
                p[0].rightrect = p[0].rightrect.move(-1, 0)
                p[0].leftrect = p[0].leftrect.move(-1, 0)
                self.offset_x = self.rect.left - p[0].feetrect.left
                self.offset_y = self.rect.top - p[0].feetrect.top
                self.offset_x2 = self.rect.left - p[0].rightrect.left
                self.offset_y2 = self.rect.top - p[0].rightrect.top
                self.offset_x3 = self.rect.left - p[0].leftrect.left
                self.offset_y3 = self.rect.top - p[0].leftrect.top
            if (p[0].feetmask.overlap(self.mask, (self.offset_x, self.offset_y)) != None) and p[0].grav >= 0 and p[0].deatha == 0:
                p[0].landed = 1
                while (p[0].feetmask.overlap(self.mask, (self.offset_x, self.offset_y)) != None):
                    p[0].rect = p[0].rect.move(0, -1)
                    p[0].feetrect = p[0].feetrect.move(0, -1)
                    p[0].rightrect = p[0].rightrect.move(0, -1)
                    self.offset_x = self.rect.left - p[0].feetrect.left
                    self.offset_y = self.rect.top - p[0].feetrect.top
                p[0].rect = p[0].rect.move(0, 3)
                p[0].feetrect = p[0].feetrect.move(0, 3)
                p[0].rightrect = p[0].rightrect.move(0, 3)

class flag:
    def __init__(self, pos):
        self.image = pygame.image.load("flag.gif")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1] - self.rect.height)
    def move(self, speed):
        self.rect = self.rect.move([speed, 0])
    def collide(self, p):
        if p[0].rect.left <= self.rect.right and p[0].rect.right >= self.rect.left and p[0].rect.bottom <= self.rect.top + 20 and p[0].rect.bottom >= self.rect.top and p[0].grav >=0: #if player lands on top of the bumper
            s[0].Win()
        if p[0].rect.left <= self.rect.right and p[0].rect.right >= self.rect.left and p[0].rect.bottom >= self.rect.top + 20 and p[0].rect.top <= self.rect.bottom:
            s[0].Win()



class baddy1:
    def __init__(self, pos):
        self.images = []
        self.images.append(load_image('pics/baddy1-1.png'))
        self.images.append(load_image('pics/baddy1-2.png'))
        self.images.append(load_image('pics/baddy1-3.png'))
        self.images.append(load_image('pics/baddy1-4.png'))
        self.images.append(load_image('pics/baddy1-5.png'))
        self.images.append(load_image('pics/baddy1-6.png'))
        self.images.append(load_image('pics/baddy1-7.png'))
        self.images.append(load_image('pics/baddy1-8.png'))
        self.images.append(load_image('pics/baddy1-9.png'))
        self.images.append(load_image('pics/baddy1-11.png'))
        self.images.append(load_image('pics/baddy1-11.png'))
        self.images.append(load_image('pics/baddy1-12.png'))
        self.images.append(load_image('pics/baddy1-12.png'))
        self.images.append(load_image('pics/baddy1-13.png'))
        self.images.append(load_image('pics/baddy1-13.png'))
        self.images.append(load_image('pics/baddy1-14.png'))
        self.images.append(load_image('pics/baddy1-14.png'))
        self.images.append(load_image('pics/baddy1-15.png'))
        self.images.append(load_image('pics/baddy1-15.png'))
        self.images.append(load_image('pics/baddy1-16.png'))
        self.images.append(load_image('pics/baddy1-16.png'))
        self.animate = 0
        self.image = self.images[self.animate]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1] - self.rect.height + 7)
        self.patroller = pos[3]
        self.distance = pos[2]
        self.health = 3
        self.deatha = 5
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey((255, 255, 255))
    def AI(self):
        if self.animate == 0 or self.animate == 10:
            self.animate = 20
        else:
            self.animate -= 1
        self.update()
        self.patrol()
    def patrol(self):
        self.patroller += 1
        if self.patroller == self.distance * 2:
            self.patroller = 0
        if 0 <= self.patroller < self.distance:
            self.rect = self.rect.move([1, 0])
        if self.distance <= self.patroller < self.distance * 2:
            self.rect = self.rect.move([-1, 0])
    def move(self, speed):
        self.rect = self.rect.move([speed, 0])
    def collide(self, p):
        self.offset_x = self.rect.left - p[0].rect.left
        self.offset_y = self.rect.top - p[0].rect.top
        if (p[0].mask.overlap(self.mask, (self.offset_x, self.offset_y)) != None):
            p[0].Death()
    def Death(self, i):
        if self.deatha > 0:
            self.deatha -= 1
        else:
            try:
                b1.pop(i)
            except:
                pass
    def update(self):
        self.image = self.images[self.animate]

class baddy2:
    def __init__(self, pos):
        self.images = []
        self.images.append(load_image('pics/baddy2-1.gif'))
        self.images.append(load_image('pics/baddy2-2.gif'))
        self.images.append(load_image('pics/baddy2-3.gif'))
        self.images.append(load_image('pics/baddy2-4.gif'))
        self.images.append(load_image('pics/baddy2-5.gif'))
        self.images.append(load_image('pics/baddy2-6.gif'))
        self.images.append(load_image('pics/baddy2-7.gif'))
        self.images.append(load_image('pics/baddy2-8.gif'))
        self.images.append(load_image('pics/baddy2-9.gif'))
        self.images.append(load_image('pics/baddy2-10.gif'))
        self.images.append(load_image('pics/baddy2-11.gif'))
        self.animate = 0
        self.image = self.images[self.animate]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1] - self.rect.height + 7)
        self.patroller = pos[3]
        self.distance = pos[2]
        self.health = 4
        self.mode = 1
        self.lasertime = 0
        self.direction = 5
        self.rotate = 0
        self.deatha = 5
        self.mask = pygame.mask.from_surface(self.image)
    def AI(self):
        if self.animate > 0:
            self.animate -= 1
            self.update()
        if self.mode == 1:
            self.patrol()
        if self.mode == 2:
            self.hunt()
        if self.lasertime > 0:
            self.lasertime -= 1
    def patrol(self):
        self.patroller += 1
        if self.patroller == self.distance * 2:
            self.patroller = 0
        if 0 <= self.patroller < self.distance:
            self.rect = self.rect.move([0, 1])
        if self.distance <= self.patroller < self.distance * 2:
            self.rect = self.rect.move([0, -1])
        if self.rect.right >= p[0].rect.left - 200 and self.rect.left <= p[0].rect.right + 200:
            self.mode = 2
    def hunt(self):
        if self.rect.bottom >= p[0].rect.top - 100:
            self.rect = self.rect.move(0, -2)
        if self.rect.bottom <= p[0].rect.top - 120:
            self.rect = self.rect.move(0, +2)
        if self.rect.right <= p[0].rect.left - 40:
            self.rect = self.rect.move(+2, 0)
        if self.rect.left >= p[0].rect.right + 40:
            self.rect = self.rect.move(-2, 0)
        if (self.rect.left <= p[0].rect.left <= self.rect.right or self.rect.left <= p[0].rect.right <= self.rect.right) and self.rect.bottom <= p[0].rect.top:
            self.direction = 3
        elif self.rect.left >= p[0].rect.right and self.rect.bottom > p[0].rect.top:
            self.direction = 5
        elif self.rect.left >= p[0].rect.right and self.rect.bottom <= p[0].rect.top:
            self.direction = 4
        elif self.rect.right <= p[0].rect.left and self.rect.bottom <= p[0].rect.top:
            self.direction = 2
        elif self.rect.right <= p[0].rect.left and self.rect.bottom > p[0].rect.top:
            self.direction = 1
        if self.rect.right >= p[0].rect.left - 350 and self.rect.left <= p[0].rect.right + 350 and self.lasertime == 0:
            if self.direction == 4 or self.direction == 5:
                lb.append(LaserB([self.rect.left, (self.rect.top + self.rect.bottom) / 2], self.direction, self.rotate))
            if self.direction == 1 or self.direction == 2:
                lb.append(LaserB([self.rect.right, (self.rect.top + self.rect.bottom) / 2], self.direction, self.rotate))
            if self.direction == 3:
                lb.append(LaserB([(self.rect.left + self.rect.right) / 2, self.rect.bottom], self.direction, self.rotate))
            self.lasertime = 15
            if self.rotate == 0:
                self.rotate = 1
            elif self.rotate == 1:
                self.rotate = 2
            elif self.rotate == 2:
                self.rotate = 0
    def move(self, speed):
        self.rect = self.rect.move([speed, 0])
    def collide(self, p):
        if p[0].rect.left <= self.rect.right and p[0].rect.right >= self.rect.left and p[0].rect.bottom <= self.rect.top + 20 and p[0].rect.bottom >= self.rect.top and p[0].grav >=0: #if player lands on top of the bumper
            p[0].grav = -15
        if p[0].rect.left <= self.rect.right and p[0].rect.right >= self.rect.left and p[0].rect.bottom >= self.rect.top + 20 and p[0].rect.top <= self.rect.bottom:
            p[0].Death()
    def Death(self, i):
        if self.deatha > 0:
            self.deatha -= 1
        else:
            try:
                b2.pop(i)
            except:
                pass
    def update(self):
        self.image = self.images[self.animate]


class LaserB:
    def __init__(self, pos, direction, rotate):
        self.image = pygame.image.load("laserb.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])
        self.direction = direction
        if self.direction == 2:
            self.rect = self.rect.move(-self.rect.width, 0)
            if rotate == 0:
                self.image = pygame.transform.rotate(self.image, 285)
            if rotate == 1:
                self.image = pygame.transform.rotate(self.image, 315)
                self.direction = 6
            if rotate == 2:
                self.image = pygame.transform.rotate(self.image, 345)
                self.direction = 7
        if self.direction == 3:
            self.image = pygame.transform.rotate(self.image, 270)
        if self.direction == 4:
            if rotate == 0:
                self.image = pygame.transform.rotate(self.image, 255)
            if rotate == 1:
                self.direction = 8
                self.image = pygame.transform.rotate(self.image, 225)
            if rotate == 2:
                self.direction = 9
                self.image = pygame.transform.rotate(self.image, 195)
    def logic(self):
            self.move()
            if p[0].rect.left <= self.rect.right and p[0].rect.right >= self.rect.left and self.rect.top <= p[0].rect.bottom and self.rect.bottom >= p[0].rect.top:
                self.Death()
                p[0].Death()
            for i in range(len(floors)):
                if floors[i].rect.left <= self.rect.right and floors[i].rect.right >= self.rect.left and self.rect.top <= floors[i].rect.bottom and self.rect.bottom >= floors[i].rect.top:
                    self.Death()
    def move(self):
        for i in range(5):
            if self.direction == 1:
                self.rect = self.rect.move(4, 0)
            if self.direction == 2:
                self.rect = self.rect.move(2, 2)
            if self.direction == 3:
                self.rect = self.rect.move(0, 4)
            if self.direction == 4:
                self.rect = self.rect.move(-2, 2)
            if self.direction == 5:
                self.rect = self.rect.move(-4, 0)
            if self.direction == 6:
                self.rect = self.rect.move(1, 4)
            if self.direction == 7:
                self.rect = self.rect.move(3, 1)
            if self.direction == 8:
                self.rect = self.rect.move(-1, 4)
            if self.direction == 9:
                self.rect = self.rect.move(-3, 1)

    def Death(self):
        self.rect = self.rect.move(0,1000)



playerpos = [[200, 200, 600]]
floorpos = [[0, 400, 600], [800, 250, 600], [1700, 450, 700], [3200, 400, 500], [4800, 120, 200], [5100, 400, 10000]]
platpos = [[2700, 350], [4000, 300], [4200, 180]]
baddy1pos = [[3400, 400, 400, 200], [5100, 400, 800, 0]]
baddy2pos = [[5500, 250, 100, 100]]
flagpos = [5900,400]

def Garbage():
    for i in range(len(l)):
        try:
            if l[i].rect.left > width or l[i].rect.right < 0:
                l.pop(i)
            l[i].logic()
        except:
            pass

    for i in range(len(g)):
        try:
            if g[i].rect.left > width or g[i].rect.right < 0:
                g.pop(i)
            g[i].logic(i)
        except:
            pass


    for i in range(len(lb)):
        try:
            if lb[i].rect.left > width or lb[i].rect.right < 0:
                lb.pop(i)
            lb[i].logic()
        except:
            pass

def load_image(name):
    image = pygame.image.load(name)
    return image


s = []
s.append(Scrn(width))

l = []
g = []
lb = []

flags = []
flags.append(flag(flagpos))

p = []
for i in range(len(playerpos)):
    p.append(Player(playerpos[i]))

floors = []
for i in range(len(floorpos)):
    floors.append(Floor(floorpos[i]))

platforms = []
for i in range(len(platpos)):
    platforms.append(Platform(platpos[i]))

b1 = []
for i in range(len(baddy1pos)):
    b1.append(baddy1(baddy1pos[i]))

b2 = []
for i in range(len(baddy2pos)):
    b2.append(baddy2(baddy2pos[i]))


clock=pygame.time.Clock() #make a clock

s[0].MusicStart()

while 1: #infinite loop
        for event in pygame.event.get(): #if something clicked
                if event.type == pygame.QUIT: #if EXIT clicked
                        sys.exit() #close cleanly

        clock.tick(60) #limit framerate to 60 FPS
        try:
            s[0].text = s[0].font.render(str(g[0].offset_x), 1, (100, 100, 100))
        except: pass

        p[0].keypress(pygame.key.get_pressed())

        if p[0].pausetimer > 0:
            p[0].pausetimer -= 1

        if not p[0].pause:
            p[0].logic()
            for i in range(len(b1)):
                try:
                    baddy1.AI(b1[i])
                    if b1[i].health <= 0:
                        b1[i].Death(i)
                except:
                    pass
            for i in range(len(b2)):
                try:
                    baddy2.AI(b2[i])
                    if b2[i].health <= 0:
                        b2[i].Death(i)
                except:
                    pass



            Garbage()

            s[0].ScrollAdjust(s)
            s[0].display()
        else:
            pygame.time.wait(10)