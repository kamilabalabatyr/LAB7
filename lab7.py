import pygame
from datetime import datetime

pygame.init()


screen = pygame.display.set_mode((830, 800))
pygame.display.set_caption("Mickey Clock")


bg_image = pygame.image.load('mickeyclock.jpeg') 
sec_image = pygame.image.load('righthand.PNG')
min_image = pygame.image.load('lefthand.PNG')


rect = bg_image.get_rect(center=(415, 400))  


clock = pygame.time.Clock()

done = False
while not done:
    screen.fill((255, 255, 255))  
    screen.blit(bg_image, rect.topleft)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    time = datetime.now().time()

    
    sec_angle = -(time.second * 6) + 90  
    nsec_img = pygame.transform.rotate(sec_image, sec_angle)
    sec_rect = nsec_img.get_rect(center=rect.center)  
    screen.blit(nsec_img, sec_rect)

    
    min_angle = -(time.minute * 6) + 90
    nmin_img = pygame.transform.rotate(min_image, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect)

    
    pygame.display.flip()
    clock.tick(30) 

pygame.quit()
