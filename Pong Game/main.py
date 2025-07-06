from raylib import *
from pyray import *




class Ball :
    def __init__(self,pos,radius, dir,speed):
        self.pos = pos
        self.radius = radius
        self. dir = dir
        self.speed = speed

    def Draw(self) :
        draw_circle_v(self.pos,self.radius,Color(109,60,140,200))

    def Update(self,dt):
        self.pos.x += self.speed * dt * self.dir.x
        self.pos.y += self.speed * dt * self.dir.y

    def ScreenBorder(self):
        if self.pos.x <= 0 + self.radius or self.pos.x >= get_screen_width() - self.radius:
            self.dir.x *= -1.1
        if self.pos.y <= 0 + self.radius or self.pos.y >= get_screen_height() - self.radius:
            self.dir.y *= -1.1

        

ball = Ball(Vector2(500,400), 20, Vector2(1,1), 400)

init_window(1250,730,"OPP")
set_target_fps(60)

while not WindowShouldClose():
    dt = get_frame_time()
    begin_drawing()

    clear_background(BLACK)

    ball.Draw()
    ball.Update(dt)
    ball.ScreenBorder()
    ball.dir = Vector2Normalize(ball.dir)

    end_drawing()

CloseWindow()