# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:33:54 2023

@author: mixpp
"""

from configparser import ConfigParser
config=ConfigParser()
config.read("config.ini")
# config.read("F:\Datacookie\content\other\config file\config.ini")
print(config.sections())
print(list(config['account']))

host=config['account']['host']
db=config['account']['database']
user=config['account']['user']
password=config['account']['pass']

import mysql
import mysql.connector as msql
from mysql.connector import Error

try:
    conn = msql.connect(host=host,
                        database=db,
                        user=user,
                        password=password)

except Error as e:

    print("Error while connecting to MySQL now ", e)
    
    
import pandas as pd
df=pd.read_sql("SELECT * FROM `P1-OfficeSupplies`",con=conn)
df
