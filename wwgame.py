import sys, pygame, random
from ww import *
pygame.init()

ww=Stage(20, 20, 24)
ww.set_player(KeyboardPlayer("icons/face-cool-24.png", ww))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 0, 3, 1))
ww.add_actor(KingMonster("icons/king-monster.png", ww, 7, 4, 5))
ww.add_actor(AddBoxesMonster("icons/add-boxes-monster.png", ww, 4, 10, 3))
ww.add_actor(ExplosiveMonster("icons/explosive-monster.png", ww, 5, 20, 2))

# Places 100 boxes in random positions on the stage
num_boxes=0
while num_boxes<90:
    x=random.randrange(ww.get_width())
    y=random.randrange(ww.get_height())
    if ww.get_actor(x,y) is None:
        ww.add_actor(Box("icons/emblem-package-2-24.png", ww, x, y))
        num_boxes+=1

num_sticky_boxes=0
while num_sticky_boxes<10:
    x=random.randrange(ww.get_width())
    y=random.randrange(ww.get_height())
    if ww.get_actor(x,y) is None:
        ww.add_actor(StickyBox("icons/happy-package-2-24.jpg", ww, x, y))
        num_sticky_boxes+=1
        
ww.add_actor(Wall("icons/wall.jpg", ww, 4, 3))
ww.add_actor(Wall("icons/wall.jpg", ww, 5, 3))
ww.add_actor(Wall("icons/wall.jpg", ww, 6, 3))
ww.add_actor(Wall("icons/wall.jpg", ww, 16, 11))
ww.add_actor(Wall("icons/wall.jpg", ww, 16, 12))
ww.add_actor(Wall("icons/wall.jpg", ww, 16, 13))
ww.add_actor(Wall("icons/wall.jpg", ww, 11, 19))
ww.add_actor(Wall("icons/wall.jpg", ww, 12, 19))

# YOUR COMMENT GOES HERE. BRIEFLY DESCRIBE WHAT THE FOLLOWING LOOP DOES.
while True:
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
                ww.player_event(event.key)
    ww.step()
    ww.draw()
