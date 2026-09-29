import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    clock.tick(200)
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kokaton_img = pg.image.load("fig/3.png")
    kokaton_img = pg.transform.flip(kokaton_img,True,False)
    tmr = 0
    x = 1
    
    kk_rct = kokaton_img.get_rect() 
    kk_rct.center = 300, 200 
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        y=-1
        z=0
        key_lst = pg.key.get_pressed() 
        if key_lst[pg.K_UP]: 
            z+=-1
        if key_lst[pg.K_DOWN]:
            z+=1
        if key_lst[pg.K_LEFT]: 
            y+=-1
        if key_lst[pg.K_RIGHT]: 
            y+=2
        
        kk_rct.move_ip((y, z))

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kokaton_img, kk_rct)
        pg.display.update()
        if x > 3199:
            x = 0
        else:
            x += 1
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()