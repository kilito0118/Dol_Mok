import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
font = pygame.font.Font("Dol_Mok\Chilgok_Cye.ttf",80)

SURFACE = pygame.display.set_mode((1200,900))
FPSCLOCK = pygame.time.Clock()
Dol_Color = [0xFF0000, 0xFFFF00]
pan = [[-1 for i in range(7)] for i in range(7)]
force = [([400, 870], [500, 870], [450, 830]),
         ([870, 400], [870, 500], [830,450]),
        ([450, 70], [400, 30], [500, 30]), 
        ([30, 400], [30, 500], [70, 450])
        ]
pygame.display.set_caption("돌목")
flag = False
dr = 0
def gravity(Direction : int):
    for i in range(7):
        match Direction:
            case 0:  #아래
                for i in range(5,-1,-1):
                    for j in range(6,-1,-1):
                        if pan[i][j]!=-1 and pan[i+1][j]==-1:
                            pan[i+1][j]=pan[i][j]
                            pan[i][j]=-1
            case 1: #오른쪽
                for j in range(5,-1,-1):
                    for i in range(6,-1,-1):
                        if pan[i][j]!=-1 and pan[i][j+1]==-1:
                            pan[i][j+1]=pan[i][j]
                            pan[i][j]=-1
            case 2: #위
                for i in range(1,7):
                    for j in range(7):
                        if pan[i][j]!=-1 and pan[i-1][j]==-1:
                            pan[i-1][j]=pan[i][j]
                            pan[i][j]=-1                             
            case 3: #왼쪽
                for i in range(7):
                    for j in range(1,7):
                        if pan[i][j]!=-1 and pan[i][j-1]==-1:
                            pan[i][j-1]=pan[i][j]
                            pan[i][j]=-1   




def main():
    global dr, flag
    cnt=0



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and flag == False:
                if event.pos[0]>800 or event.pos[1]>800:
                    continue 
                if pan[event.pos[1]//100-1][event.pos[0]//100-1]==-1:
                    pan[event.pos[1]//100-1][event.pos[0]//100-1] = cnt%2
                    
                    gravity(dr)
                    flag = True

                        
                else:
                    continue
                cnt+=1
            elif event.type == pygame.KEYDOWN and flag == True:
                if event.key==pygame.K_LEFT:
                    dr-=1
                    flag = False

                elif event.key==pygame.K_RIGHT:
                    dr+=1
                    flag = False
                
        if dr==-1:
            dr = 3
        elif dr==4:
            dr = 0
        SURFACE.fill((0,0,0))
        if cnt%2==0:
            text_Title= font.render("Red 턴", True, 0xd0fc5c)
        else:
            text_Title= font.render("Yellow 턴", True, 0xd0fc5c)
        pygame.draw.polygon(SURFACE, 0xd0fc5c, force[dr])
        SURFACE.blit(text_Title,[850,80])
        gravity(dr)
        for i in range(7):
            for j in range(7):
                if pan[i][j]==1:
                    pygame.draw.circle(SURFACE,Dol_Color[1], ((j+1)*100+50,(i+1)*100+50), 40)
                elif pan[i][j]==0:
                    pygame.draw.circle(SURFACE,Dol_Color[0], ((j+1)*100+50,(i+1)*100+50), 40)
        
        for xpos in range(100,900,100):
            pygame .draw.line(SURFACE, 0xFFFFFF, (xpos, 100), (xpos ,800))

        for ypos in range(100,900,100):
            pygame.draw.line(SURFACE, 0xFFFFFF, (100,ypos), (800,ypos))

        
                    

        pygame.display.update()
        FPSCLOCK.tick(60)


if __name__ == '__main__':
    main()
