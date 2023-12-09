from project.tennis_player import TennisPlayer
import unittest

class TestTennisPlayer(unittest.TestCase):

    def setUp(self):
        self.tennis = TennisPlayer("John", 20, 100)


    def test_init(self):
        self.assertEqual(self.tennis.name, "John")
        self.assertEqual(self.tennis.age, 20)
        self.assertEqual(self.tennis.points, 100)
        self.assertEqual(self.tennis.wins, [])


    def test_name_setter_failure(self):
        with self.assertRaises(ValueError) as vl:
            self.tennis.name = "ab"

        self.assertEqual(str(vl.exception), "Name should be more than 2 symbols!")


    def test_name_setter_success(self):
        self.tennis.name = "peter"
        self.assertEqual(self.tennis.name, "peter")


    def test_age_setter_failure(self):
        with self.assertRaises(ValueError) as vl:
            self.tennis.age = 17

        self.assertEqual(str(vl.exception), "Players must be at least 18 years of age!")


    def test_age_setter_success(self):
        self.tennis.age = 18
        self.assertEqual(self.tennis.age, 18)


    def test_add_new_win_if_not_in(self):
        self.tennis.add_new_win("tennis")
        self.assertEqual(self.tennis.wins, ["tennis"])


    def test_add_new_win_if_in(self):
        self.tennis.wins.append("tennis")
        self.assertEqual(self.tennis.add_new_win("tennis"), "tennis has been already added to the list of wins!")


    def test_lt_if_lower(self):
        other1 = TennisPlayer("peter", 18, 500)
        self.assertEqual(self.tennis < other1, "peter is a top seeded player and he/she is better than John")


    def test_lt_if_bigger(self):
        other1 = TennisPlayer("peter", 18, 50)
        self.assertEqual(self.tennis < other1, "John is a better player than peter")

    def test_str_(self):
        self.tennis.wins.append("tennis")
        self.tennis.wins.append("tennis1")
        self.assertEqual(str(self.tennis), "Tennis Player: John\n" \
                "Age: 20\n" \
                "Points: 100.0\n" \
                "Tournaments won: tennis, tennis1")

if __name__ == '__main__':
    unittest.main()