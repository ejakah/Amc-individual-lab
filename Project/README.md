* Project Title: *Implementation of a Cloud-Based Web Application Deployment Strategy on Amazon Web Services (AWS) Utilizing Virtual Private Cloud (VPC), GitHub Version Control, Docker Containerization, Kubernetes Orchestration, and Ngrok Tunneling with Kubernetes Load Balancing.*


# RUN DOCKER, MINIKUBE START, configuration for a Kubernetes Service file & deployment file 

`docker run -p 80:80 ejakah/amc-wintersemester`

`docker ps`

`docker stop image ID`

`minikube start` 

`kubectl get svc -n ejaka (EXTERNAL IP)`

`minikube service amc-lab -n ejaka (URL LINK)`

`minikube service amc-lab -n ejaka --url  (URL LINK)`

# VERIFY THE THREE RUNNING REPLICALS OR PODS 

`kubecolor get pods --namespace=ejaka`

`kubectl get pods --namespace=ejaka`

# WE DELETE ONE OF THE PODS TO DETERMINE IF ANOTHER POD WILL BE AUTOMATICALLY CREATED BASED ON AUTO-HEALING.
# NOTE, EDIT THE NAME SPACE ID YOU WISH TO DELETE e.g 

* amclab-deployment-bf6f9b6fb-b8z84 *

`kubectl delete pod amclab-deployment-bf6f9b6fb-b8z84 --namespace=ejaka`

# DELETE ALL RUNNING PODS 
`kubectl delete pods --namespace=ejaka --all`

# DELETE SERVICE 
`kubectl delete service amc-lab -n ejaka`

# RECREATE SERVICE 
`kubectl apply -f service.yaml`

# VERIFY THE NEW SERVICE
`kubectl get services -n ejaka`








# Task 1 - Install Docker and Docker-Compose:
  `apt install docker`

`docker ps`
`docker ps -a`
#
`docker stop 2a20189b00a5`
`docker rm 2a20189b00a5`
#
`docker rmi hostname-color-webapp:latest`

# If you still face issues, you might need to force the removal by adding the *-f flag:* 

`docker rmi -f hostname-color-webapp:latest`
`docker run -p 20231:80 patrickdevops:latest`
#
`docker build --no-cache -t patrickdevops:latest -f Dockerfile .`
#
`python3 -m venv venv`
`source venv/bin/activate`

#
`docker build -t hostname-color-webapp . `

`docker run -p 80:80 hostname-color-webapp`


# Listing running Docker images with their tag (*registry/namespace/name:tag*) use the command below

`docker inspect --format '{{.Config.Image}}' $(docker ps --format='{{.ID}}')`


## craete ec2 instance
`sudo apt-get update`
`mkdir amc-project`
#
`cd amc-project`


## clone github code and check docker file
`cd folder`

`ubuntu>amc-project>github folder have to install docker`

# Install Docker
`sudo apt-get install docker.io`


# If docker container permission denied
`docker images`
`sudo usermod -a -G docker $USER`
#
`sudo reboot`

`git clone https://github.com/ejakah/devops-project.git`
#

`ls`

`docker build -t amclab:dockerimage . `
#
`docker run -d -p 8000:8000 amclab:dockerimage`

`docker login`
#
*`ejakah`*
*`password`*

#

`docker image tag amclab:dockerimage ejakah/amclab:dockerimage`

`docker image push ejakah/amclab:dockerimage`


# Log in to Docker Hub (if not already logged in)

`docker login`

# Tag your Docker image with your Docker Hub username and repository name
`docker tag your-image-name:your-tag your-docker-hub-username/your-repository-name:your-tag`

`docker tag individual-lab:latest ejakah/amc-wintersemester:latest`

# Push the image to Docker Hub
`docker push your-docker-hub-username/your-repository-name:your-tag`

`docker push ejakah/amc-wintersemester:latest`
#

`docker image tag hostname-color-webapp:latest ejakah/amc-project:latest`

`docker image push ejakah/amc-project:latest`



# IF WE DECIDE NOT TO PUSH, BECAUSE WE HAVE AN EXISTING DOCKER IMAGE FROM PROXY, (*Public docker hub register*) THEN WE USE THE FOLLOWING

`docker rmi amclab:dockerimage`
`docker stop e05bf729681a`
#
`docker rm e05bf729681a`
`docker rmi ejakah/amclab:dockerimage`

#

`docker pull ejakah/amc-wintersemester:latest`
`docker images`

#

`docker ps`
`docker run -d -p 80:80 ejakah/amc-wintersemester:latest`

# KUBERNATES SETUP 1) START WITH MINIKUBE INSTALLATION BELOW

`curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`
`sudo install minikube-linux-amd64 /usr/local/bin/minikube`

#

`minikube start`

# KUBERNATES SETUP 2) START WITH KUBECTL INSTALLATION BELOW

`snap install kubectl --classic`

# VERIFY KUBECTL CONFIGURATION 

`minikube status`

`kubectl cluster-info`
#
`kubectl cluster-info dump`

# INTERACT WITH CLUSTERS
`kubectl get po -A`
`minikube kubectl -- get po -A`
#
`alias kubectl="minikube kubectl --"`
`minikube addons enable metrics-server`
#
`minikube dashboard`
`kubectl config current-context`
#
`minikube stop`
`minikube start`
#
`kubectl get namespaces`
`kubectl get pods --namespace=kube-system`
#
`kubectl create namespace ejaka`
`kubectl get namespaces`

# CREAT DEPLOYMENT YAML FILE
`vim deployment.yaml`

# COPY THE FOLLOWING CODE AND PAST

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: amclab-deployment
  labels:
    app: web-app
  namespace: ejaka
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: ejakah/amc-wintersemester:latest
        ports:
        - containerPort: 80
        
```

# SAVE THE ABOVE FILE 

`kubectl apply -f deployment.yaml`

`kubectl get pods --namespace=ejaka`

# WE DELETE ONE OF THE PORT TO DETERMINE IF ANOTHER PORT WILL BE AUTOMATICALLY CREATED BASE ON AUTO HEALING

# NOTE, EDIT THE NAME SPACE ID YOU WISH TO DELET *e.g*
* amclab-deployment-bf6f9b6fb-b8z84

`kubectl delete pod amclab-deployment-bf6f9b6fb-b8z84 --namespace=ejaka`

# TO GET THREE HOST ID (PODS IP ADDRESS) BASE ON OUR 3 REPLICAL WE USE COMMAND 

`kubectl get pods -o wide -n ejaka`

# CREAT SERVICE YAML FILE (Load Balancer service)

`vim service.yaml`

# COPY THE FOLLOWING CODE AND PAST

```
apiVersion: v1
kind: Service
metadata:
  name: amc-lab
  namespace: ejaka
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP

```    

# TO CREAT A SINGLE CLUSTER IP ADDRESS FOR 3 PODS

`kubectl apply -f service.yaml`

# Check the status of your LoadBalancer service to get the external IP:

`kubectl get svc -n ejaka`


# deploy the application.
`minikube service amc-lab -n ejaka --url`

# EDIT THE HTTP ADDRESS BELOW WITH THE ONE IN DISPLACE 

`curl -L http://192.168.49.2:32644`

`minikube service amc-lab -n ejaka`
#

`minikube dashboard`

# LOGIN TO NGROK, GO TO THE WEBSITE COPT THE LINUX LINK ADDRESS TYPE WGET AND PASTE THE ADDRESS TO DOWNLOAD AND UNZIP THE FILE 

`wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz`

`tar -xvzf ngrok-v3-stable-linux-amd64.tgz` 



# Authenticate yourself with ngrok: Go to the ngrok page and you will see under *option 2 <Connect your account>.* Now copy the command and run your local machine.


`sudo snap install ngrok`

`ngrok config add-authtoken 2XEf8P1eHcu8lPRBi93zdsxLecH_2fKp1WXpzRW4dRvuQSbXo`

# EDIT ONLY THE IP AND PORT ADDRESS BELOW WITH YOUR CLUSTER IP
`ngrok http 192.168.49.2:32644`

# COPPY THIS FORWARDING LINK FROM THE DISPLAY TERMINAL 
* https://0ead-54-209-19-230.ngrok-free.app



## Setting up Prometheus and Grafana for monitoring involves deploying both tools in your Kubernetes cluster. Prometheus will collect and store metrics, while Grafana will provide a visualization dashboard


# Step 1: Install *Helm*

`sudo snap install helm --classic`

`helm version`

# Step 2: Install *Prometheus and Grafana* using Helm:

# Add Prometheus Helm chart repository
`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
`helm repo update`

# Ensure to run kubernates cluster IP before installing Prometheus
`minikube start` 
`minikube service amc-lab -n ejaka`




# Step1 Install Prometheus





# Create Namespace and Add Helm Charts Repo
`kubectl create namespace kubernetes-monitoring`

# Add Prometheus-community repo (copy the command below same way it is)
`helm repo add Prometheus-community \
https://prometheus-community.github.io/helm-charts`

# To update the helm repo 
 `helm repo update`
 
# Deploying Helm Charts to Created Namespace

`helm install monitoring prometheus-community/kube-prometheus-stack --namespace kubernetes-monitoring`

# run the following command to confirm your Kube-Prometheus stack deployment.

`kubectl get pods -n kubernetes-monitoring`


# Accessing the Prometheus Instance and Viewing the Internal State Metrics

`kubectl get svc -n kubernetes-monitoring`

# Look for the service associated with Prometheus

`kubectl get services -n kubernetes-monitoring`

# Replace "YOUR_PROMETHEUS_SERVICE_NAME" with the actual name of the Prometheus service in your namespace. After running this command, you should be able to access the Prometheus web UI at http://localhost:9090 in your browser.

`kubectl port-forward svc/YOUR_PROMETHEUS_SERVICE_NAME -n kubernetes-monitoring 9090`



# Step2 Install Prometheus alternative to step1
`helm install my-prometheus prometheus-community/prometheus`

# Get the Prometheus server URL by running these commands in the same shell:

`export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=my-prometheus" -o jsonpath="{.items[0].metadata.name}")`

#

`kubectl --namespace default port-forward $POD_NAME 9090`


# Get the Alertmanager URL by running these command

`export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=my-prometheus" -o jsonpath="{.items[0].metadata.name}")`

#

`kubectl --namespace default port-forward $POD_NAME 9093`

#
`export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=my-prometheus" -o jsonpath="{.items[0].metadata.name}")`

#

`kubectl --namespace default port-forward $POD_NAME 9091`


# Add Grafana Helm chart repository
`helm repo add grafana https://grafana.github.io/helm-charts`
`helm repo update`

# Install Grafana
`helm install my-grafana grafana/grafana`

# 1. Get your 'admin' user password by running:
`kubectl get secret --namespace default my-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`

# Coppy the encrpted key password from the display terminal
* dlKZFFgAw9ZJWYmTYLOiMGiKiFKhg0rZSeuzSTU1

# 2. Get the Grafana URL to visit by running these commands in the same shell:
`export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=my-grafana" -o jsonpath="{.items[0].metadata.name}")`

#
`kubectl --namespace default port-forward $POD_NAME 3000`

# If the domain is denied then use the command below to forward the targeted pot to pot 80
`kubectl port-forward service/my-grafana 3000:80 -n default`

# 3. Login with the password from step 1 and the username: 
* admin

# After running these commands, you can visit * http://localhost:3000 in your web browser to access the Grafana dashboard and log in using the provided username and password.


`minikube stop`
`minikube start` 
`minikube service amc-lab -n ejaka`
# to check if the KMS Tools is running and port forwarding
`kubectl get svc -n kubernetes-monitoring`
`kubectl get svc -n kubernetes-monitoring | grep kube-state-metrics`
`kubectl port-forward svc/monitoring-kube-state-metrics -n kubernetes-monitoring 8080`
#
`kubectl get svc -n kubernetes-monitoring`
`kubectl port-forward svc/YOUR_PROMETHEUS_SERVICE_NAME -n kubernetes-monitoring 9090`


# GRAFANA DASHBOARD
`kubectl get secret -n kubernetes-monitoring monitoring-grafana -o yaml`
# DECODE ADMIN-USER
`echo 'YWRtaW4=' | base64 --decode`
# DECODE PASSWORD 
`echo 'cHJvbS1vcGVyYXRvcg==' | base64 --decode`


* These are the default credentials provided by the Helm chart for Grafana
* Username: admin
* Password: prom-operator
  
  `kubectl get svc -n kubernetes-monitoring`

  `kubectl port-forward svc/monitoring-grafana -n kubernetes-monitoring 3001:80`
  `kubectl port-forward svc/prometheus-operated -n kubernetes-monitoring 9090`
  


# Check Prometheus Service:

`kubectl get services -n default`

# Check Prometheus Deployment:

* Verify that the Prometheus deployment is running:

`kubectl get deployments -n default`

# Check Prometheus Pod Logs:

* Examine the logs of the Prometheus pod to see if there are any errors:

`kubectl logs <prometheus-pod-name> -n default`





