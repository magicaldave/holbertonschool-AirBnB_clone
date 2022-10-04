#!/usr/bin/python3
"""
This module is the unittest for the class: Filestorage.
"""
import os.path
import unittest
import pep8
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFilestorageClass(unittest.TestCase):
    """
    This class is for testing Filestorage.
    """

    def setUp(self):
        """
        Setup method.
        """
        self.User1 = BaseModel()
        self.User2 = BaseModel()
        self.fsUser = FileStorage()
        storage.save()

    def tearDown(self):
        """
        Teardown method.
        """
        del self.User1
        del self.User2
        storage.save()

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(FileStorage.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(FileStorage.all.__doc__) >= 1)
        self.assertTrue(len(FileStorage.new.__doc__) >= 1)
        self.assertTrue(len(FileStorage.save.__doc__) >= 1)
        self.assertTrue(len(FileStorage.reload.__doc__) >= 1)

    def test_all(self):
        """
        Testing all.
        """
        new_dict = self.fsUser.all()
        self.assertIsInstance(new_dict, dict)
        self.assertTrue(len(new_dict) > 0)

    def test_new(self):
        """
        Testing new.
        """
        self.User3 = BaseModel()
        new_dict = self.fsUser.all()
        self_key = "{}.{}".format(self.User3.__class__.__name__, self.User3.id)
        self.assertIn(self_key, new_dict.keys())

    def test_save(self):
        """
        Testing save.
        """
        self.User1.save()

        self.assertEqual(os.path.exists('testdata.json'), True)

    def test_reload(self):
        """
        Testing reload.
        """
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)
