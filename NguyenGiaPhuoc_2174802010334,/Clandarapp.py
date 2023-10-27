#thu vien
import pygame
from pygame.locals import *
import random

pygame.init()

#mau nen
orange=(255,69,0)
green=(76,208,56)
yellow=(255,232,0)
red=(200,0,0)
white=(255,255,255)
blue=(0,191,255)
black=(0,0,0)
brown=(139,69,19)
gray = (128,128,128)
#cua so 
width=500
height=500
screen_size=(width,height)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption('Đua xe đường phố')

#khoi tao cac bbien
gameplay=False
speed=2
score=0	

#Đường cho xe đua 
road_width=300
street_width=10
street_height=50

#lane duong
lane_left=150
lane_center=250
lane_right=350
lanes=[lane_left,lane_right,lane_center]
lane_move_y=0

#Biên đường 
road=(100,0,road_width,height)
left_edge=(95,0,street_width,height)
right_edge=(395,0,street_width,height)
#vi tri xe nguoi choi
player_x=250
player_y=400
#Doi tuong xe luu thong-vehical
class Vehicle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
#scale image
        image_scale=45 / image.get_rect().width
        new_width = image.get_rect().width *image_scale
        new_heigh = image.get_rect().height  *image_scale
        self.image = pygame.transform.scale(image,(new_width,new_heigh))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
#doi tuong xe player
class playervehicle(Vehicle):
    def __init__(self,x,y):
        image = pygame.image.load('./images/car.png')
        super().__init__(image,x,y)
#sprite groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()
#Tao xe nguoi choi
player = playervehicle (player_x,player_y)
player_group.add(player)
#load xe luu thong
image_name=['pickup_truck.png','semi_trailer.png','taxi.png','van.png']
vehicle_images =[]
for name in image_name:
    image = pygame.image.load('./images/'+ name )
    vehicle_images.append(image)

#cai dat fps cua game
clock=pygame.time.Clock()
fps=120
 
#Vong lap xu ly
running=True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

	#ve dia hinh
    screen.fill(brown)
    #ve road $ duong chay
    pygame.draw.rect(screen,gray,road)
	#ve edge-hang lang duong
    pygame.draw.rect(screen,yellow,left_edge)
    pygame.draw.rect(screen,yellow,right_edge)
    #ve lane duong 	   	
    lane_move_y+=speed*2
    if lane_move_y >=street_height *2:
        lane_move_y=0
    for y in range(street_height* -2,height,street_height*2):
        pygame.draw.rect(screen,white,(lane_left+45,y+lane_move_y,street_width,street_height))
        pygame.draw.rect(screen,white,(lane_center+45,y+lane_move_y,street_width,street_height))

#Ve xe player
    player_group.draw(screen)
    if len(vehicle_group) <2 :
        add_verhicle = True
        for verhicle in vehicle_group :
            if verhicle.rect.top < verhicle.rect.height * 1.5 :
                add_verhicle = False
        if add_verhicle:
                lane = random.choice(lanes)
                image = random.choice(vehicle_images)
                vehicle_instance = Vehicle(image, lane, height / -2)
                vehicle_group.add(vehicle_instance)
#cho xe cong cong
    for Vehicle in vehicle_group:
        Vehicle.rect.y +=speed
#remove verhicle
        if Vehicle.rect.top >=height:
            Vehicle.kill()      
            score +=1
#tang toc do chay
            if score>0 and score % 5 == 0:
                speed+= 1
#ve nhom xe luu thong
    vehicle_group.draw(screen)
        


#ve phuong tien giao thong

    pygame.display.update()
pygame.quit()
    
    

