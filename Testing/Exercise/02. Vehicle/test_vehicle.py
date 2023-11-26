import unittest
from project.vehicle import Vehicle

class TestVehicle(unittest.TestCase):

  def setUp(self):
    self.vehicle = Vehicle(15.5, 50)



  def test__init__(self):
    self.assertEqual(self.vehicle.fuel, 15.5)
    self.assertEqual(self.vehicle.capacity, 15.5)
    self.assertEqual(self.vehicle.horse_power, 50)
    self.assertEqual(self.vehicle.fuel_consumption, 1.25)


  def test_drive_error(self):

    with self.assertRaises(Exception) as ex:
      self.vehicle.drive(15)

    self.assertEqual(str(ex.exception), "Not enough fuel")


  def test_drive(self):
    self.vehicle.drive(10)
    self.assertEqual(self.vehicle.fuel, 3)


  def test_refuel_error(self):

    with self.assertRaises(Exception) as ex:
      self.vehicle.refuel(4)

    self.assertEqual(str(ex.exception), "Too much fuel")


  def test_refuel(self):
    self.vehicle.refuel(0)
    self.assertEqual(self.vehicle.fuel, 15.5)


  def test__str__(self):
    self.assertEqual(str(self.vehicle), "The vehicle has 50 "
               "horse power with 15.5 fuel left and 1.25 fuel consumption")



if __name__ == "__main__":
  unittest.main()