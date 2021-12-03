from pygame.sprite import GroupSingle

from models import BackGround


class BackGroundManager:
    def __init__(self):
        self.background = GroupSingle()
        self.level = 0

    def upgrade(self):
        background = BackGround()
        if self.level == 0:
            self.background.empty()
            background.set_images('stage1')
            self.background.add(background)

        elif self.level == 1:
            self.background.empty()
            background.set_images('stage2')
            self.background.add(background)

        # elif self.level == 2:
        #     self.background.empty()
        #     background.set_images('stage3')
        #     self.background.add(background)

        self.level += 1

    def draw(self, surface):
        self.background.draw(surface)

    def update(self):
        self.background.update()
