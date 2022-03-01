import time
import pygame

WIDTH, HEIGHT = 900,600
BG = (255,255,255)
BLACK=(0,0,0)
FPS=60
V=5

MAIN = pygame.display.set_mode((900,600))

MAZE = pygame.image.load("Assets/Images/maze1.png")
MAZE = pygame.transform.scale(MAZE,(HEIGHT,HEIGHT))
DOT = pygame.image.load("Assets/Images/dot.png")
DOT = pygame.transform.scale(DOT,(50,50))
END = pygame.image.load("Assets/Images/end.png")
END = pygame.transform.scale(END,(480,250))

f = open("Assets/Files/maze1.txt", 'r')
values = f.readlines()
start_x = int(values[0])
start_y = int(values[1])
end_x_1 = int(values[2])
end_x_2 = int(values[3])
end_y_1 = int(values[4])
end_y_2 = int(values[5])
end_axi = int(values[6])
end_mov = int(values[7])
start_a = int(values[8])
start_d = int(values[9])
def draw(dot,check):
    MAIN.fill(BG)
    MAIN.blit(MAZE,(150,0))
    MAIN.blit(DOT,(dot.x,dot.y))
    if(check==1):
        MAIN.blit(END,(210,175))
    pygame.display.update()
def start(dot):
   
    clock = pygame.time.Clock()
    if(start_a==0):
        dot.x-=start_d*90
    if(start_a==1):
        dot.y-=start_d*90
        i=0
    while(i<90):
        clock.tick(FPS*3000)
        if(start_a==0):
            dot.x+=start_d
        else:
            dot.y+=start_d
        draw(dot,0)
        i+=1
    draw(dot,0)
def move_dot(keypress,dot):
    
    if(keypress[pygame.K_LEFT] and dot.x-V>150):
        cnt=0
        i=0
        while(i<=dot.width):
            j=0
            while(j<=dot.height):
                color= MAIN.get_at((dot.x+i-V,dot.y+j))
                if(color[0]<100 and color[1]<100 and color[2]<100) :
                    cnt=1
                j+=1
            i+=1
        if(cnt==0):
            dot.x-=V
        
    if(keypress[pygame.K_RIGHT] and dot.x+V<750-dot.width):
        cnt=0
        i=0
        while(i<=dot.width):
            j=0
            while(j<=dot.height):
                color= MAIN.get_at((dot.x+i+V,dot.y+j))
                if(color[0]<100 and color[1]<100 and color[2]<100) :
                    cnt=1
                j+=1
            i+=1
        if(cnt==0):
            dot.x+=V
    if(keypress[pygame.K_UP] and dot.y-V>0):
        cnt=0
        i=0
        while(i<=dot.width):
            j=0
            while(j<=dot.height):
                color= MAIN.get_at((dot.x+i,dot.y-V+j))
                if(color[0]<100 and color[1]<100 and color[2]<100) :
                    cnt=1
                j+=1
            i+=1

        if(cnt==0):
            dot.y-=V
    if(keypress[pygame.K_DOWN] and dot.y+V<600-dot.height):
        cnt=0
        i=0
        while(i<=dot.width):
            j=0
            while(j<=dot.height):
                color= MAIN.get_at((dot.x+i,dot.y+V+j))
                if(color[0]<100 and color[1]<100 and color[2]<100) :
                    cnt=1
                j+=1
            i+=1
        if(cnt==0):
            dot.y+=V
def check(dot):
    if(dot.x>end_x_1 and dot.x<end_x_2 and dot.y>end_y_1 and dot.y<end_y_2):
        
        i=0
        clock = pygame.time.Clock()
        while(i<90):
            clock.tick(FPS*3000)
            if(end_axi==0):
                
                dot.x+=end_mov
            else:
                
                dot.y+=end_mov
            draw(dot,1)
            i+=1
        pygame.quit()
    

def main():
    running = True
    clock = pygame.time.Clock()
    dot = pygame.Rect(start_x,start_y,50,50)
    MAIN.fill(BG)
    start(dot)
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        keypress = pygame.key.get_pressed()
        move_dot(keypress,dot)
        check(dot)
        draw(dot,0)
    pygame.quit()
if __name__ == '__main__':
    main()