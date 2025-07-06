from pyray import *
from raylib import *
from random import randint ,choice
print("Hello, World!")
init_window(800, 600, "Raylib Window")
set_window_state(FLAG_VSYNC_HINT)



secree_width = get_screen_width()
secree_height = get_screen_height()
player_score = 0
bots_score = 0



#Boll
ball_pos = Vector2(secree_width/2, secree_height/2)
direction = [-1,1]
ball_dir = Vector2(1,1)
ball_radius = 20
speed = 300


#Player
player = Rectangle(0, secree_height/2 - 50, 10, 100)
player_dir = Vector2(0, 1)


#AI Player
ai_player = Rectangle(int(secree_width-10), int(secree_height/2 - 50), 10, 100)
ai_player_dir = Vector2(0, 1)

def PlayerMovement(dt,player, speed):
    if is_key_down(KEY_W):
        player.y -= speed * dt
        
    if is_key_down(KEY_S):
        player.y += speed * dt 

    if player.y < 0:
        player.y = 0

    if player.y > secree_height - 100:
        player.y = secree_height - 100

def Ai_PlayerMovment(ai_player_dir  , speed,dt):
    ai_player_dir.y  += ball_dir.y  * speed * dt

    if ai_player.y < 0:
        ai_player.y = 0

    if ai_player.y > secree_height - 100:
        ai_player.y = secree_height - 100


def CheckCollision():
    global speed
    
    if check_collision_circle_rec(ball_pos, ball_radius , player):
        ball_dir.x *= -1
        speed += 20
        
        
    if check_collision_circle_rec(ball_pos, ball_radius , ai_player):
        ball_dir.x *= -1
        speed += 20
    
        

# Reset function to reset the ball and player positions
def reset(ball_pos):  
    global speed
    if ball_pos.x <= 0 or ball_pos.x >= secree_width:
        ball_pos.x = secree_width / 2
        ball_pos.y = secree_height / 2
        ball_dir.x *= choice(direction)
        ball_dir.y *= choice(direction)
        speed = 300        

while not window_should_close():
    
    draw_fps(10,10)
    
    dt = get_frame_time()
    begin_drawing()
    clear_background(Color(55, 115, 55, 45)) 



    # Ball movement
    ball_pos.x += ball_dir.x * speed * dt
    ball_pos.y += ball_dir.y * speed * dt
    ball_dir = Vector2Normalize(ball_dir)

    # Player Movement
    PlayerMovement(dt,player, speed)
    # PlayerMovement(dt,ai_player, speed)
    Ai_PlayerMovment(ai_player,speed ,dt)

    # Check Collision
    CheckCollision()
    
   
    if ball_pos.x < 0:
        bots_score += 1

    if ball_pos.x > secree_width :
        player_score += 1

    reset(ball_pos)
    
    
    if ball_pos.y < 0 + ball_radius:
        ball_dir.y *= -1
    if ball_pos.y > secree_height - ball_radius:
        ball_dir.y *= -1 

    # Draw a Player
    draw_rectangle_rounded(player,0.5,0,WHITE)

    # Draw AI Player
    draw_rectangle_rounded(ai_player,0.5,0,WHITE)


    #drawCircle
    draw_circle_v(ball_pos, ball_radius , RED)
    
    draw_text( "Player: " + str(player_score) ,  200 , 50, 20 , WHITE)
    draw_text( "Bot: " + str(bots_score) ,  500 , 50, 20 , WHITE)

    draw_text("Bong Game", int(secree_width / 2 - 50) , 200, 20, WHITE)
    end_drawing()
close_window()


