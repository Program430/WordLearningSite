import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.append(parent_dir)

import mysql.connector as con
import requests
from bs4 import BeautifulSoup
from my_settings import *

connection = con.connect(
    host='localhost',
    user=sql_name,
    password=sql_password,
    database=sql_database_name
)

url = 'https://studynow.ru/dicta/allwords'

class DataToDB:
    @staticmethod
    def __data_parcing(html_content):
        word_list = []
        # Создаём объект BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        target_element = soup.find('table', id='wordlist')
        child_elements = target_element.find_all('tr')
        for child in child_elements:
            word_list.append(child.find_all('td')[1].text)
        return word_list

    @staticmethod
    def __words_to_file():
        pass

    @staticmethod
    def __get_data_from_server():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        response = requests.get(url, headers=headers)
        return response.text

    @staticmethod
    def __insert_to_db(word_list):
        cursor = connection.cursor()
        for word in word_list:
            print(word)
            new_product = (word,)

            request_to_insert_data = '''
                    INSERT INTO main_word (english) VALUES (%s);
                    '''
            try:
                cursor.execute(request_to_insert_data, new_product)
            except:
                pass
            connection.commit()

        cursor.close()
        connection.close()

    @classmethod
    def controller(cls):
        html = cls.__get_data_from_server()
        word_list = cls.__data_parcing(html)
        cls.__insert_to_db(word_list)


DataToDB.controller()


# import random

# list1 = []
# index_list = []

# class DellTester:
#     @staticmethod
#     def __full(count, indexes):
#         a = 1
#         b = 1000
#         for i in range(count):
#             list1.append(random.randint(a, b))
#         l = len(list1)
#         for i in range(indexes):
#             rd = random.randint(a, b)
#             if rd not in index_list and rd < l:
#                 index_list.append()

#     @staticmethod
#     def __del_tester():
#         for i in list1:
#             del i

#     @classmethod
#     def test(cls):
#         cls.__full(100)
#         cls.__del_tester()

# class T:
#     def __init__(self):
#         self.data = [1, 2 ,3]

#     def list(self):
#         return self.data

# a = T()

# print(list(a))



# import time
# import requests
# import aiohttp


# class GetDataFromServer:
#     def __init__(self):
#         pass

#     def get_data(self, url, headers):
#         try:
#             data = requests.get(url,
#                                 params=headers)
#         except :
#             return 'Error'

#         data = data.json()['results']
#         return data


# headers = {
# }

# first_request = GetDataFromServer()

# for i in range(1, 10):
#     headers['page'] = i
#     print(first_request.get_data('http://127.0.0.1:8000/api/get_word', headers))
