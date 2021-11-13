# Documentation
## Deployment

![Alt text](/images/6.png?raw=true "File distribution")

I have decided to use docker with docker-compose. Of course you need to have docker and docker-compose installed. You just need to execute:
```sh
docker-compose up -d
```
I have opted for a microservices architecture because it is much faster, which is one of its great advantages.

![Alt text](/images/1.png?raw=true "Deploy command")


#### ***Alternatives***
I could have opted for **kubernetes** if I had gone with the microservices approach with an yaml file and the command:
```sh
kubectl apply -f myfile.yaml
```
The problem with kubernetes is that we would have to create the docker images before, then it would not be just a command

In monolithic architecture, I think I could have chosen to deploy by creating a playbook with ***ansible*** but it would be more tedious.



### API REST

I opted for ***flask*** simply because it was a tool I already had some knowledge of.

![Alt text](/images/2.png?raw=true "Flask code")

The first thing to do is to create a python file where we define the path where we are going to raise the service, in this case in /helloworld and with the GET method. The following is the response of the 200 code and then enable the application to receive https traffic.

To deploy this easily we need a dependency that we have in the requirements.txt file and that when we build the image we have to execute with pip along with the commands to raise the server to listen on port 8000 and all egress traffic on 0.0.0.0.0.

![Alt text](/images/3.png?raw=true "Flask Dockerfile")

#### ***Alternatives***

I could have used in a simple way with python ***Django*** or for example something that if I would have had more time is to raise it with ***Go***, a language that I would like to learn in depth.



### PROXY

In this case I have chosen nginx as the reverse proxy because I have worked with it in the past.
In the dockerfile we simply install the latest nginx image and copy the configuration file into it

![Alt text](/images/4.png?raw=true "Nginx Dockerfile")

As for the configuration file, it has more things. In this case we can differentiate the listening part of port 80 and 443. In each of them we make a proxy_pass to our backend application, in the case of https we need the certificates. A commonly used self-signed certificate option is ***certbot*** with letsencrypt.

![Alt text](/images/5.png?raw=true "Nginx conf file")

#### ***Alternatives***

I could have used apache or very light reverse proxies such as ***caddy***

-------

## Scaling

When scaling the application, it is necessary to differentiate between vertical and horizontal scaling. Of course, kubernetes/docker swarm options are better here.

### Vertical scaling

To scale the application vertically in this case you would simply have to increase in the docker-compose its memory or its cpu so that it does not take default values. Of course you could migrate to a host with better performance.

### Horizontal scaling

To scale the application horizontally in this case by being behind a proxy would simply add containers with the application and configure them in the nginx conf. We need to configure nginx as a balancer too.

----

## Logging

For the logging part we can locate the container and execute the following command:

```sh
docker logs -f <container name/id>
```

If we want something more sophisticated we could centralize the logs with tools such as loki or the elk stack.

----

## Observability

For the observability we could apply prometheus stack or/and elk stack. Regarding the question, in my opinion the most important metrics are all those concerning the application and its service and the environment where it has been deployed, for example the metrics of the number of requests to the api (maybe an api gateway like Kong would be good). On the other hand, I think that all the information we can get can help us.

----

## Monitoring

To monitor the application I would use prometheus to collect the metrics, cadvisor to expose the metrics of the docker server and its containers to prometheus, and alertmanager for alerts. To visualize the alerts I would use Grafana and create/modify panels. This is what I would do because I have some background with prometheus stack but I wouldn't mind learning ELK stack.