from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:

  def __init__(self):
    self.customers = []
    self.trainers = []
    self.equipment = []
    self.plans = []
    self.subscriptions = []


  def add_customer(self, customer: Customer):

    if customer not in self.customers:
      self.customers.append(customer)


  def add_trainer(self, trainer: Trainer):

    if trainer not in self.trainers:
      self.trainers.append(trainer)


  def add_equipment(self, equipment: Equipment):

    if equipment not in self.equipment:
      self.equipment.append(equipment)



  def add_plan(self, plan : ExercisePlan):

    if plan not in self.plans:
      self.plans.append(plan)


  def add_subscription(self, subscription: Subscription):
    
    if subscription not in self.subscriptions:
      self.subscriptions.append(subscription)


  def subscription_info(self, subscription_id):
    to_return = []
    
    for subscription in self.subscriptions:

      if subscription.id == subscription_id:
        global subscription1
        subscription1 = subscription


    customer_id1 = subscription1.customer_id
    trainer_id1 = subscription1.trainer_id
    exercise_id1 = subscription1.exercise_id
    

    to_return.append(str(subscription1)) # subscription done


    for customer in self.customers:
      if customer.id == customer_id1:
        global customer1
        customer1 = customer


    to_return.append(str(customer1)) ## customer done


    for trainer in self.trainers:
      if trainer.id == trainer_id1:
        global trainer1
        trainer1 = trainer


    to_return.append(str(trainer1)) ## trainer done


    for exercise in self.plans:

      if exercise.id == exercise_id1:
        global exercise1
        exercise1 = exercise

    equipment_id1 = exercise1.equipment_id

    for equipment in self.equipment:

      if equipment.id == equipment_id1:
        global equipment1
        equipment1 = equipment

    to_return.append(str(equipment1))
    to_return.append(str(exercise1))

    return "\n".join(to_return)


