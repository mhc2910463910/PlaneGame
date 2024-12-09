# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:18:08 2022

@author: Administrator
"""
#1 python3
import pygame
import sys
import pygame.freetype
from random import randint
from random import choice
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.bullet=pygame.image.load("img/bullet2.png")
        self.bullet_width=30
        self.bullet_height=30
        self.bullet_speed=5
        self.bullet_rect=pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.bullet_rect.midtop=ai_game.plain_rect.midtop
    def draw(self):
        self.screen.blit(self.bullet,self.bullet_rect)
    def run(self):
        self.bullet_rect.y-=self.bullet_speed
class attack(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.attack_img=pygame.image.load("img/attavk_!.png")
        self.attack_rect=self.attack_img.get_rect()
        self.attack_rect.x=randint(20,420)
        self.attack_rect.y=randint(20,40)
        self.attack_speed=1
    def run(self):
        self.attack_rect.y+=self.attack_speed
    def draw(self):
        self.screen.blit(self.attack_img,self.attack_rect)
class plain:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((487,731))
        self.bkimage=pygame.image.load("img/img.png")
        self.plain=pygame.image.load("img/plain_1.png")
        
        self.screen_rect=self.screen.get_rect()
        self.bkimage_rect=self.bkimage.get_rect()
        self.plain_rect=self.plain.get_rect()
        self.plain_rect.midbottom=self.screen_rect.midbottom
        self.speed=5
        
        file=r'music/bgm.mp3'		# 音乐的路径
        pygame.mixer.init()						# 初始化
        pygame.mixer.music.load(file)	# 加载音乐文件
        self.bullets=pygame.sprite.Group()
        self.attacks=pygame.sprite.Group()
        pygame.mixer.music.play()# 开始播放音乐流
        
        pygame.display.set_caption("飞机大战")
    def run(self):
        self.plain_left=False
        self.plain_right=False
        self.plain_up=False
        self.plain_down=False
        number=int(0)
        num=int(0)
        active=True
        flag=1
        while active:
            if num>=70:
                number=int(10)
                num=int(0)
                font=pygame.freetype.Font("font/COOPBL.TTF",size=100)
                while flag:
                    if self.attacks!=0:
                        for i in self.attacks:
                            self.attacks.remove(i)
                    font.render_to(self.screen,(80,400),"WIN GAME",size=50,fgcolor="#FF4500")
                    pygame.display.flip() 
                           
            rand_plain=randint(0,20)
            if number<3:
                if rand_plain==12:
                    Attack=attack(self)
                    Attack.attack_img=pygame.image.load("img/boss.png")
                    Attack.flag=1
                    Attack.bullet_num=5
                    self.attacks.add(Attack)
                    number+=1
                else:
                    Attack=attack(self)
                    Attack.flag=0
                    self.attacks.add(Attack)
                    number+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.plain_left=True
                    if event.key==pygame.K_RIGHT:
                        self.plain_right=True
                    if event.key==pygame.K_UP:
                        self.plain_up=True
                    if event.key==pygame.K_DOWN:
                        self.plain_down=True
                    if event.key==pygame.K_SPACE:
                        bull=Bullet(self)
                        self.bullets.add(bull)
                    
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        self.plain_left=False
                    elif event.key==pygame.K_RIGHT:
                        self.plain_right=False
                    elif event.key==pygame.K_UP:
                        self.plain_up=False
                    elif event.key==pygame.K_DOWN:
                        self.plain_down=False
                        
            if self.plain_left==True:
                if self.plain_rect.left>=self.screen_rect.left:
                    self.plain_rect.x-=self.speed
            if self.plain_right==True:
                if self.plain_rect.right<=self.screen_rect.right:
                    self.plain_rect.x+=self.speed
            if self.plain_up==True:
                if self.plain_rect.top>=self.screen_rect.top:
                    self.plain_rect.y-=self.speed
            if self.plain_down==True:
                if self.plain_rect.bottom<=self.screen_rect.bottom:
                    self.plain_rect.y+=self.speed
            
            self.screen.blit(self.bkimage,self.screen_rect)
            self.screen.blit(self.plain,self.plain_rect)
            for tack in self.attacks.sprites():
                tack.run()
                tack.draw()    
                for bullet in self.bullets.sprites():
                    bullet.draw()
                    bullet.run()
                    if bullet.bullet_rect.x>=tack.attack_rect.x and bullet.bullet_rect.x<=tack.attack_rect.x+80 \
                        and bullet.bullet_rect.y<=tack.attack_rect.y and tack.flag==0:
                            self.bullets.remove(bullet)
                            self.attacks.remove(tack)
                            number-=1
                            num+=1
                    elif bullet.bullet_rect.x>=tack.attack_rect.x and bullet.bullet_rect.x<=tack.attack_rect.x+80 \
                        and bullet.bullet_rect.y<=tack.attack_rect.y and tack.flag==1:
                        self.bullets.remove(bullet)
                        tack.bullet_num-=1
                        if tack.bullet_num==0:
                            self.attacks.remove(tack)
                            num+=1
                    if tack.attack_rect.y>730:
                        self.attacks.remove(tack)
                        number-=1
            font=pygame.freetype.Font("font/COOPBL.TTF",size=100)
            font.render_to(self.screen,(200,50),str(num),fgcolor="#97ffff") 
            
            pygame.display.flip()
if __name__=='__main__':
    game=plain()
    game.run()
            
            
            
            
            
            
            
            
            
            