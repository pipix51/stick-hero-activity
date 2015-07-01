#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Stick Hero
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com




import os
import gtk
import pickle
import pygame
import sys

from math import *



class game:

    def make(self):
        
        pygame.init()
        sound=True
        
        try:
            pygame.mixer.init()
        except Exception, err:
            sound=False
            print 'error with sound', err
            
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
            
        crashed=False   
        disp_width = 600
        disp_height = 600
            
        press=0    
        
        info=pygame.display.Info()
        gameDisplay=pygame.display.get_surface()
        
        
        if not(gameDisplay):
            
            gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
            #pygame.display.set_caption("Stick Hero")
            #gameicon=pygame.image.load('data/images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        hero=pygame.image.load("images/hero.png")
        
        #herotr=hero
        herotr=pygame.transform.scale(hero,(30,26))
        
        hero1=pygame.image.load("images/hero1.png")
        hero2=pygame.image.load("images/hero2.png")
        hero3=pygame.image.load("images/hero3.png")
        stick=pygame.image.load("images/stick.png")
        background=pygame.image.load("images/background.png")
        alpha=pygame.image.load("images/alpha.png")
        beta=pygame.image.load("images/beta.png")
        gamma=pygame.image.load("images/gamma.png")
        delta=pygame.image.load("images/delta.png")
        
        
        back1=pygame.image.load("background/back1.png").convert()
        back1a=pygame.transform.scale(back1,(1280,720))
        back1b=back1a
        
        #stickx1=455
        #sticky1=50
        
        herokicklist=[hero,herotr]
        
        herolist=[hero,hero1,hero2,hero3]
        
        
        pillarlist=[alpha,beta,gamma,delta]
        
        stickx1=stickx=455
        sticky1=sticky=472
        
        anglenum=90
        angle=(pi/180)*anglenum
        
        sticklength=0
        
        time=0
        flag=0          #stick fall flag
        keypressflag=0
        
        moveit=0  #hero move flag
        
        herox=420
        heroy=442
        
        i=0
        j=0
        k=0
        
        pillar1x=355
        pillar2x=650
        
        pillar1=alpha
        pillar2=beta
        
        herofall=0
        herofallflag=0
        
        pillarmoveflag=0
        
        stickmove=0
        
        backx=0
        
        pillarfound=0
        
        
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
            #totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                crashed=True
                
            
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print event
            
                
            gameDisplay.fill(white)
            gameDisplay.blit(back1a,(250+backx,0))
            #gameDisplay.blit(background,(350,0))
            
            
            i+=1
            if(i%4==0):
                j+=1
            
            if(j==4):
                j=0
                
                
            if(moveit==1):    
                gameDisplay.blit(herolist[j],(herox,heroy))
            
            if(moveit==0):
                
                if(k<=6):
                    gameDisplay.blit(herokicklist[0],(herox,heroy))
                if(k<=12):
                    gameDisplay.blit(herokicklist[1],(herox-1,heroy+2))
                
                if(keypressflag==1):
                    k+=1
                if(k==12):
                    k=0
                    
                    
                    
            
            if(moveit==1):
                herox+=3
                backx-=1
            
            
           
            
            
            
            
            
            
            gameDisplay.blit(pillar1,(pillar1x,470))
            
            gameDisplay.blit(pillar2,(pillar2x,470))
            
            
            
            
           
            
            
            
            
            
            if(flag==0):
                
                if(stickx==stickx1):
                    sticklength=abs(sticky-sticky1)
                if(sticky==sticky1):
                    sticklength=abs(stickx1-stickx)
            
            if(anglenum>0 and flag==1 ):
                
                anglenum-=0.03*(time)*(time)
                if(anglenum<=0):
                    
                    anglenum=0
                    sticky1=472
                    stickx1=stickx+sticklength
                    #sticklength=stickx1-stickx
                    flag=0
                    moveit=1
                    time=0
                    
                    colortest=gameDisplay.get_at((460+sticklength,heroy+30))
                    
                    if not((colortest[0]==0 and colortest[1]==0 and colortest[2]==0) or (colortest[0]==1 and colortest[1]==1 and colortest[2]==1) or colortest[0]==255):
                        herofallflag=1
                        
                    
                    
                    
                #if(anglenum<0):
                #    break
                
                #if(anglenum>85):
                time+=1
                
            print sticklength
            
            if(herofall==1):
                
                
                if(anglenum>-90):
                    anglenum-=0.03*(time)*(time)
                    
                    #print "hey"
                    
                    if(anglenum<=-90):
                        
                        #print "hey"
                        anglenum=-90
                        sticky1=sticky+sticklength
                        stickx1=455
                        #sticklength=stickx1-stickx
                        #flag=0
                        moveit=1
                        time=0
                    
                    
                    
                    time+=1
            
                
                
            
            angle=(pi/180)*anglenum
            
            if event.type==pygame.KEYDOWN and event.key==273:
                #jump.play(0)
                
                keypressflag=1
              
              
            if keypressflag==1:  
                
                sticky1-=5
                
                
                
                
            if event.type==pygame.KEYUP  and event.key==273:
                flag=1
                keypressflag=0
                #print "fuck"
                
            
            
            
            
            
            
            
            
            
            if(flag==1):
                sticky1=472-sticklength*sin(angle)
                stickx1=455+sticklength*cos(angle)
                
            
            
            
            
            
            if(stickx<=349):
                
                stickmove=0
                stickx1=stickx=455
                sticky1=sticky=472
            
            if((stickx1-stickx)!=0 or sticky1-sticky!=0):
                pygame.draw.line(gameDisplay,black,(stickx1,sticky1),(stickx,sticky), 6)
            
            
            
            
            
            pygame.draw.circle(gameDisplay,white, (herox+30,heroy+30) ,3, 2)
            pygame.draw.circle(gameDisplay,white, (457+sticklength,heroy+30) ,3, 2)
            
            
            
            #if hero has to fall
            
            if((herox+30)>=457+sticklength and herofallflag==1):
                herofall=1
                moveit=0
                flag=1
                
            
            #if hero has to stop
            if((herox+30)>=457+sticklength and herofallflag==0):
                
                color=gameDisplay.get_at((herox+30,heroy+30))
                
                if(color[0]!=0 and color[0]!=1 and color[0]!=255):
                    moveit=0
                    pillarmoveflag=1
                    stickmove=1
                    
                    
                
            
            #pillar movement condition check
            
            pygame.draw.circle(gameDisplay,white,(462,478),3,2)
            
            
            if(moveit==0 and pillarmoveflag==1):
                
                color=gameDisplay.get_at((462,478))
                if((color[0]!=0 and color[0]!=1) or pillarfound==1):
                
                    pillar1x-=3
                    pillar2x-=3
                    
                    if(stickmove==1):
                        stickx1-=3
                        stickx-=3
                    
                    herox-=3
                    #print "help"
                    
                    
                else:
                    pillarfound=1
                    
                    
                if(color[0]!=0 and color[0]!=1 and pillarfound==1):    
                    pillarmoveflag=0
                    
                    color=gameDisplay.get_at((450,472))
                    
                    
            
                    
            pygame.draw.rect(gameDisplay,black,(0,0,349,768))    
                    
            pygame.draw.rect(gameDisplay,black,(840,0,693,768))
            
            
            
                
            
            if(herofall==1):
                
                heroy+=15
            
            
            
            pygame.display.update()
            clock.tick(60)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
     
     
     
     
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()
            

if __name__ == "__main__":
    g = game()
    g.make()         

            