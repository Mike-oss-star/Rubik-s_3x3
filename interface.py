import pygame 
import sys
from dataclasses import dataclass



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

        self.front_view=[
            FrontView(
                120+35*i ,
                150+13*i + 45*j,
                28,
                40,
                10,
                (255,0,0)
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
                (0,0,255)
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
                (255,255,255)
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
