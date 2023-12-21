# RUN DOCKER, MINIKUBE START, configuration for a Kubernetes Service file & deployment file 

`docker run -p 80:80 ejakah/amc-wintersemester`

`docker ps`

`docker stop image ID`

`minikube start` 

`kubectl get svc -n ejaka (EXTERNAL IP)`

`minikube service amc-lab -n ejaka (URL LINK)`

`minikube service amc-lab -n ejaka --url  (URL LINK)`

`kubectl get pods --namespace=ejaka`

`kubecolor get pods --namespace=ejaka`

# WE DELETE ONE OF THE PODS TO DETERMINE IF ANOTHER POD WILL BE AUTOMATICALLY CREATED BASED ON AUTO-HEALING.
# NOTE, EDIT THE NAME SPACE ID YOU WISH TO DELETE e.g 

* amclab-deployment-bf6f9b6fb-b8z84 *

`kubectl delete pod amclab-deployment-bf6f9b6fb-b8z84 --namespace=ejaka`

# DELETE ALL RUNNING PODS 
`kubectl delete pods --namespace=ejaka --all`
