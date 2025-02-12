import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        # Run before all test
        print("setupClass")
        # return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        # Run after all test
        print("teardownClass")
        # return super().tearDownClass()
    
    def setUp(self) -> None:
        print("setUp")
        ## setUp code will run before every test
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)
        # return super().setUp()
    
    def tearDown(self) -> None:
        ## tearDown code will run after every test
        print('tearDown\n')
        # return super().tearDown()
    
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")
        
        self.emp_1.first = "John"
        self.emp_2.first = "Jane"
        
        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")    
    
    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")  
        
        self.emp_1.first = "John"
        self.emp_2.first = "Jane"
        
        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")  
        
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    