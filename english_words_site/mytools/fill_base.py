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
    def get_correct_translation(string):
        result = ''
        for i in string:
            if i == ',' or i == ' ':
                break
            result += i
        return result

    @classmethod
    def __data_parcing(cls, html_content):
        word_list = []
        # Создаём объект BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        target_element = soup.find('table', id='wordlist')
        child_elements = target_element.find_all('tr')
        for child in child_elements:
            obj = (child.find_all('td')[1].text, cls.get_correct_translation(child.find_all('td')[2].text))
            word_list.append(obj)
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
        for word, translate in word_list:
            print(word , translate)
            new_product = (word, translate)

            request_to_insert_data = '''
                    INSERT INTO main_word (english, russian) VALUES (%s, %s);
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