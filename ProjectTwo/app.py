import sqlite3
import csv
import os

import pandas as pd
import numpy as np


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

conn = sqlite3.connect('LB_database.sqlite')
c = conn.cursor() #cursor allows you to run SQL commands using execute method

c.execute("DROP TABLE IF EXISTS LB_hvi")
c.execute("CREATE TABLE LB_hvi (\
			RegionName text,\
			State text,\
			SizeRank integer,\
			January real,\
			February real,\
			March real,\
			April real,\
			May real,\
			June real,\
			July real,\
			August real,\
			September real,\
			October real,\
			November real,\
			'id' INTEGER ,PRIMARY KEY ('id'))") 
#print("Table created successfully........")

HVI_file = 'LongBeach_HVI.csv'
HVI_file_path = f'/Users/jasmin/Data Analytics/ProjectTwo/datasets/{HVI_file}'

with open(HVI_file_path,'r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    my_data = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['RegionName'], i['State'], i['SizeRank'],\
    		i['January'], i['February'], i['March'],\
    		i['April'], i['May'], i['June'],\
    		i['July'], i['August'], i['September'],\
    		i['October'], i['November']) for i in my_data]

c.executemany("""INSERT INTO LB_hvi (RegionName, State, SizeRank,
	'January','February','March','April','May','June',
	'July','August','September', 'October', 'November')
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)

c.execute("DROP TABLE IF EXISTS LB_Rent_Sqft")
c.execute("CREATE TABLE LB_Rent_Sqft (\
			RegionName text,\
			State text,\
			SizeRank integer,\
			January real,\
			February real,\
			March real,\
			April real,\
			May real,\
			June real,\
			July real,\
			August real,\
			September real,\
			October real,\
			November real,\
			'id' INTEGER ,PRIMARY KEY ('id'))") 

Sqft_file = 'LongBeach_Rent_Sqft.csv'
Sqft_file_path = f'/Users/jasmin/Data Analytics/ProjectTwo/datasets/{Sqft_file}'

with open(Sqft_file_path,'r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    my_data_2 = csv.DictReader(fin) # comma is default delimiter
    to_db_2 = [(i['RegionName'], i['State'], i['SizeRank'],\
    		i['January'], i['February'], i['March'],\
    		i['April'], i['May'], i['June'],\
    		i['July'], i['August'], i['September'],\
    		i['October'], i['November']) for i in my_data_2]

c.executemany("""INSERT INTO LB_Rent_Sqft (RegionName, State, SizeRank,
	'January','February','March','April','May','June',
	'July','August','September', 'October', 'November')
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db_2)

c.execute("DROP TABLE IF EXISTS LB_Rent_Unit")
c.execute("CREATE TABLE LB_Rent_Unit (\
			RegionName text,\
			State text,\
			SizeRank integer,\
			January real,\
			February real,\
			March real,\
			April real,\
			May real,\
			June real,\
			July real,\
			August real,\
			September real,\
			October real,\
			November real,\
			'id' INTEGER ,PRIMARY KEY ('id'))") 

Unit_file = 'LongBeach_Rent_Unit.csv'
Unit_file_path = f'/Users/jasmin/Data Analytics/ProjectTwo/datasets/{Unit_file}'

with open(Unit_file_path,'r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    my_data_3 = csv.DictReader(fin) # comma is default delimiter
    to_db_3 = [(i['RegionName'], i['State'], i['SizeRank'],\
    		i['January'], i['February'], i['March'],\
    		i['April'], i['May'], i['June'],\
    		i['July'], i['August'], i['September'],\
    		i['October'], i['November']) for i in my_data_3]

c.executemany("""INSERT INTO LB_Rent_Unit (RegionName, State, SizeRank,
	'January','February','March','April','May','June',
	'July','August','September', 'October', 'November')
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db_3)

conn.commit()
c.execute("SELECT * FROM LB_hvi")
print(c.fetchall())
conn.close()


