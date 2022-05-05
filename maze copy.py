
from cProfile import run
import pygame
MAIN = pygame.display.set_mode((900,600))
WIDTH, HEIGHT = 900,600
BG = (255,255,255)
BLACK=(0,0,0)
FPS=60
V=5
pygame.font.init()
FONT=pygame.font.SysFont('comicsans',32)

def start():
    MAIN.fill(BG)
    running=True
    fonts = FONT.render("Enter level of difficulty of maze : 1, 2 or 3",2,True)
    MAIN.blit(fonts,(140,250))
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            keypress = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 1
                    if event.key == pygame.K_2:
                        return 2
                    if event.key == pygame.K_3:
                        return 3
                    if event.key == pygame.K_4:
                        return 4
                    if event.key == pygame.K_5:
                        pass
                    if event.key == pygame.K_e:
                        pygame.quit()
                    

def tryagain():
    pass
                        


nth_maze=start()

MAZE = pygame.image.load(f"Assets/Images/maze{nth_maze}.png")
MAZE = pygame.transform.scale(MAZE,(HEIGHT,HEIGHT))

f = open(f"Assets/Files/maze{nth_maze}.txt", 'r')
values = f.readlines()
start_x = int(values[0])
start_y = int(values[1])
end_x_1 = int(values[2])
end_x_2 = int(values[3])
end_y_1 = int(values[4])
end_y_2 = int(values[5])
end_axi = int(values[6])
end_mov = int(values[7])
dotsize = int(values[8])

DOT = pygame.image.load("Assets/Images/dot.png")
DOT = pygame.transform.scale(DOT,(dotsize,dotsize))
END = pygame.image.load("Assets/Images/end.png")
END = pygame.transform.scale(END,(480,250))

def draw(dot,check):
    MAIN.fill(BG)
    MAIN.blit(MAZE,(150,0))
    MAIN.blit(DOT,(dot.x,dot.y))
    if(check==1):
        MAIN.blit(END,(210,175))
    pygame.display.update()

def move_dot(keypress,dot):
    
    if((keypress[pygame.K_LEFT] or keypress[pygame.K_a]) and dot.x-V>150):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i-V,dot.y+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.x-=V
        
    if((keypress[pygame.K_RIGHT] or keypress[pygame.K_d]) and dot.x+V<750-dot.width):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i+V,dot.y+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.x+=V

    if((keypress[pygame.K_UP] or keypress[pygame.K_w]) and dot.y-V>0):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i,dot.y-V+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.y-=V
    if((keypress[pygame.K_DOWN] or keypress[pygame.K_s]) and dot.y+V<600-dot.height):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i,dot.y+V+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.y+=V
def check(dot):
    if(dot.x>end_x_1 and dot.x<end_x_2 and dot.y>end_y_1 and dot.y<end_y_2):
        clock = pygame.time.Clock()
        for i in range(0,90,1):
            clock.tick(FPS)
            if(end_axi==0):
                dot.x+=end_mov
            else:
                dot.y+=end_mov
            draw(dot,1)
        clock.tick(10000)
        pygame.quit()



def main():
    running = True
    clock = pygame.time.Clock()
    dot = pygame.Rect(start_x,start_y,dotsize,dotsize)
    MAIN.fill(BG)
    while running:
        clock.tick(FPS)
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if keypress[pygame.K_e]:
                running = False
                pygame.quit()
        
        move_dot(keypress,dot)
        check(dot)
        draw(dot,0)
    pygame.quit()
if __name__ == '__main__':
    main()