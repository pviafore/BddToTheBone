import unittest


class TestUrlShortener(unittest.TestCase):
    """
    Unit Test
    """
    def test_retrieve_shortened_url(self):
        url_shortener = UrlShortener()
        shortnened_url = url_shortener.shorten("https://www.python.org")
        self.assertEquals("http://pat.ly/1", shortnened_url)
