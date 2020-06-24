import unittest
from app import songs, predict
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk
import app
class ReportAppSongs(unittest.TestCase):
    def test_songs(self):
        unittest.FunctionTestCase(songs())
class ReportAppPredicts(unittest.TestCase):
    def test_predict(self):
        unittest.FunctionTestCase(predict())
        #RuntimeError: Working outside of request context.
        """
        (From console):
        This typically means that you attempted to use functionality
        that needed an active HTTP request. Consult the documentation
        on testing for information about how to avoid this problem.
        """
if __name__ == '__main__':
    unittest.main()