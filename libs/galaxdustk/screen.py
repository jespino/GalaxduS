import pygame 

class BaseScreen(object):
    background_path = ""

    def __init__(self, context):
        self.context = context
        if self.background_path:
            self.background = pygame.image.load(self.background_path)
        else:
            self.background = pygame.Surface(context.screen.get_size())

        self.sprites = pygame.sprite.RenderPlain()
        self.pointer = pygame.sprite.RenderPlain((self.context.pointer,))

    def draw(self):
        self.context.screen.blit(self.background, (0,0))
        self.sprites.update()
        self.pointer.update()
        self.sprites.draw(self.context.screen)
        self.pointer.draw(self.context.screen)
