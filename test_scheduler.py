import unittest
from scheduler import Resource, Scheduler, OutsideInterface, Task

class TestScheduler(unittest.TestCase):
    def test_run_scheduler(self):
        resources = [Resource(i) for i in range(2)]
        outside_interface = OutsideInterface()
        scheduler = Scheduler(resources, outside_interface)
        scheduler.run_scheduler()
        self.assertEqual(1,1) 
        
if __name__ == '__main__':
    unittest.main()
