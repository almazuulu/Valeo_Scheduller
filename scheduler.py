import time
import random


class Resource:
    """
    Class representing a resource that can perform tasks.
    """
    
    def __init__(self, id):
        """
        Initialize a resource with a given id.
        """
        self.id = id
        self.busy = False
        self.current_task = None

    def start_task(self, task):
        """
        Start a given task and set the resource to busy.
        """
        self.busy = True
        self.current_task = task
        print(f"Resource {self.id} started task for project {task.project}")

    def end_task(self):
        """
        End the current task and set the resource to not busy.
        """
        if self.current_task:
            self.busy = False
            print(f"Resource {self.id} ended task for project {self.current_task.project}")
            self.current_task = None


class Task:
    """
    Class representing a task with a project.
    """
    def __init__(self, project):
        self.project = project


class OutsideInterface:
    """
    Class representing the interface for getting new tasks.
    """
    def __init__(self):
        self.tasks = [Task("project1"), Task("project2"), Task("project3"), Task("project4"),
                      Task("project5"), Task("project6"), Task("project7"), Task("project8"),
                      Task("project9"), Task("project10")]

    def check_for_new_task(self):
        """
        Check for a new task and return it if there is one.
        """
        if self.tasks:
            return self.tasks.pop(0)
        else:
            return None


class Scheduler:
    """
    Class that schedules tasks to resources.
    """
    def __init__(self, resources, outside_interface):
        """
        Initialize a scheduler with a given list of resources and an outside interface.
        """
        self.resources = resources
        self.outside_interface = outside_interface
        self.next_resource_index = 0

    def run_scheduler(self):
        """
        Run the scheduler continuously, getting new tasks and assigning them to resources.
        """
        while True:
            task = self.outside_interface.check_for_new_task()
            if not task:
                break
            while True:
                resource = self.resources[self.next_resource_index]
                if not resource.busy:
                    resource.start_task(task)
                    break
                else:
                    self.next_resource_index = (self.next_resource_index + 1) % len(self.resources)
                    time.sleep(0.1)
                    continue
                break
            time.sleep(random.randint(1, 5)) # simulate task execution time
            resource.end_task()
            self.next_resource_index = (self.next_resource_index + 1) % len(self.resources)


if __name__ == "__main__":
    # Create two resources and an outside interface
    resources = [Resource(i) for i in range(2)]
    outside_interface = OutsideInterface()

    # Create a scheduler and run it
    scheduler = Scheduler(resources, outside_interface)
    scheduler.run_scheduler()
