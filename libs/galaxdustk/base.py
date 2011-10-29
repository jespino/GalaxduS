import pygame

class Widget(pygame.sprite.Sprite):
    signals = None
    hover = False
    clicked = False
    screen = None
    pushed = False

    def __init__(self, screen, *args, **kwargs):
        super(Widget,self).__init__(*args, **kwargs)
        self.screen = screen
        self.signals = {}

    def connect(self, signal, handler):
        if self.signals.has_key(signal):
            self.signals[str(signal)].append(handler)
        else:
            self.signals[str(signal)] = [ handler ]

    def disconnect(self, signal, handler):
        if self.signals.has_key(signal):
            if handler in self.signals[str(signal)]:
                self.signals[str(signal)].remove(handler)

    def disconnect_signal(self, signal):
        if self.signals.has_key(signal):
            self.signals[str(signal)] = []

    def disconnect_all(self):
        self.signals = {}

    def _run_signal(self, signal):
        if self.signals.has_key(signal):
            for handler in self.signals[signal]:
                handler(self)

    def update(self):
        pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        
        is_in = False

        if self.rect.top < pos[1] and self.rect.bottom > pos[1] and self.rect.left < pos[0] and self.rect.right > pos[0]:
            is_in = True

        if is_in:
            if not self.hover:
                self.hover = True
                self._run_signal("in")
        else:
            if self.hover:
                self.hover = False
                self.pushed = False
                self._run_signal("out")

        if is_in and clicked[0] and not self.pushed:
            self.pushed = True
            self._run_signal("pushed")

        if is_in and not clicked[0] and self.pushed:
            self.pushed = False
            self._run_signal("released")
            self._run_signal("clicked")

        self.draw()

    def draw(self):
        pass

