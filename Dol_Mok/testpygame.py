import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
font = pygame.font.Font("Chilgok_Cye.ttf",80)

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
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def before_start():
    

    global flag, dr
    pygame.init()
    #font = pygame.font.Font("Dol_Mok\Chilgok_Cye.ttf",80)

    #SURFACE = pygame.display.set_mode((1200,900))
    #FPSCLOCK = pygame.time.Clock()
    
    for i in range(7):
        for j in range(7):
            pan[i][j]=-1 
  
    pygame.display.set_caption("돌목")
    flag = False
    dr = 0



def check(x,y):
    
    if y<4:
        for i in range(4):#가로줄 4칸인지
            if pan[x][y+i]!=pan[x][y]:
                break
        else:
            return pan[x][y]
        
    if x<4:
        for i in range(4):#세로줄 4칸인지
            if pan[x+i][y]!=pan[x][y]:
                break
        else:
            return pan[x][y]
            
    if x>2 and y<4:#오른쪽 위 대각선
        for i in range(4):
            if pan[x-i][y+i]!=pan[x][y]:
                break
        else:
            return pan[x][y]

    if x<4 and y<4:
        for i in range(4):#오른쪽 아래 대각선
            if pan[x+i][y+i]!=pan[x][y]:
                break
        else:
            return pan[x][y]


        
def show_dol():
        
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


def win():
    count = 0
    for i in range(7):
        for j in range(7):
            if pan[i][j] != -1:
                a = check(i,j) 
                if a != None:
                    
                    return a     
                               
                

def game_end(k):
    if k != None:
        
        SURFACE.fill((0,0,0))
        show_dol()
        if k==0:
            k = "Red"
        else:
            k = "Yellow"
        text_Title= font.render(k+"win", True, 0xd0fc5c)
        
        SURFACE.blit(text_Title,[400,400])
        text = font.render("Press the SPACE to Restart", True,0xd0fc5c)
        SURFACE.blit(text,[200,500])
        
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        before_start()
                        
                        show_dol()
                        
                        main()
                        




            
        





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
                
            elif event.type == pygame.KEYDOWN and flag == True:
                if event.key==pygame.K_LEFT:
                    dr-=1
                    flag = False
                    cnt+=1
                elif event.key==pygame.K_RIGHT:
                    dr+=1
                    flag = False
                    cnt+=1
                elif event.key == pygame.K_DOWN:
                    flag = False
                    cnt+=1
        
        game_end(win())
        
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
        show_dol()
        gravity(dr)
        
        game_end(win())
        

        pygame.display.update()
        FPSCLOCK.tick(60)


if __name__ == '__main__':
    main()
