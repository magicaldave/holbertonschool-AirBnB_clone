#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""

import unittest
import inspect
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base_model.py', 'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)


if __name__ == '__main__':
    unittest.main()
