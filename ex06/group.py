
import pygame as pg
from pygame.locals import *
import sys
import random

#ディスプレイの描画設定
class Display:
    def __init__(self, title, wh, col):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.Surface((1600,900))
        self.bgi_sfc.fill(col)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

#ゲーム内で表示される岩盤の描画
class Ganban:
    def __init__(self):
        self.gx_size = 250
        self.gy_size = 200
        self.dig_count = 0
        self.dig_impct = 8
        self.kiban_size = pg.Rect(20,20,1000,800)
        self.color_list = [[255,255,255],[210,105,30],[160,82,45],[139,69,19]]
        self.rock = [[random.randint(1,3) for i in range(self.gx_size)] for j in range(self.gy_size)]
        self.kiban_sfc = pg.Surface((self.gx_size*4,self.gy_size*4))
        self.kiban_sfc.set_alpha(255)
        self.kiban_sfc.set_colorkey([255,255,255])
        self.kiban_rct = self.kiban_sfc.get_rect()
        self.dig_size = 45
        for y in range(self.gy_size):
            for x in range(self.gx_size):
                g_c = self.rock[y][x]
                pg.draw.rect(self.kiban_sfc,(self.color_list[g_c][0],self.color_list[g_c][1],self.color_list[g_c][2]),(((4*x)),(4*y),4,4))

    def dig(self):
        x,y = pg.mouse.get_pos()
        self.pos_x = x//4
        self.pos_y = y//4
        self.dig_count += self.dig_impct
        self.dig_list = []
        self.big_list_x = [[i for i in range(-1*(2+(self.dig_size//4-abs(j-self.dig_size//2))),5+(self.dig_size//4-abs(j-self.dig_size//2)))] for j in range(self.dig_size)]
        self.big_list_y = [i for i in range(-1*(self.dig_size//2),(self.dig_size//2)+5)]
        for y in range(len(self.big_list_x)):
            for x in range(len(self.big_list_x[y])):
                self.big_list_x[y][x] += self.pos_x

        for y in range(len(self.big_list_x)):
            p_y = self.big_list_y[y]
            for x in range(len(self.big_list_x[y])):
                p_x = self.big_list_x[y][x]
                try:
                    self.rock[self.pos_y + p_y][p_x] -= 1
                    g_c = self.rock[self.pos_y + p_y][p_x]
                    if g_c < 0 :
                        g_c = 0
                    pg.draw.rect(self.kiban_sfc,(self.color_list[g_c][0],self.color_list[g_c][1],self.color_list[g_c][2]),(((4*p_x)),(4*(self.pos_y + p_y)),4,4))
                except IndexError:
                    print("out of Index")

    def size_chang(self,size):
        if size == "big":
            self.dig_size = 45
            self.dig_impct = 8
        elif size == "small":
            self.dig_size = 15
            self.dig_impct = 2

    def bilt(self,dis:Display):
        dis.sfc.blit(self.kiban_sfc,(20,20,1000,800),self.kiban_rct)

#こうかとん、HPバーなどの描画
class Object:
    def __init__(self,dis:Display):
        self.big_btn = pg.Rect(1100,50,200,100)
        self.sml_btn = pg.Rect(1350,50,200,100)
        pg.draw.rect(dis.bgi_sfc,(255,0,0),self.big_btn)
        pg.draw.rect(dis.bgi_sfc,(0,255,0),self.sml_btn)
        self.HPbar_sfc = pg.Surface((1000,50))
        self.HPbar_rct = self.HPbar_sfc.get_rect()
        for i in range(500):
            pg.draw.rect(self.HPbar_sfc,(255,0,0),(i*2,0,2,50))
    
    def HP_chang(self,gbn:Ganban): #HPバーの処理
        for i in range(500,500-gbn.dig_count,-1):
            pg.draw.rect(self.HPbar_sfc,(0,0,255),(i*2,0,2,50))

    def yakitori(self,image,size,pos):
        self.yakitori_img_sfc = pg.image.load(image)
        self.yakitori_img_sfc = pg.transform.rotozoom(self.yakitori_img_sfc,0,size)
        self.yakitori_img_rct = self.yakitori_img_sfc.get_rect()
        self.yakitori_img_rct.center = pos

    def bilt(self,dis:Display):
        dis.sfc.blit(dis.bgi_sfc, dis.bgi_rct)
        dis.sfc.blit(self.HPbar_sfc,(20,830,1000,50),self.HPbar_rct)
        dis.sfc.blit(self.yakitori_img_sfc,self.yakitori_img_rct)

#スタート画面の描画
class Start:
    def __init__(self,image,dis:Display):
        self.start_img_sfc = pg.image.load(image)
        self.start_img_sfc = pg.transform.scale(self.start_img_sfc,(1600,900))
        self.start_img_rct = self.start_img_sfc.get_rect()
        while True:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    return
            dis.sfc.blit(self.start_img_sfc,self.start_img_rct)
            pg.display.update()




def main():
    clock = pg.time.Clock()
    dis = Display("甦れコウカトン", (1600, 900), (0,0,0))
    gbn = Ganban()
    obj = Object(dis)
    obj.yakitori("ex03/fig/6.png", 2.0,(random.randint(70,gbn.kiban_sfc.get_width()-50), random.randint(70,gbn.kiban_sfc.get_height()-50)))
    Start("ex03/fig/こうかとん.PNG", dis)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            if event.type == pg.MOUSEBUTTONDOWN:  
                if obj.big_btn.collidepoint(event.pos):
                    print("red button was pressed")  #赤色のボタンが押された場合、割る大きさが大きくなる
                    gbn.size_chang("big")
                if obj.sml_btn.collidepoint(event.pos):
                    print("green button was pressed")  #緑色のボタンが押された場合、割る大きさが小さくなる
                    gbn.size_chang("small")
                if gbn.kiban_size.collidepoint(event.pos):
                    gbn.dig()
                    obj.HP_chang(gbn)

        dis.blit()
        obj.bilt(dis)
        gbn.bilt(dis)
        pg.display.update()

        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()