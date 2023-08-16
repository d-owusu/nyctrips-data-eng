#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import argparse
import os
from time import  time



def main(params) :
    
    user= params.user
    password =params.password
    host = params.host
    port =params.port
    db =params.db
    url=params.url
    table_name = params.table_name
    
    csv_name = 'output.csv'
    # Download CSV
    
    os.system(f"wget {url} -O {csv_name} ")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter=  pd.read_csv(csv_name, iterator= True, chunksize= 100000,compression='gzip')

    df=next(df_iter)


    #Columns to datetime
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime  = pd.to_datetime(df.tpep_pickup_datetime)

    df.head(n=0).to_sql( name='yellow_taxi_data' , con= engine, if_exists = 'replace')
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists= 'append')

    #Load data in batches

    while True:
        t_start = time()
        
        try:
            df = next(df_iter)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            
            df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
            
            t_end = time()
            print('Inserted another chunk, took %.3f seconds' % (t_end - t_start))
        
        except StopIteration:
            print('Finished inserting all data chunks.')
            break
        
        except Exception as e:
            print('Error occurred during data insertion:', e)
            # You can choose to handle the error accordingly, e.g., retry, log, or exit the loop.
            break
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help= 'user name for postgres')
    parser.add_argument('--password', help= 'password for postgres')
    parser.add_argument('--host', help= 'host for postgres')
    parser.add_argument('--port', help= 'user name for postgres')
    parser.add_argument('--db', help= 'database name for postgres')
    parser.add_argument('--table_name', help= 'name of where we write the results to')
    parser.add_argument('--url', help= 'url of csv file')

                        
    args = parser.parse_args()

    main(args)




