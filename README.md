
## Description
In this project, I do an e2e data engineering on the Nyctrips data. 



## Dataset

Nyc trips data is a publically available dataset of the NYC Taxi andLimousine Commission. The data is made up of GReen and Yellow taxi trips in the Newyork area and contains data 2009 till date.  I use data from January 2019 till July 2021 which contains over 130 million rows. [Biqquery](https://github.com/d-owusu/Nyctrips-Data-Eng/blob/main/images/bq.png)


## Tech Stack
Cloud - [Google Cloud Platform](https://cloud.google.com/?hl=en) \
Iac - [Terraform](https://www.terraform.io/) \
Orchestration - [Prefect](https://www.prefect.io/), [Mage Ai](https://www.mage.ai/) \
Transformation - [dbt](https://www.getdbt.com/)  \
Data Lake - [Google Cloud Storage]()  \
Data Warehouse - [Bigquery]()  \
Data Visualisation  - [Tableau]()


## Architecture

![](https://github.com/d-owusu/Nyctrips-Data-Eng/blob/main/images/Architecture.png)




### Extras
 google cloud 
create a a project name and a service account
create and dowload a key
install google SDK
export google credentials to keyfile
 export GOOGLE_APPLICATIO_CREDENTIALS= '.json'
 
 using bash to communicate with gcp , 
 create an ssh connection in bash using
 ssh-keygen -t rsa -f ~/.ssh/KEY_FILENAME -C USERNAME -b 2048 [https://cloud.google.com/compute/docs/connect/create-ssh-keys]
 to google cloud compute engine, click on metadata and add your key to it and save
 
 
 create a config file with 
 Host "name of the file "
    Hostname "this is your gcp external id"
    User "gcp user name
    IdentityFile "path to your ssh key"

 using vscode as my editor, i can access the vscode remote on my gcp instance by installing 
 the extension remote-ssh 
 click on "connect host " and choose the config file you created
 
 install docker and docker compose in your instance 
 give permissions to run docker with
 1. sudo groupadd docker
 2. sudo gpasswd -a $USER docker "adds the user "
 3. sudo service restart docker
 4. logout of instance and log back in . 
 4 run "docker run hello-world"
 5. "docker run -it ubuntu bash"
 
 
 
 download docker compose from their github page . 
 "wget https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-linux-x86_64 -O docker-compose"
 add path to bashrc.
 
