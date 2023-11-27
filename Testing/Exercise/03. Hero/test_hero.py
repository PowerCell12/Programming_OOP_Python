import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("George", 20, 100, 5)

    def test_init(self):
        self.assertEqual("George", self.hero.username)
        self.assertEqual(20, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_if_enemy_hero_equals_name(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("George", 25, 101, 10))

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_if_hero_health_below_0(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("John", 25, 101, 10))
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_if_Enemy_health_below(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("John", 25, 0, 10))

        self.assertEqual(str(ex.exception), "You cannot fight John. He needs to rest")

    def test_battle_draw(self):
        self.assertEqual("Draw", self.hero.battle(Hero("John", 100, 1, 100)))


    def test_battle_win(self):
        win = self.hero.battle(Hero("John", 2, 1, 1))
        self.assertEqual("You win", win)
        self.assertEqual(self.hero.level, 21)
        self.assertEqual(self.hero.health, 103)
        self.assertEqual(self.hero.damage, 10)

    def test_if_battle_lost(self):
        villan = Hero("John", 100, 101, 100)
        lost = self.hero.battle(villan)
        self.assertEqual("You lose", lost)
        self.assertEqual(villan.level, 101)
        self.assertEqual(villan.damage, 105)
        self.assertEqual(villan.health, 6)


    def test__str__(self):
        self.assertEqual("Hero George: 20 lvl\nHealth: 100\nDamage: 5\n", str(self.hero))


if __name__ == "__main__":
    unittest.main()