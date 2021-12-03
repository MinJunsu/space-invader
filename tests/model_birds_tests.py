from unittest import TestCase

from pygame import mixer

from models.enemy import SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird

mixer.pre_init(44100, -16, 2, 512)


class BirdTest(TestCase):
    def setUp(self) -> None:
        self.smile_bird = SmileBird(100, 100)
        self.poisoned_bird = PoisonedBird(100, 100)
        self.circled_bird = CircledBird(100, 100)
        self.old_bird = OldBird(100, 100)
        self.crazy_bird = CrazyBird(100, 100)

    def test_smile_bird_attribute(self):
        self.assertEqual(self.smile_bird.speed, 4)
        self.assertEqual(self.smile_bird.DEFAULT_COUNT, 5)
        self.assertEqual(self.smile_bird.score, 10)

    def test_poisoned_bird_attribute(self):
        self.assertEqual(self.poisoned_bird.speed, 6)
        self.assertEqual(self.poisoned_bird.DEFAULT_COUNT, 8)
        self.assertEqual(self.poisoned_bird.score, 30)

    def test_circled_bird_attribute(self):
        self.assertEqual(self.circled_bird.speed, 6)
        self.assertEqual(self.circled_bird.DEFAULT_COUNT, 10)
        self.assertEqual(self.circled_bird.score, 50)

    def test_old_bird_attribute(self):
        self.assertEqual(self.old_bird.speed, 2)
        self.assertEqual(self.old_bird.DEFAULT_COUNT, 15)
        self.assertEqual(self.old_bird.score, 60)

    def test_crazy_bird_attribute(self):
        self.assertEqual(self.crazy_bird.speed, 8)
        self.assertEqual(self.crazy_bird.DEFAULT_COUNT, 1)
        self.assertEqual(self.crazy_bird.score, 500)
        self.assertEqual(self.crazy_bird.health_point, 15)

    def test_bird_move(self):
        before_pos_x = self.smile_bird.rect.x
        self.smile_bird.move()
        after_pos_x = self.smile_bird.rect.x
        self.assertGreater(after_pos_x, before_pos_x)

    def test_image_update(self):
        before_image = self.smile_bird.image
        self.smile_bird.update()
        after_image = self.smile_bird.image
        self.assertNotEqual(before_image, after_image)

    def test_image_index_update(self):
        before_image_index = self.smile_bird.image_index
        self.smile_bird.update()
        after_image_index = self.smile_bird.image_index
        self.assertLess(before_image_index, after_image_index)


if __name__ == '__main__':
    test = BirdTest()
    test.run()
