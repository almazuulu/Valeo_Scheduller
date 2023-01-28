import unittest
from scheduler import Scheduler, Task, Resource

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()
        self.resource1 = Resource("resource1")
        self.resource2 = Resource("resource2")
        self.task1 = Task("task1", "project1", 1, self.resource1)
        self.task2 = Task("task2", "project2", 2, self.resource1)
        self.task3 = Task("task3", "project3", 3, self.resource2)
        self.task4 = Task("task4", "project4", 4, self.resource2)

    def test_add_task(self):
        self.scheduler.add_task(self.task1)
        self.scheduler.add_task(self.task2)
        self.scheduler.add_task(self.task3)
        self.scheduler.add_task(self.task4)
        self.assertEqual(len(self.scheduler.tasks), 4)

    def test_add_resource(self):
        self.scheduler.add_resource(self.resource1)
        self.scheduler.add_resource(self.resource2)
        self.assertEqual(len(self.scheduler.resources), 2)
        
    def test_get_next_task(self):
        self.scheduler.add_task(self.task1)
        self.scheduler.add_task(self.task2)
        self.scheduler.add_task(self.task3)
        self.scheduler.add_task(self.task4)
        next_task = self.scheduler.get_next_task()
        self.assertEqual(next_task, self.task1)
        
    def test_run_scheduler(self):
        self.scheduler.add_task(self.task1)
        self.scheduler.add_task(self.task2)
        self.scheduler.add_task(self.task3)
        self.scheduler.add_task(self.task4)
        self.scheduler.add_resource(self.resource1)
        self.scheduler.add_resource(self.resource2)
        self.scheduler.run_scheduler()
        self.assertEqual(self.resource1.current_task, self.task1)
        self.assertEqual(self.resource2.current_task, self.task2)
        
    def test_update_project_count(self):
        self.scheduler.update_project_count("project1")
        self.assertEqual(self.scheduler.projects["project1"]["count"], 1)
        
    
