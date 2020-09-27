import unittest
import database_queries
import database_generator


class SimpleTest(unittest.TestCase):

    def test_get_all_skus(self):
        expected_sku_names = database_generator.SKU_names
        result = database_queries.get_all_skus()
        self.assertEqual(expected_sku_names.sort(), result.sort())

    def test_check_sku_not_available(self):
        expected_sku_names = "bottle_200ml"
        result = database_queries.get_all_skus()
        status = expected_sku_names in result
        self.assertFalse(status)

    def test_check_sku_available(self):
        expected_sku_names = "bottle_100ml"
        result = database_queries.get_all_skus()
        status = expected_sku_names in result
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
