import pygame
import os
import base

def _button_in_handler(widget):
    widget.color = widget.color_hover

def _button_out_handler(widget):
    widget.color = widget.color_default

def _button_pushed_handler(widget):
    widget.color = widget.color_pressed

def _button_released_handler(widget):
    widget.color = widget.color_default

def _select_button_out_handler(widget):
    if not widget.selected:
        widget.color = widget.color_default
    elif widget.selected:
        widget.color = widget.color_selected

def _select_button_clicked_handler(widget):
    for sprite in widget.screen.sprites.sprites():
        if hasattr(sprite,'group_id'):
            if sprite.group_id == widget.group_id:
                sprite.selected = False
                sprite.color = sprite.color_default
    widget.color = widget.color_selected
    widget.selected = True

class Button(base.Widget):
    color = (0,0,200)
    color_default = (0,0,200)
    color_hover = (0,200,0)
    color_pressed = (200,0,0)
    color_selected = (200,200,0)
    width = None
    height = None

    def __init__(self, screen, label, width=200, height=40):
        super(Button,self).__init__(screen)

        self.width = width
        self.height = height

        font = pygame.font.Font(None, 24)
        self.text = font.render(label, 1, (240, 240, 240))

        self.draw()
        self.rect = self.image.get_rect()
        self.connect('in', _button_in_handler)
        self.connect('out', _button_out_handler)
        self.connect('pushed', _button_pushed_handler)

    def draw(self):
        self.image = pygame.Surface((self.width,self.height), flags=pygame.SRCALPHA)
        self.image.fill((0,0,0,128))
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), 2)
        textpos = self.text.get_rect(centerx=self.image.get_width()/2, centery=self.image.get_height()/2)
        self.image.blit(self.text, textpos)

class CircularButton(base.Widget):
    color = (0,0,200)
    color_default = (0,0,200)
    color_hover = (0,200,0)
    color_pressed = (200,0,0)

    radius = None
    image_in = None

    def __init__(self, screen, image_path, radius=50):
        super(CircularButton,self).__init__(screen)
        self.radius = radius
        self.image_in = pygame.image.load(image_path)
        self.draw()
        self.rect = self.image.get_rect()
        self.connect('in', _button_in_handler)
        self.connect('out', _button_out_handler)
        self.connect('pushed', _button_pushed_handler)
        self.connect('released', _button_released_handler)

    def draw(self):
        self.image = pygame.Surface((self.radius*2,self.radius*2), flags=pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0,0,0,128), (self.image.get_rect().centerx,self.image.get_rect().centery), self.radius, 0)
        pygame.draw.circle(self.image, self.color, (self.image.get_rect().centerx,self.image.get_rect().centery), self.radius, 2)
        image_in_pos = self.image_in.get_rect(centerx=self.image.get_width()/2, centery=self.image.get_height()/2)
        self.image.blit(self.image_in, image_in_pos)

class CircularSelectButton(CircularButton):
    selected = False
    color_selected = (200,200,0)
    group_id = 0
    value = None

    def __init__(self, screen, image_path, radius=50):
        super(CircularSelectButton,self).__init__(screen, image_path, radius)
        self.disconnect_all()
        self.connect('in', _button_in_handler)
        self.connect('out', _select_button_out_handler)
        self.connect('pushed', _button_pushed_handler)
        self.connect('released', _button_released_handler)
        self.connect('clicked', _select_button_clicked_handler)

    def get_value(self):
        return self.value

class SelectButton(Button):
    selected = False
    color_selected = (200,200,0)
    group_id = 0
    value = None

    def __init__(self, screen, label, width=200, height=40):
        super(SelectButton,self).__init__(screen, label, width, height)
        self.disconnect_all()
        self.connect('in', _button_in_handler)
        self.connect('out', _select_button_out_handler)
        self.connect('pushed', _button_pushed_handler)
        self.connect('released', _button_released_handler)
        self.connect('clicked', _select_button_clicked_handler)

    def get_value(self):
        return self.value
