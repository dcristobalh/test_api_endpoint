Create a new microservice , that given a GET request to the /helloworld endpoint , it returns a JSON response

{ "hello": "world" }

Infra

This microservice will have two components:

Web App
Web proxy
Web App
Write a simple HTTP application in any language that listens to the port 8000 tcp. The application only needs to answer to following request:

GET /helloworld

and it should reply: { "hello": "world" }

Giving a 200 http statuscode

$ curl http://localhost/helloworld { "hello": "world" }

Web Proxy A reverse proxy needs to handle all the requests, and send them to the backend application.
Requirements for the proxy:

Pass HTTP (port 80) requests to the backend application (port 8000) Pass HTTPS requests (port 443) to the backend application (port 8000) (OPTIONAL) In case HTTPS is implemented, redirect port 80 requests to 443. Special points how you manage tls cert generation,

We suggest to use Nginx or Apache as the proxy application, but you can use any other reverse proxy software.

Deployment
Use one command , to deploy all the required infrastructure for this app to work.

Required deliverables
zip with all your work.

It should include a README.md. Put there precise instructions , on how to use your solution. The clarity and precision of these instructions will be a key part of the test.

Production.md

Document detailing , high level steps topics to think about:

deployment . where, what ,how. tooling?
scaling . how would you handle traffic spikes? tooling , approaches etc
logging . what to log , where and how
observability . which metrics would you consider key for this product. What to do with them?
monitoring . how would you monitor this app to ensure 24/7 uptime?