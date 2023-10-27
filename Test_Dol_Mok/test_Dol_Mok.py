
pan = [[-1 for i in range(7)] for i in range(7)]

dr = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

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
        
def win():
    count = 0
    for i in range(7):
        for j in range(7):

            if pan[i][j] != -1:
                a = check(i,j) 
                if a != None:
                    return a






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

def rotate(arr,dr):
    if dr==1:
        return list(map(list,zip(*arr[::-1])))
    elif dr==2:
        return list(map(list,zip(*list(map(list,zip(*list(map(list,zip(*arr[::-1])))[::-1])))[::-1])))
    else:
        return arr



def main():
    global pan
    cnt = 0
    
    while True:
        print(*pan,sep="\n")
        x,y,d=map(int,input("first\n" if cnt%2==0 else "Second\n").split())
        cnt+=1
        #좌표와 방향(0이면 유지, 1이면 시계방향으로, 2면 반시계로)
        if pan[x][y]!=-1:
            cnt-=1
            continue
        else:
            pan[x][y] = cnt%2
        gravity(0)
        pan = rotate(pan,d)
        if d!=0:
            gravity(0)
        k = win()
        if k!=None:
            print("The winner is",end = "")
            print(("first" if cnt%2==0 else "Second"),win)
            break
        
        
            
main()
            
        
        
        
        
                
