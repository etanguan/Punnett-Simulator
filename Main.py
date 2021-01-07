import pygame
import random

class ShortPlantTop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((227, 245, 66))
        self.rect = self.surf.get_rect()
        self.height = "Tall"
        self.clicked = False
        self.pos = [0, 0]


class TallPlantTop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((132, 245, 66))
        self.rect = self.surf.get_rect()
        self.height = "Tall"
        self.clicked = False
        self.pos = [0, 0]

class TallPlant(pygame.sprite.Sprite):
    def __init__(self):
        super(TallPlant, self).__init__()
        self.font = pygame.font.SysFont('Coffee', 40)
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((132, 245, 66))
        self.rect = self.surf.get_rect()
        self.height = "Tall"
        self.gene = 'AA'
        self.pos = [0, 0]

class ShortPlant(pygame.sprite.Sprite):
    def __init__(self):
        super(ShortPlant, self).__init__()
        self.font = pygame.font.SysFont('Coffee', 40)
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((227, 245, 66))
        self.rect = self.surf.get_rect()
        self.height = "Short"
        self.gene = 'aa'
        self.pos = [0, 0]

from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
shortPlantMake = ShortPlantTop()
tallPlantMake = TallPlantTop()
screen.fill((0, 0, 0))

screen.blit(tallPlantMake.surf, ((SCREEN_WIDTH / 5)-tallPlantMake.surf.get_width()/2, (SCREEN_HEIGHT / 5)-tallPlantMake.surf.get_height()/2))
screen.blit(shortPlantMake.surf, ((SCREEN_WIDTH / 1.25)-shortPlantMake.surf.get_width()/2, (SCREEN_HEIGHT / 5)-shortPlantMake.surf.get_height()/2))
tallPlantMake.pos = [(SCREEN_WIDTH / 5), (SCREEN_HEIGHT / 5)]
shortPlantMake.pos = [(SCREEN_WIDTH / 1.25), (SCREEN_HEIGHT / 5)]
pygame.display.flip()
shortPlantMake.rect = pygame.Rect(shortPlantMake.pos[0]-shortPlantMake.surf.get_width()/2, shortPlantMake.pos[1]-shortPlantMake.surf.get_height()/2, 50, 50)
tallPlantMake.rect = pygame.Rect(tallPlantMake.pos[0]-tallPlantMake.surf.get_width()/2, tallPlantMake.pos[1]-tallPlantMake.surf.get_height()/2, 50, 50)
handled = False
sprites = []
plantLst = []
sprites.append(tallPlantMake)
sprites.append(shortPlantMake)
MousePressed = False
MouseDown = False
MouseReleased = False
Target = None
update = []
testPlant = pygame.sprite.Group()

while running:
    for i in update:
        screen.blit(i.surf, (i.pos[0], i.pos[1]))

    screen.blit(tallPlantMake.surf, (
    (SCREEN_WIDTH / 5) - tallPlantMake.surf.get_width() / 2, (SCREEN_HEIGHT / 5) - tallPlantMake.surf.get_height() / 2))
    screen.blit(shortPlantMake.surf, ((SCREEN_WIDTH / 1.25) - shortPlantMake.surf.get_width() / 2,
                                      (SCREEN_HEIGHT / 5) - shortPlantMake.surf.get_height() / 2))

    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

            if event.key == K_SPACE:
                for i in update:
                    pygame.display.update(screen.blit(i.font.render(i.gene, True, (0, 0, 0)), i.pos))

        elif event.type == QUIT:
            running = False




        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            if tallPlantMake in clicked_sprites:

                temp = TallPlant()

                pygame.display.update(screen.blit(temp.surf, ((SCREEN_WIDTH / 5) - temp.surf.get_width() / 2,
                                    (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)))
                temp.rect = pygame.Rect((SCREEN_WIDTH / 5) - temp.surf.get_width() / 2,
                                                  (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2, 50, 50)
                temp.pos = ((SCREEN_WIDTH / 5) - temp.surf.get_width() / 2,
                                    (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)

                plantLst.append(temp)
                testPlant.add(temp)
                update.append(temp)

            elif shortPlantMake in clicked_sprites:

                temp = ShortPlant()

                pygame.display.update(screen.blit(temp.surf, ((SCREEN_WIDTH / 1.25) - temp.surf.get_width() / 2,
                                    (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)))
                temp.rect = pygame.Rect((SCREEN_WIDTH / 1.25) - temp.surf.get_width() / 2,
                                        (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2, 50, 50)
                temp.pos = ((SCREEN_WIDTH / 1.25) - temp.surf.get_width() / 2,
                                    (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)
                plantLst.append(temp)
                testPlant.add(temp)
                update.append(temp)

            MouseReleased = True
            MouseDown = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePressed = True
            MouseDown = True

    if MousePressed is True:
        for item in plantLst:
            if item.rect.collidepoint(mousePos):
                Target = item

    if MouseDown and Target is not None:

        Target.rect = pygame.Rect(mousePos[0]-Target.surf.get_width()/2, mousePos[1]-Target.surf.get_height()/2, 50, 50)
        screen.blit(Target.surf, (mousePos[0]-Target.surf.get_width()/2, mousePos[1]-Target.surf.get_height()/2))
        Target.pos = [mousePos[0]-Target.surf.get_width()/2, mousePos[1]-Target.surf.get_height()/2]
        pygame.display.flip()

    if MouseReleased:
        Target = None

    if len(update) > 0:
        for i in range(len(update)):
            temp = pygame.sprite.spritecollide(update[i], testPlant, False)

            if len(temp) > 1:
                j = update.index(temp[1])

                g = ''
                n = random.randint(1, 4)
                if n == 1:
                    g = update[i].gene[0] + update[j].gene[0]
                if n == 2:
                    g = update[i].gene[0] + update[j].gene[1]
                if n == 3:
                    g = update[i].gene[1] + update[j].gene[0]
                if n == 4:
                    g = update[i].gene[1] + update[j].gene[1]

                print(g)

                s = pygame.Surface((51, 51))
                s.fill((0, 0, 0))
                update[i].surf.fill((0, 0, 0))
                update[j].surf.fill((0, 0, 0))
                pygame.display.update(screen.blit(s, (update[i].pos[0], update[i].pos[1])))
                pygame.display.update(screen.blit(s, (update[j].pos[0], update[j].pos[1])))
                update[i].kill()
                update[j].kill()
                update[i].rect = None
                update[j].rect = None

                plantLst.remove(update[i])
                plantLst.remove(update[j])
                if j > i:
                    update.remove(update[j])
                    update.remove(update[i])
                else:
                    update.remove(update[i])
                    update.remove(update[j])

                if 'A' in g:
                    temp = TallPlant()
                    if g == 'aA':
                        g = 'Aa'
                    temp.gene = g
                    pygame.display.update(screen.blit(temp.surf, ((SCREEN_WIDTH / 2) - temp.surf.get_width() / 2,
                                                                  (
                                                                          SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)))
                    temp.rect = pygame.Rect((SCREEN_WIDTH / 2) - temp.surf.get_width() / 2,
                                            (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2, 50, 50)
                    temp.pos = ((SCREEN_WIDTH / 2) - temp.surf.get_width() / 2,
                                (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)
                    plantLst.append(temp)
                    testPlant.add(temp)
                    update.append(temp)
                    print(temp.gene)

                else:
                    temp = ShortPlant()
                    temp.gene = g
                    pygame.display.update(screen.blit(temp.surf, ((SCREEN_WIDTH / 2) - temp.surf.get_width() / 2,
                                                                  (
                                                                          SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)))
                    temp.rect = pygame.Rect((SCREEN_WIDTH / 2) - temp.surf.get_width() / 2,
                                            (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2, 50, 50)
                    temp.pos = ((SCREEN_WIDTH / 2) - temp.surf.get_width() / 2,
                                (SCREEN_HEIGHT / 2) - temp.surf.get_height() / 2)
                    plantLst.append(temp)
                    testPlant.add(temp)
                    update.append(temp)
                break


    screen.fill((0, 0, 0))

