from project.task import Task

class Section:

  def __init__(self, name):
    self.name = name
    self.tasks = []


  def add_task(self, new_task: Task):

    if new_task in self.tasks:
      return f"Task is already in the section {self.name}"

    self.tasks.append(new_task)
    return f"Task {new_task.details()} is added to the section"


  def complete_task(self, task_name):
    bool = False
    final  = ""

    for task in self.tasks:
      if task.name == task_name:
        bool = True
        final = task
        break


    if bool == False:
      return f"Could not find task with the name {task_name}"

    index= self.tasks.index(final)

    self.tasks[index].completed = True
    return f"Completed task {task_name}"



  def clean_section(self):
    counter = 0
    for i in range(len(self.tasks)):
      task = self.tasks[i]

      if task.completed == True:
        counter += 1
        self.tasks.remove(task)
      
    return f"Cleared {counter} tasks."


  
  def view_section(self):
    to_return =[]

    to_return.append(f"Section {self.name}:")

    for task in self.tasks:
      to_return.append(task.details())

    return "\n".join(to_return)
