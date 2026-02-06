# test_smartvortex.py
"""
Tests for smartVortex module.
"""

import unittest
from smartvortex import smartVortex

class TestsmartVortex(unittest.TestCase):
    """Test cases for smartVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = smartVortex()
        self.assertIsInstance(instance, smartVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = smartVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
