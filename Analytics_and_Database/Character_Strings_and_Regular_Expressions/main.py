import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' A function that returns the result of a database query for the movie title, language, and category for a given:
  
    Parameters:
    category (int,str): The value of the category by id (if of type int) or name (if of type str) for which we perform the query
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(category, int):
        result = pd.read_sql(f'''select film.title, language.name as languge, category.name as category
                            from category 
                            inner join film_category
                            on category.category_id = film_category.category_id 
                            inner join film 
                            on film_category.film_id = film.film_id 
                            inner join language 
                            on film.language_id = language.language_id 
                            where category.category_id = {category}
                            order by film.title ASC, language.name ASC ''', con=connection)
        if result is None:
            return None
        else:
            return result
    elif isinstance(category, str):
        result = pd.read_sql(f'''select film.title, language.name as languge, category.name as category
                            from category 
                            inner join film_category
                            on category.category_id = film_category.category_id 
                            inner join film 
                            on film_category.film_id = film.film_id 
                            inner join language 
                            on film.language_id = language.language_id 
                            where category.name like '{category}'
                            order by film.title ASC, language.name ASC ''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' A function that returns the result of a database query for the movie title, language, and category for a given:
    
    Parameters:
    category (int,str): The value of the category by id (if of type int) or name (if of type str) for which we perform the query
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(category, int):
        result = pd.read_sql(f'''select film.title, language.name as languge, category.name as category
                            from category 
                            inner join film_category
                            on category.category_id = film_category.category_id 
                            inner join film 
                            on film_category.film_id = film.film_id 
                            inner join language 
                            on film.language_id = language.language_id 
                            where category.category_id = {category}
                            order by film.title ASC, language.name ASC ''', con=connection)
        if result is None:
            return None
        else:
            return result
    elif isinstance(category, str):
        result = pd.read_sql(f'''select film.title, language.name as languge, category.name as category
                            from category 
                            inner join film_category
                            on category.category_id = film_category.category_id 
                            inner join film 
                            on film_category.film_id = film.film_id 
                            inner join language 
                            on film.language_id = language.language_id 
                            where category.name ilike '{category}'
                            order by film.title ASC, language.name ASC ''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None
    
def film_cast(title:str)->pd.DataFrame:
    ''' A function that returns the result of a database query for the cast of a movie with the exact given title.
        
    Parameters:
    title (int): the value of the id of the category for which we are performing the query
    
    Returns:
    pd.DataFrame: DataFrame zawierająca wyniki zapytania
    '''
    if isinstance(title, str):
        result = pd.read_sql(f'''select actor.first_name, actor.last_name 
                                        from actor 
                                        left join film_actor 
                                        on actor.actor_id = film_actor.actor_id 
                                        left join film 
                                        on film_actor.film_id = film.film_id
                                        where film.title ilike '{title}'
                                        order by actor.last_name ASC, actor.first_name ASC''', con=connection)
        if result is None:
            return None
        else:
            return result
    else:
        return None
    

def film_title_case_insensitive(words:list) :
    ''' A function that returns the result of a database query for movie titles containing at least one of the given words from the words list.
    
    Parameters:
    words(list): value of the minimum film length
    
    Returns:
    pd.DataFrame: DataFrame containing the results of the query
    '''
    if isinstance(words, list):
        con_words = '|'.join(words)
        result = pd.read_sql(f"""select film.title
                                from film
                                where film.title ~* '(?:^| )({con_words})"""+"""{1,}(?:$| )'
                                order by film.title""", con=connection)
        if result is None:
            return None
        else:
            return result
    else:
          return None