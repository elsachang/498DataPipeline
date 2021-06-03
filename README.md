# capstone498

#Airflow and GCP

Purpose of this project is to automate traditional ETL that is inefficient. Like most development operations these days, cloud services do most of the work. Data engineeering is no exception. Using Google Cloud Composer reduces time spent on DevOps. Developers just focus on building workflows, and Composer manages the infrastructure. 

Let's look into the advantages of Apache Airflow and Google Cloud Platform. A little bit history about Airflow, it is an open source project developed by Airbnb Data Science team in 2016.

Airflow
- Python
- Good interfaces (CLI/Webserver/API server)
- Flexible scheduling and dependency management with Retries
- Rich library of connectors
- Active community support

Google Cloud Platform
- Infrastructure scalability and reliability
- Secured (Cloud IAP-protected web server)
- Ease of use
- Automatic DAG synchronization
- One-click deployment
- Cost effectve
- Operability & Maintainance - easy Python dependency management and Airflow configuation update propagation

However, Airflow also has its disadvantages, such as uneasy setup & management. It also lacks logging/debugging.
In addition, GCP does not have an orchestration solution.


To Start, you will need to install the necessary tools, such as -
- Dockers
- Docker Compose
- Python Package Index

Next steps

In your terminal, type docker-compose up -d
After that you build the image by typing
docker-compose up -d --build

To check whether your Airflow is installed correctly, you may go to - 
http://localhost:8080/
From there you should see your Airflow is live.

Next thing we need to do is setting up GCP.

<img width="1327" alt="Screen Shot 2021-06-02 at 10 04 01 PM" src="https://user-images.githubusercontent.com/181012/120722430-9174a500-c484-11eb-98a1-1dd200424024.png">

After that we need to start writing the DAG flow and dependency.

![airflow-example-dag](https://user-images.githubusercontent.com/181012/120722509-ae10dd00-c484-11eb-9f7c-8491e56850aa.png)


How do you schedule when the data is pulled?

![Screen Shot 2021-05-15 at 8 26 47 PM](https://user-images.githubusercontent.com/181012/120722788-44450300-c485-11eb-87d9-a832b6543032.png)

