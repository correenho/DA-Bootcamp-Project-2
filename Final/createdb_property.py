import sqlite3
import csv
conn = sqlite3.connect('Zillow_database.sqlite')
c = conn.cursor() #cursor allows you to run SQL commands using execute method
c.execute("DROP TABLE IF EXISTS buy_list")
c.execute("CREATE TABLE buy_list (\
			address text,\
    		price text,\
    		details text,\
    		zipcode integer,\
    		latitude real,\
    		longitude real,\
    		zpid integer,\
    		link text\
			)") 
print("Table 1 created successfully........")

csv_file_buy = 'buy_full_list.csv'
csv_file_path_buy = f'C:/Users/corre/Documents/0.0_UCI_DA_Bootcamp_inClass/19-Project_2/Data/{csv_file_buy}'
with open(csv_file_path_buy,'r') as buy: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    my_data = csv.DictReader(buy) # comma is default delimiter
    to_db = [(i['address'], i['price'], i['details'],\
    		i['zipcode'], i['latitude'], i['longitude'],\
    		i['zpid'], i['link']) for i in my_data]
c.executemany("""INSERT INTO buy_list (address, price, details,
	zipcode, latitude, longitude, zpid, link)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?);""", to_db)
c.execute("SELECT * FROM buy_list") #this is to test via terminal that the data was inserted successfully
print(c.fetchall())

c.execute("DROP TABLE IF EXISTS rent_list")
c.execute("CREATE TABLE rent_list (\
			address text,\
			price text,\
			details text,\
			zipcode integer,\
			lat real,\
			lng real,\
			zpid integer,\
			link text\
	)")
print("Table 2 created successfully......")

csv_file_rent = 'rent_full_list.csv'
csv_file_path_rent = f'C:/Users/corre/Documents/0.0_UCI_DA_Bootcamp_inClass/19-Project_2/Data/{csv_file_rent}'
with open(csv_file_path_rent,'r') as rent: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    my_data_2 = csv.DictReader(rent) # comma is default delimiter
    to_db = [(i['address'], i['price'], i['details'],\
    		i['zipcode'], i['lat'], i['lng'],\
    		i['zpid'], i['link']) for i in my_data_2]
c.executemany("""INSERT INTO rent_list (address, price, details,
	zipcode, lat, lng, zpid, link)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?);""", to_db)
c.execute("SELECT * FROM rent_list") #this is to test via terminal that the data was inserted successfully

print(c.fetchall())


conn.commit()
conn.close()