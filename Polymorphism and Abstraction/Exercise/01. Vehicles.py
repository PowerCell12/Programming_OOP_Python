from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, fuel_quantity, fuel_consumption):
    self.fuel_quantity =fuel_quantity
    self.fuel_consumption =fuel_consumption

  @abstractmethod
  def drive(self, distance):
    pass

  @abstractmethod
  def refuel(self, fuel):
    pass




class Car(Vehicle):
  Conditioner_on = 0.9


  def drive(self, distance):
    final = distance * (self.fuel_consumption + Car.Conditioner_on)
    
    if self.fuel_quantity - final >= 0:
        self.fuel_quantity -= final


  
  def refuel(self, fuel):
    self.fuel_quantity += fuel




class Truck(Vehicle):
  Conditioner_on = 1.6




  def drive(self, distance):
    final = distance * (self.fuel_consumption + Truck.Conditioner_on)
    
    if self.fuel_quantity - final >= 0:
        self.fuel_quantity -= final


  def refuel(self, fuel):
    self.fuel_quantity += fuel * 0.95

