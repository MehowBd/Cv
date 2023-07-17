# <Michał Białożyt><406347>
# <Michał Badura><407049>
# <Piotr Suchy><407332>

import unittest
from collections import Counter
from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError
server_types = (ListServer, MapServer)

class ServerTest(unittest.TestCase):
    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))


class ListServerTest(unittest.TestCase):
    def test_init_method(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        list_server1 = ListServer(products)
        self.assertEqual(list_server1.n_max_returned_entries, 3)
        self.assertEqual(list_server1.products, [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)])

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))


class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server1 = server_type(products)
            client = Client(server1)
            self.assertEqual(5, client.get_total_price(2))

    def test_sorted_in_growing_price(self):
        products = [Product('PP123', 7), Product('PP134', 3), Product('PP145', 11)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            sorted_list = client.server.get_entries(2)
            self.assertEqual(3, sorted_list[0].price)
            self.assertEqual(7, sorted_list[1].price)
            self.assertEqual(11, sorted_list[2].price)

    def test_total_price_ex_thrown_no_products(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(3))
        products_2 = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 5), Product('PP237', 2)]
        for server_type in server_types:
            server = server_type(products_2)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))

class ExceptionTest(unittest.TestCase):
    def test_is_throwing_error(self):
        products = [Product('PP234', 21), Product('PP235', 7), Product('PP237', 32), Product('PP238', 68)]
        for server_type in server_types:
            server = server_type(products)
            self.assertRaises(TooManyProductsFoundError, server.get_entries, 2)

    def test_wrong_name(self):
        self.assertRaises(ValueError, Product, '2', 3)
        self.assertRaises(ValueError, Product, 'A', 1)
        self.assertRaises(ValueError, Product, '2A', 2)
        self.assertEqual('A1', Product('A1', 1).name)


if __name__ == '__main__':
    unittest.main()
