from src.main import print_hi
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

class PrintingTest(TestCase):

    def test_print_hi(self):
        name = 'test'
        expected_output = 'Hi, {}\n'.format(name)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_hi(name)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_empty(self):
        name = ''
        expected_output = 'Hi stranger\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_hi(name)
            self.assertEqual(fake_out.getvalue(), expected_output)