#Dieu khien x
''''
        if event.type==KEYDOWN:
            if event.key== K_LEFT and player.rect.center(0)>lane_left:
                player.rect.x -=100    
            if event.key== K_RIGHT and player.rect.center(0)>lane_right:
                player.rect.x +=100               
'''