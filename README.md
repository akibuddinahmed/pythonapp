# Python App

> Python App which exposes the following- 

  - a health endpoint which returns OK
  - an endpoint for inserting or updating a city and its population
  - an endpoint for retrieving the population of a city

## Pre-Requisit 
  - This app requires a PostgreSQL DB, set this details in `main.py`  
  - If you require to setup PostgreSQL for the first time in your K8s cluster, you may follow this article-https://phoenixnap.com/kb/postgresql-kubernetes 
  - Install Kompose using - https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/ 
  

# Install the app
  - if you require to set this up in a docker enviroment. 
    run the below command where docker-compose.yml file is located. The docker compose up command will start and run the entire app.
    `docker compose up`
  - To set the app in Kubernetes cluster: Run the below commands- 
        
        - kubectl apply -f app-claim0-persistentvolumeclaim.yaml
        - kubectl apply -f app-deployment.yaml
        - kubectl apply -f kubectl apply -f app-service.yaml
  

# Serve on localhost:5000
python app.py
