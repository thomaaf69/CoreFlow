# test_coreflow.py
"""
Tests for CoreFlow module.
"""

import unittest
from coreflow import CoreFlow

class TestCoreFlow(unittest.TestCase):
    """Test cases for CoreFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreFlow()
        self.assertIsInstance(instance, CoreFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
