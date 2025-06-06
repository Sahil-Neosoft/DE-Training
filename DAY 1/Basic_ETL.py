import requests
import pandas as pd
import pymysql
from tabulate import tabulate
import logging

# Setup logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

# Fetching data from Rest Country API
def fetch_country_data():
    url="https://restcountries.com/v3.1/all"
    logging.info("Fetching data from Rest countries API")

    response=requests.get(url)
    response.raise_for_status()   
    data=response.json()

    countries=[]
    for country in data:
        try:
            countries.append({
                "name":country.get("name",{}).get("common","N/A"),
                "region":country.get("region","N/A"),
                "population":country.get("population",0),
                "area":country.get("area",0.0),
                "capital":country.get("capital",["N/A"])[0] # What if multiple capital for the same country
            })
        except Exception as e:
            logging.warning(f"Failed to parse country: {e}")
    return countries

# Save to csv
def save_to_csv(data, filename="countries.csv"):
    df=pd.DataFrame(data)
    df.to_csv(filename,index=False)
    logging.info(f"Data saved to csv file: {filename}")

#  Store Data in MySQL
def save_to_mysql(data,db_config):
    connection=pymysql.connect(**db_config)
    cursor=connection.cursor()

    cursor.execute("""
    create table countries(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        region VARCHAR(100),
        population BIGINT,
        area FLOAT,
        capital VARCHAR(100)
        )
    """)
    
    insert_query="""
    insert into countries(name,region,population,area,capital)
    values (%s, %s, %s, %s, %s) 
    """
    # %s are placeholders to safely insert values and prevent SQL injection.

    values=[(c["name"], c["region"], c["population"], c["area"], c["capital"]) for c in data]
    cursor.executemany(insert_query,values)
    connection.commit()
    logging.info(f"{cursor.rowcount} records inserted into MySQL.")
    return connection,cursor
    
def perform_aggregations(cursor):
    queries={
        "Total countries":"select count(*) from countries",
        "Total population":"select sum(population) from countries",
        "Average area":"select avg(area) from countries",
        "Population by region":"select region,sum(population) from countries group by region"
    }

    print("\n Aggregation Results:")
    for label,query in queries.items():
        cursor.execute(query)
        results=cursor.fetchall()
        print(f"\n{label}:")
        print(tabulate(results, headers=[desc[0] for desc in cursor.description], tablefmt="grid"))

def main():
    country_data=fetch_country_data()
    save_to_csv(country_data)

    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "testdb"
    }

    connection,cursor=save_to_mysql(country_data,db_config)
    perform_aggregations(cursor)

    cursor.close()
    connection.close()

if __name__=="__main__":
    main()