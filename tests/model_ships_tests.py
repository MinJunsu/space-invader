from unittest import TestCase

from pygame import mixer

from models.enemy import RedSpaceShip, BlueSpaceShip, GreenSpaceShip, CircledSpaceShip
from models.enemy.bullets import BlueSpaceShipBullet, RedSpaceShipBullet, GreenSpaceShipBullet, CircledSpaceShipBullet

mixer.pre_init(44100, -16, 2, 512)


class ShipTest(TestCase):
    def setUp(self) -> None:
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
