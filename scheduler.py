import time
import random
from queue import PriorityQueue
from collections import defaultdict

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
        print(f"Resource {self.id} started task for project {task.project} with priority {task.priority}")

    def end_task(self):
        """
        End the current task and set the resource to not busy.
        """
        if self.current_task:
            self.busy = False
            print(f"Resource {self.id} ended task for project {self.current_task.project} with priority {self.current_task.priority}")
            self.current_task = None

class Task:
    """
    Class representing a task with a project and priority.
    """
    def __init__(self, project, priority):
        self.project = project
        self.priority = priority
        
    def __lt__(self, other):
        return self.priority < other.priority

class OutsideInterface:
    """
    Class representing the interface for getting new tasks.
    """
    def __init__(self):
        self.tasks = PriorityQueue()
        self.tasks.put(Task("project1", 1))
        self.tasks.put(Task("project2", 2))
        self.tasks.put(Task("project3", 3))
        self.tasks.put(Task("project4", 1))
        self.tasks.put(Task("project5", 2))
        self.tasks.put(Task("project6", 3))
        self.tasks.put(Task("project7", 1))
        self.tasks.put(Task("project8", 2))
        self.tasks.put(Task("project9", 3))
        self.tasks.put(Task("project10", 1))

    def check_for_new_task(self):
        """
        Check for a new task and return it if there is one.
        """
        if not self.tasks.empty():
            return self.tasks.get()
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
        self.projects = defaultdict(lambda: {"count": 0})
        for resource in resources:
            self.projects[resource.id] = {"project": None, "count": 0}

    def run_scheduler(self):
        """
        Run the scheduler and assign tasks to resources.
        """
        while True:
            task = self.outside_interface.check_for_new_task()
            if task is None:
                break
            resource = self.get_next_resource()
            while resource.busy: # check if resource is busy
                resource = self.get_next_resource() # get the next resource if current resource is busy
            resource.start_task(task)
            self.update_project_count(task.project)

    def get_next_resource(self):
        """
        Get the next available resource.
        """
        resource = self.resources[self.next_resource_index]
        self.next_resource_index += 1
        if self.next_resource_index == len(self.resources):
            self.next_resource_index = 0
        return resource

    def update_project_count(self, project_id):
        """
        Update the count of tasks for a given project.
        """
        self.projects[project_id]["count"] += 1
        self.projects[project_id]["project"] = project_id

    def get_project_count(self, project_id):
        """
        Get the count of tasks for a given project.
        """
        return self.projects[project_id]["count"]


if __name__ == '__main__':
    resources = [Resource(i) for i in range(2)]
    outside_interface = OutsideInterface()
    scheduler = Scheduler(resources, outside_interface)
    scheduler.run_scheduler()

