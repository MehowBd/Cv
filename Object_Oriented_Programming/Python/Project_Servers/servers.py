# <Michał Białożyt><406347>
# <Michał Badura><407049>
# <Piotr Suchy><407332>


from typing import Optional, TypeVar, List, Dict
from abc import ABC, abstractmethod
import re


class Product:
    def __init__(self, name: str, price: float):
        match = re.fullmatch('^[a-zA-Z]{{1,}}[1234567890]{{1,}}$'.format(), name)
        if match is None:
            raise ValueError
        else:
            self.name = name
            self.price = price

    def __eq__(self, other):
        if self.name == other.name and self.price == other.price:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.price))


class Server(ABC):
    n_max_returned_entries = 3

    @abstractmethod
    def get_list(self, n_letters: Optional[int]) -> List[Product]:
        pass

    @staticmethod
    def check_name(name: str, n_letters: Optional[int]) -> bool:
        match = re.fullmatch('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters), name)
        if match is not None:
            return True
        else:
            return False

    def get_entries(self, n_letters: Optional[int]) -> List[Product]:
        entries_products_not_sorted = self.get_list(n_letters)
        if len(entries_products_not_sorted) > self.n_max_returned_entries:
            raise TooManyProductsFoundError(msg=f'Znaleziono {len(entries_products_not_sorted)} produktów')
        else:
            return sorted(entries_products_not_sorted, key=lambda product: product.price)


ServerType = TypeVar('ServerType', bound=Server)


class ServerError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


class TooManyProductsFoundError(ServerError):
    def __init__(self, msg=None, *args, **kwargs):
        if msg is None:
            msg = 'Zła liczba produktów!'
        super().__init__(*args, **kwargs)
        self.msg = msg


class ListServer(Server):
    def __init__(self, products_: List[Product]):
        self.products: List[Product] = []
        for product_index in range(len(products_)):
            self.products.append(products_[product_index])

    def get_list(self, n_letters: Optional[int]) -> List[Product]:
        entries_products = []
        for product in self.products:
            if self.check_name(product.name, n_letters):
                entries_products.append(product)
        return entries_products


class MapServer(Server):
    def __init__(self, products: List[Product]):
        self.products: Dict[str: Product] = {}
        for product in products:
            self.products[product.name] = product

    def get_list(self, n_letters: Optional[int]) -> List[Product]:
        entries_products = []
        for product in self.products.values():
            if self.check_name(product.name, n_letters):
                entries_products.append(product)
        return entries_products


class Client:
    def __init__(self, server_: ServerType):
        self.server = server_

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            list_of_products = self.server.get_entries(n_letters)
            if not list_of_products:
                raise TooManyProductsFoundError
            total_price = 0
            for product in list_of_products:
                total_price += product.price
            return total_price
        except TooManyProductsFoundError:
            return None
