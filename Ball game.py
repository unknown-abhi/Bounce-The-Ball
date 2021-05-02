import pygame
import random
import os


pygame.mixer.init()

pygame.init()
clock=pygame.time.Clock()

speed=50
ball_speed = 0

display_width = 1280
display_height = 720

x = 100
y = 100
radius = 10

dx = 3
dy=3

paddle_x = 10
paddle_y =10
paddle_width = 6
paddle_height = 200
player_score = 0

if (not os.path.exists("highscore.txt")):
	with open("highscore.txt", "w") as f:
		f.write("0")

with open("highscore.txt", "r") as f:
	h_score = f.read()

def randomize_start():
	global x, y, dx
	x = random.randint(int(display_width/4), display_width-20)
	y = random.randint(10, display_height-10)
	pygame.mixer.music.load("02.mp3")
	pygame.mixer.music.play(-1)
	if random.randint(0,2)%2==0:
		dx *= -1

def hit_back():
    if x + radius > display_width:
        return True
    return False

def hit_sides():
    if y - radius<0:
        return True
    if y+radius>display_height:
        return True
    return False

def hit_paddle():
    global player_score
    global paddle_height
    global ball_speed
    if x-radius <= paddle_x +paddle_width and y> paddle_y and y< paddle_y+paddle_height:
        player_score += 10
        if paddle_height > 25:
            paddle_height -= 5
        else:
        	paddle_height == 25
        global speed
        speed += 5
        ball_speed += 5
        return True
    return False

def game_over():
    global player_score
    end_game=True
    display.fill((75,0,130))
    display.blit(bgimg2, (0, 0))
    pygame.mixer.music.load("03.mp3")
    pygame.mixer.music.play(-1)
    font_title = pygame.font.Font(None, 36)
    font_instrutions = pygame.font.Font(None, 24)

    annoucement = font_title.render("GAME OVER", True, (255,255,255))
    annoucement_rect= annoucement.get_rect(center = (int(display_width/2), int(display_height/3)))
    display.blit(annoucement, annoucement_rect)

    qinstruction = font_instrutions.render("Press 'Q' to QUIT the Game", True, (255,255,255))
    qinstruction_rect = qinstruction.get_rect(center = (int(display_width/2), int(display_height/1.5)))
    display.blit(qinstruction, qinstruction_rect)

    rinstruction = font_instrutions.render("Press 'R' to RESUME the Game", True, (255,255,255))
    rinstruction_rect = rinstruction.get_rect(center = (int(display_width/2), int(display_height/1.3)))
    display.blit(rinstruction, rinstruction_rect)

    final_score = "Your Final Score: " + str(player_score)
    score_show = font_instrutions.render(final_score, True, (255,255,255))
    score_show_rect = score_show.get_rect(center = (int(display_width/2), int(display_height/2)))
    display.blit(score_show, score_show_rect)

    pygame.display.flip()
    while(end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    end_game = False

#Game Window
display =pygame.display.set_mode((display_width, display_height))

bgimg = pygame.image.load("001.jpg")
bgimg = pygame.transform.scale(bgimg, (display_width, display_height)).convert_alpha()
bgimg1 = pygame.image.load("002.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (display_width, display_height)).convert_alpha()
bgimg2 = pygame.image.load("003.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (display_width, display_height)).convert_alpha()

pygame.display.set_caption("Let's Bounce!")
icon=pygame.image.load('micon.png')
pygame.display.set_icon(icon)

display.fill((0,0,0))
display.blit(bgimg, (0, 0))

pygame.mixer.music.load("01.mp3")
pygame.mixer.music.play(-1)

dev=pygame.font.SysFont("Brush Script MT",20)
welcome_screen=pygame.font.SysFont("Times New Roman", 30)
welcome = welcome_screen.render("Let's Play Bounce!", True, (255,255,255))
welcome_rect = welcome.get_rect(center = (int(display_width/2), int(display_height/2)))

startmsg = welcome_screen.render("Hit 'Y' to START, Press 'Q' to Quit, or Game Will Autostart in 10 Seconds.", True, (255,255,255))
startmsg_rect =startmsg.get_rect(center = (int(display_width/2), int(display_height/4)))

devlop=dev.render("Developed By: Abhishek Kumar", True, (255,255,255))
devlop_rect=devlop.get_rect(center = (int(display_width/2), int(display_height/1.1)))
display.blit(devlop, devlop_rect)
display.blit(welcome, welcome_rect)
display.blit(startmsg, startmsg_rect)
pygame.display.flip();

pygame.time.set_timer(pygame.USEREVENT, 10000)

timer_active = True
while(timer_active):
	for event in pygame.event. get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.USEREVENT:
			timer_active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_y:
				timer_active = False
			if event.key == pygame.K_q:
				quit()

randomize_start()

while True:
    clock.tick(speed)
    pressed_key=pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height +10 <= display_height:
            paddle_y += 10

    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    #Main Game Window
    display.fill((0,0,0))
    display.blit(bgimg1, (0, 0))
    #Speed
    speed_indicate = pygame.font.Font(None, 24)
    final_speed = "Speed: " + str(ball_speed)
    speed_show = speed_indicate.render(final_speed, True, (255,255,255))
    speed_show_rect = speed_show.get_rect(center = (float(display_width/1.1), float(display_height/23)))
    display.blit(speed_show, speed_show_rect)
    #High-Score
    final_score = "Hi-Score: " + str(h_score)
    s_show = speed_indicate.render(final_score, True, (255,255,255))
    s_show_rect = s_show.get_rect(center = (float(display_width/1.4), float(display_height/23)))
    display.blit(s_show, s_show_rect)
    #Current Score
    current_score = "Score: " + str(player_score)
    current_show = speed_indicate.render(current_score, True, (255,255,255))
    current_show_rect = current_show.get_rect(center = (int(display_width/2), int(display_height/23)))
    display.blit(current_show, current_show_rect)

    x += dx
    y += dy

    pygame.draw.rect(display, (255,255,255), (paddle_x,paddle_y,paddle_width,paddle_height))
    pygame.draw.circle(display,(255,0,0), (x,y), radius)

    if x < radius:
        game_over()
        randomize_start()
        dx=abs(dx)
        if player_score>int(h_score):
        	h_score = player_score
        	with open("highscore.txt", "w") as f:
        		f.write(str(h_score))
        player_score=0
        speed = 50
        paddle_height = 200
        ball_speed = 0
    if hit_back() or hit_paddle():
        dx *= -1
    if hit_sides():
        dy *= -1
    pygame.display.update()
pygame.quit()
quit()

#Game Version V-1.0
#Name: Abhishek Kumar
#Gmail: ak35540@gmail.com