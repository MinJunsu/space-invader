from unittest import TestCase

import pygame

from models.enemy import RedSpaceShip, BlueSpaceShip, GreenSpaceShip, CircledSpaceShip
from models.enemy.bullets import BlueSpaceShipBullet, RedSpaceShipBullet, GreenSpaceShipBullet, CircledSpaceShipBullet


class ShipTest(TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.mixer.pre_init()
        self.blue_ship = BlueSpaceShip(100, 100)
        self.red_ship = RedSpaceShip(100, 100)
        self.green_ship = GreenSpaceShip(100, 100)
        self.circled_ship = CircledSpaceShip(100, 100)

    def test_blue_ship_attribute(self):
        self.assertEqual(self.blue_ship.speed, 5)
        self.assertEqual(self.blue_ship.DEFAULT_COUNT, 10)
        self.assertEqual(self.blue_ship.score, 150)
        self.assertEqual(self.blue_ship.COOLDOWN, 70)
        self.assertEqual(self.blue_ship.weapon, BlueSpaceShipBullet)

    def test_red_ship_attribute(self):
        self.assertEqual(self.red_ship.speed, 7)
        self.assertEqual(self.red_ship.DEFAULT_COUNT, 10)
        self.assertEqual(self.red_ship.score, 200)
        self.assertEqual(self.red_ship.COOLDOWN, 60)
        self.assertEqual(self.red_ship.weapon, RedSpaceShipBullet)

    def test_green_ship_attribute(self):
        self.assertEqual(self.green_ship.speed, 8)
        self.assertEqual(self.green_ship.DEFAULT_COUNT, 15)
        self.assertEqual(self.green_ship.score, 300)
        self.assertEqual(self.green_ship.COOLDOWN, 50)
        self.assertEqual(self.green_ship.weapon, GreenSpaceShipBullet)

    def test_circled_ship_attribute(self):
        self.assertEqual(self.circled_ship.speed, 8)
        self.assertEqual(self.circled_ship.DEFAULT_COUNT, 1)
        self.assertEqual(self.circled_ship.score, 1000)
        self.assertEqual(self.circled_ship.COOLDOWN, 10)
        self.assertEqual(self.circled_ship.weapon, CircledSpaceShipBullet)

    def test_blue_ship_attack(self):
        self.blue_ship.weapons.empty()
        self.blue_ship.cool_down_counter = self.blue_ship.COOLDOWN + 1
        self.blue_ship.attack()
        self.assertIsInstance(self.blue_ship.weapons.sprites().pop(), BlueSpaceShipBullet)

    def test_red_ship_attack(self):
        self.red_ship.weapons.empty()
        self.red_ship.cool_down_counter = self.red_ship.COOLDOWN + 1
        self.red_ship.attack()
        self.assertIsInstance(self.red_ship.weapons.sprites().pop(), RedSpaceShipBullet)

    def test_green_ship_attack(self):
        self.green_ship.weapons.empty()
        self.green_ship.cool_down_counter = self.green_ship.COOLDOWN + 1
        self.green_ship.attack()
        self.assertIsInstance(self.green_ship.weapons.sprites().pop(), GreenSpaceShipBullet)

    def test_space_ship_update(self):
        before_image_index = self.red_ship.image_index
        before_cool_down = self.red_ship.cool_down_counter
        self.red_ship.update()
        after_image_index = self.red_ship.image_index
        after_cool_down = self.red_ship.cool_down_counter
        self.assertLess(before_image_index, after_image_index)
        self.assertLessEqual(before_cool_down, after_cool_down)


if __name__ == '__main__':
    test = ShipTest()
    test.run()
