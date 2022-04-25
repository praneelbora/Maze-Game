
import pygame

WIDTH, HEIGHT = 900,600
BG = (255,255,255)
BLACK=(0,0,0)
FPS=60
V=5
MAZE = pygame.image.load("Assets/Images/maze4.png")
MAZE = pygame.transform.scale(MAZE,(HEIGHT,HEIGHT))

f = open("Assets/Files/maze4.txt", 'r')
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
MAIN = pygame.display.set_mode((900,600))

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
    
    if(keypress[pygame.K_LEFT] and dot.x-V>150):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i-V,dot.y+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.x-=V
        
    if(keypress[pygame.K_RIGHT] and dot.x+V<750-dot.width):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i+V,dot.y+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.x+=V

    if(keypress[pygame.K_UP] and dot.y-V>0):
        cnt=0
        for i in range(0,dot.width,1):
            for j in range (0,dot.height,1):
                color= MAIN.get_at((dot.x+i,dot.y-V+j))
                if(color[0]<100):
                    cnt=1
        if(cnt==0):
            dot.y-=V
    if(keypress[pygame.K_DOWN] and dot.y+V<600-dot.height):
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
        pygame.quit()


def main():
    running = True
    clock = pygame.time.Clock()
    dot = pygame.Rect(start_x,start_y,dotsize,dotsize)
    MAIN.fill(BG)
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