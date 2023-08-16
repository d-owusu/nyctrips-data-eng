from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials





@task(retries=3)
def extract_from_gcs(color:str, year: int, month:int) -> Path :
    
    gcs_path = f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("trip-gcs-prefect")
    gcs_block.get_directory(from_path =gcs_path,local_path= f"../data/")
    return Path(f"../data/{gcs_path}")

@task(retries=3)
def transform(path:Path) -> pd.DataFrame :
    """Data cleaning parquet"""
    df = pd.read_parquet(path)
    print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
    df['passenger_count'].fillna(0, inplace= True)
    print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    return(df)



@task()
def write_to_bq(df:pd.DataFrame) -> None :
    """write Dataframe to Biqquery"""
    gcp_credentials_block = GcpCredentials.load("my-creds")
    
    df.to_gbq(
        destination_table= "trips_dataset.trips", 
        project_id= "data-eng-389711",
        credentials= gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=  "500_000", 
        if_exists= "append",
        
    )
    

@flow()
def etl_to_bq() :
    """main ETL FLOW to load data to Big Query"""
    color = "yellow"
    year  = 2021
    month = 1
    
    path= extract_from_gcs(color,year,month) 
    df = transform(path)
    write_to_bq(df)
    
if __name__=="__main__":
    etl_to_bq()    
    
    