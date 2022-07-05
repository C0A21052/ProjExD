import pygame as pg
import sys
import random
def check_bound(rct,scr_rct):
    yoko, tate = +1,+1
    if rct.left < scr_rct.left or scr_rct.right<rct.right:
        yoko=-1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate=-1
    return yoko,tate
def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()

    bgimg_sfc=pg.image.load("ex03/fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)
    
    kkimg_sfc = pg.image.load("ex03/fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400
    
    ov_sfc = pg.image.load("ex03/fig/ov.jpg")
    ov_sfc = pg.transform.rotozoom(ov_sfc, 0, 2.0)
    ov_rct = ov_sfc.get_rect()
    ov_rct.center = 800,200 

    ka_sfc = pg.image.load("ex03/fig/kaopng.png")
    ka_sfc = pg.transform.rotozoom(ka_sfc, 0, 2.0)
    ka_rct = ka_sfc.get_rect()
    ka_rct.center = 1000,200 

    bmimg_sfc = pg.Surface((20,20))
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centery = random.randint(0,screen_rct.height)
    vx, vy = +1, +1

    bmimg2_sfc = pg.Surface((20,20))
    bmimg2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg2_sfc,(255,0,0),(10,10),10)
    bmimg2_rct = bmimg2_sfc.get_rect()
    bmimg2_rct.centery = random.randint(0,screen_rct.height)
    vx2, vy2 = +2, +2

    while True:
        life = 3
        
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.K_u:
                screen_sfc.blit(ov_sfc,ov_rct)
                return
                
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: 
            kkimg_rct.centery -=2
        if key_states[pg.K_DOWN] == True: 
            kkimg_rct.centery +=2
        if key_states[pg.K_LEFT] == True: 
            kkimg_rct.centerx -=2
        if key_states[pg.K_RIGHT] == True: 
            kkimg_rct.centerx +=2
        if check_bound(kkimg_rct, screen_rct) != (1,1):
            if key_states[pg.K_UP] == True: 
               kkimg_rct.centery +=2
            if key_states[pg.K_DOWN] == True: 
                kkimg_rct.centery -=2
            if key_states[pg.K_LEFT] == True: 
                kkimg_rct.centerx +=2
            if key_states[pg.K_RIGHT] == True: 
                kkimg_rct.centerx -=2

        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        
        bmimg_rct.move_ip(vx,vy)
        vx+=0.01
        vy+=0.01
       
        bmimg2_rct.move_ip(vx2,vy2)
        vx2+=0.01
        vy2+=0.01
       
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        screen_sfc.blit(bmimg2_sfc,bmimg2_rct)
    
        yoko,tate= check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate
    
        if kkimg_rct.colliderect(bmimg_rct):
            screen_sfc.blit(ka_sfc,ka_rct)
            life -= 1
            if life <=0:
                return
        yoko,tate= check_bound(bmimg2_rct,screen_rct)
        vx2 *= yoko
        vy2 *= tate
       
        if kkimg_rct.colliderect(bmimg2_rct):
            screen_sfc.blit(ka_sfc,ka_rct)
            life -= 1
            if life <=0:
                return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()