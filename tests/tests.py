try:
    from unittest import TestCase, SkipTest
except ImportError:
    from unittest2 import TestCase, SkipTest

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
        self.assertTrue(ProtectedString("abc"))

    def test_protected_string_false(self):
        self.assertFalse(ProtectedString(""))

    def test_protected_string_assert_instance(self):
        self.assertTrue(isinstance(self.protected_string, ProtectedString))

    def test_protected_string_add(self):
        protected_string = ProtectedString('abc') + 'def'
        self.assertTrue(isinstance(protected_string, ProtectedString))
        self.assertEqual(str(protected_string), 'abcdef')

    def test_protected_string_radd(self):
        protected_string = 'abc' + ProtectedString('def')
        self.assertTrue(isinstance(protected_string, ProtectedString))
        self.assertEqual(str(protected_string), 'abcdef')

    def test_protected_string_replace(self):
        raise SkipTest("https://github.com/wnyc/protected/issues/4")
        protected_string = ProtectedString("abcdef").replace('b', 'd')
        self.assertTrue(isinstance(protected_string, ProtectedString))
        self.assertEqual(str(protected_string), 'adcdef')
        

    def test_multiplication(self):
        self.assertEqual(ProtectedString('a') * 10, 'a' * 10) 

