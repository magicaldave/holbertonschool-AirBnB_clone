#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""

import unittest
from unittest import mock
import inspect
import models
import pep8
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModelDocs(unittest.TestCase):
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


class TestBaseModel(unittest.TestCase):
    """test for BaseModel class"""

    def test_datetime(self):
        """Testing created_at and updated_at values and datetime objects"""
        tic = datetime.now()
        inst_1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst_1.crated_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst_2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst_2.created_at <= toc)
        self.assertEqual(inst_1.created_at, inst_1.updated_at)
        self.assertEqual(inst_2.created_at, inst_2.updated_at)
        self.assertNotEqual(inst_1.created_at, inst_2.created_at)
        self.assertNotEqual(inst_1.updated_at, inst_2.updated_at)


if __name__ == '__main__':
    unittest.main()
