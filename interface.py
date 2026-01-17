import pygame 
import sys
from dataclasses import dataclass
from main import new_cube,move_L,move_B,move_D,move_F,move_R,move_U


@dataclass
class FrontView:
    x:int
    y:int
    width: int
    height:int 
    d:int
    
    face:int
    i:int
    j:int

    def points(self):
        return[
            (self.x, self.y),
            (self.x, self.y+self.height),
            (self.x + self.width, self.y + self.height+self.d),
            (self.x + self.width, self.y+self.d),
        ]
    
    def draw(self,screen:pygame.Surface,cube):
        color= cube[self.face][self.i][self.j]
        pygame.draw.polygon(screen,color,self.points())

@dataclass
class LeftView:
    x:int
    y:int
    width: int
    height:int 
    d:int
    
    face:int
    i:int
    j:int

    def points(self):
        return[
            (self.x, self.y),
            (self.x, self.y+self.height),
            (self.x + self.width, self.y + self.height-self.d),
            (self.x + self.width, self.y-self.d),
        ]
    
    def draw(self,screen:pygame.Surface,cube):
        color=cube[self.face][self.i][self.j]
        pygame.draw.polygon(screen,color,self.points())

@dataclass
class TopView:
    x:int
    y:int
    width: int
    height:int 
    d:int
    face:int
    i:int 
    j:int 

    def points(self):
        return[
            (self.x , self.y),
            (self.x + self.width, self.y + self.height),
            (self.x + 2*self.width , self.y),
            (self.x + self.width, self.y - self.height),
        ]
    
    def draw(self,screen:pygame.Surface,cube):
        color=cube[self.face][self.i][self.j]
        pygame.draw.polygon(screen,color,self.points())


class App:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,700))
        self.cube=new_cube()

        self.front_view=[
            FrontView(
                120+35*i ,
                150+13*i + 45*j,
                28,
                40,
                10,
                2,j,i
            )
            for i in range(3)
            for j in range (3)
        ]

        self.left_view=[
            LeftView(
                235 +33*j,
                185+46*i -13*j ,
                28,
                40,
                10,
                4,i,j
            )
            for i in range(3)
            for j in range (3)
        ]
        self.top_view=[
            TopView( 
                120 + 36*i +40*j,
                140 + 12*i - 12*j,
                28,
                10,
                20,
                0,j,i
            )
            for i in range(3)
            for j in range(3)
        ]

        self.back_view=[
            FrontView(
                420+35*i ,
                150-13*i + 45*j,
                28,
                40,
                -10,
                3,j,2-i
            )
            for i in range(3)
            for j in range (3)
        ]

        self.right_view=[
            LeftView(
                535 +33*j,
                115+46*i +13*j ,
                28,
                40,
                -10,
                5,i,2-j
            )
            for i in range(3)
            for j in range (3)
        ]
        self.bottom_view=[
            TopView( 
                420 + 36*i +40*j,
                290 + 12*i - 12*j,
                28,
                10,
                20,
                1,i,2-j
            )
            for i in range(3)
            for j in range(3)
        ]
        
    def process_events(self,event:pygame.event.Event,cube):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_u:
                move_U(cube)
            if event.key==pygame.K_d:
                move_D(cube)
            if event.key==pygame.K_f:
                move_F(cube)
            if event.key==pygame.K_b:
                move_B(cube)
            if event.key==pygame.K_l:
                move_L(cube)
            if event.key==pygame.K_r:
                move_R(cube)
        

    def draw(self):
        for view in self.front_view:
            view.draw(self.screen,self.cube)

        for view in self.left_view:
            view.draw(self.screen,self.cube)

        for view in self.top_view:
            view.draw(self.screen,self.cube)
        
        for view in self.back_view:
            view.draw(self.screen,self.cube)

        for view in self.right_view:
            view.draw(self.screen,self.cube)

        for view in self.bottom_view:
            view.draw(self.screen,self.cube)
        

    def run(self):
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                self.process_events(event,self.cube)
            self.screen.fill((0,0,0))

            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 1000, 700))
            self.draw()
            pygame.display.flip()



App().run()
