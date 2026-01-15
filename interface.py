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
    color: tuple

    def points(self):
        return[
            (self.x, self.y),
            (self.x, self.y+self.height),
            (self.x + self.width, self.y + self.height+self.d),
            (self.x + self.width, self.y+self.d),
        ]
    
    def draw(self,screen:pygame.Surface):
        pygame.draw.polygon(screen,self.color,self.points())

@dataclass
class LeftView:
    x:int
    y:int
    width: int
    height:int 
    d:int
    color: tuple

    def points(self):
        return[
            (self.x, self.y),
            (self.x, self.y+self.height),
            (self.x + self.width, self.y + self.height-self.d),
            (self.x + self.width, self.y-self.d),
        ]
    
    def draw(self,screen:pygame.Surface):
        pygame.draw.polygon(screen,self.color,self.points())

@dataclass
class TopView:
    x:int
    y:int
    width: int
    height:int 
    d:int
    color: tuple

    def points(self):
        return[
            (self.x , self.y),
            (self.x + self.width, self.y + self.height),
            (self.x + 2*self.width , self.y),
            (self.x + self.width, self.y - self.height),
        ]
    
    def draw(self,screen:pygame.Surface):
        pygame.draw.polygon(screen,self.color,self.points())


class App:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,700))
        cube=new_cube()
        """move_R(cube)
        move_U(cube)
        move_U(cube)"""

        self.front_view=[
            FrontView(
                120+35*i ,
                150+13*i + 45*j,
                28,
                40,
                10,
                cube[2][j][i]
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
                cube[4][i][j]
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
                cube[0][j][i]
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
                cube[3][j][i]
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
                cube[5][i][j]
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
                cube[1][j][i]
            )
            for i in range(3)
            for j in range(3)
        ]
        
        
        

    def draw(self):
        for view in self.front_view:
            view.draw(self.screen)

        for view in self.left_view:
            view.draw(self.screen)

        for view in self.top_view:
            view.draw(self.screen)
        
        for view in self.back_view:
            view.draw(self.screen)

        for view in self.right_view:
            view.draw(self.screen)

        for view in self.bottom_view:
            view.draw(self.screen)
        

    def run(self):
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))

            self.draw()
            pygame.display.flip()



App().run()
