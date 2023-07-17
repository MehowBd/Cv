import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple


def film_in_category(category_id: int)->pd.DataFrame:
    ''' 
    Parameters:
    category_id (int): the value of the id of the category for which we are performing the query
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(category_id, int):
        result = pd.read_sql(f'''select film.title, language.name as languge, category.name as category
                            from category 
                            left join film_category
                            on category.category_id = film_category.category_id 
                            left join film 
                            on film_category.film_id = film.film_id 
                            left join language 
                            on film.language_id = language.language_id 
                            where category.category_id = {category_id} 
                            order by film.title ASC, language.name ASC ''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None

    
def number_films_in_category(category_id:int)->pd.DataFrame:
    ''' 
    Parameters:
    category_id (int): the value of the id of the category for which we are performing the query
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(category_id, int):
        result = pd.read_sql(f'''select category.name as category, count(film.title) 
                            from category 
                            inner join film_category 
                            on category.category_id = film_category.category_id 
                            inner join film 
                            on film_category.film_id = film.film_id 
                            where category.category_id = {category_id} 
                            group by category.name''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None

def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    ''' 
    Parameters:
    min_length (int,float): value of the minimum film length
    max_length (int,float): value of the maximum film length
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(min_length, (int,float)) and isinstance(max_length, (int,float)) and min_length<max_length:
        result = pd.read_sql(f'''select film.length, count(film.title)
                            from film
                            where film.length between {min_length} and {max_length}
                            group by film.length''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None

def client_from_city(city:str)->pd.DataFrame:
    ''' 
    Parameters:
    city (str): name of the city for which we are to compile a list of customers
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(city, str):
        result = pd.read_sql(f'''select city.city, customer.first_name, customer.last_name
                            from city
                            inner join address
                            on city.city_id = address.city_id
                            inner join customer
                            on address.address_id = customer.address_id
                            where city.city = '{city}'
                            order by customer.first_name ASC, customer.last_name ASC''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None
def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    '''     
    Parameters:
    length (int,float): the length of the film for which we are to borrow the average value of borrowed films
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(length, (int, float)):
        result = pd.read_sql(f'''select film.length, avg(payment.amount)                            from film
                            left join inventory
                            on film.film_id = inventory.film_id 
                            left join rental
                            on inventory.inventory_id = rental.inventory_id
                            left join payment 
                            on rental.rental_id = payment.rental_id
                            where film.length = {length}
                            group by film.length''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None

def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    '''
    Parameters:
    sum_min (int,float): the minimum value of the sum of the length of the rented films that the customer must meet
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(sum_min, (int, float)):
        result = pd.read_sql(f'''select customer.first_name, customer.last_name, sum(film.length) 
                            from customer
                            left join rental 
                            on customer.customer_id = rental.customer_id 
                            left join inventory 
                            on rental.inventory_id = inventory.inventory_id 
                            left join film 
                            on inventory.film_id = film.film_id 
                            group by customer.first_name, customer.last_name
                            having sum(film.length) >= {sum_min} 
                            order by sum(film.length) ASC, customer.last_name ASC, customer.first_name ASC''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None

def category_statistic_length(name:str)->pd.DataFrame:
    ''' 
    name (str): The name of the category for which statistics are to be extracted
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(name, str):
        result = pd.read_sql(f'''select category.name as category, avg(film.length) as avg, sum(film.length), min(film.length), max(film.length) 
                            from category 
                            left join film_category
                            on category.category_id = film_category.category_id 
                            left join film 
                            on film_category.film_id = film.film_id 
                            where category.name = '{name}' 
                            group by category.name''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None

def main():
    print(film_in_category(1))
    print(number_films_in_category(1))
    print(number_film_by_length(48, 50))
    print(client_from_city('Athenai'))
    print(avg_amount_by_length(48))
    print(client_by_sum_length(1260))
    print(category_statistic_length('Action'))

if __name__ == "__main__":
    main()
