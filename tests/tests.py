from unittest import TestCase
from protected.string import ProtectedString

PROTECTED_STRING = 'my_secret'

class ProtectedStringTestCase(TestCase):
    """
    Tests ProtectedString class of protected class
    More info: http://wnyc.github.io/protected/
    """

    def setUp(self):
        self.protected_string = ProtectedString(PROTECTED_STRING)
        self.random_string = "This is %s!" % self.protected_string

    def test_protected_string_equals(self):
        self.assertEqual(str(self.protected_string), PROTECTED_STRING)
        self.assertEqual(str(self.random_string), 'This is my_secret!')

    def test_protected_string_notequals(self):

        self.assertNotEqual('This is %s!' % (PROTECTED_STRING),
                                 self.protected_string)

    def test_protected_string_true(self):
        self.assertTrue(bool(ProtectedString("abc")))

    def test_protected_string_false(self):
        self.assertFalse(bool(ProtectedString("")))

    def test_protected_string_assert_instance(self):
        self.assertTrue(isinstance(self.protected_string, ProtectedString))

    def test_protected_string_add(self):
        ps_a = ProtectedString('abc') + 'def'
        self.assertTrue(isinstance(ps_a, ProtectedString))
        self.assertEqual(str(ps_a), 'abcdef')

    def test_protected_string_radd(self):
        ps_b = 'abc' + ProtectedString('def')
        self.assertTrue(isinstance(ps_b, ProtectedString))
        self.assertEqual(str(ps_b), 'abcdef')

    def test_protected_string_replace(self):
        ps_c = ProtectedString("abcdef").replace('b', 'd')
        self.assertEqual(str(ps_c), 'adcdef')
        

    def test_multiplication(self):
        self.assertEqual(ProtectedString('a') * 10, 'a' * 10) 

