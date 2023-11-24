import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("John", 5000, 12)

    def test_name_salary_and_energy(self): #done
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 5000)
        self.assertEqual(self.worker.energy, 12)
        self.assertEqual(self.worker.money, 0)

    def test_rest_method_incrementation(self):
        self.worker.rest()
        starting = self.worker.energy
        result = 13
        self.assertEqual(starting, result)

    def test_raise_error_energy_work(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as e:
            self.worker.work()

        self.assertEqual(str(e.exception), 'Not enough energy.')


    def test_worker_money_increase(self): #done
        self.worker.work()
        self.assertEqual(self.worker.money, 5000)

    def test_energy_decrease_worker(self): #done
        self.worker.work()
        self.assertEqual(self.worker.energy, 11)

    def test_get_info_correct(self):
        self.assertEqual(self.worker.get_info(), f'John has saved 0 money.')

## 83/100

if __name__ == '__main__':
    unittest.main()
