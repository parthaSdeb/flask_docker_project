# Docker Multi-Container Project (Python, flask, nginx, mysql)

*This is a docker multi-container project, created mainly for the pupose of learning docker properly. The docker project is consist of thre container app-service(flask app), db(mysql-db), web_proxy(nginx). Here we are using web_proxy(nginx) as a proxy server. app-service and db container is connected to eache other.*

**Commands to run the project**

> docker-compose build --no-cache && docker-compose up

> docker-compose ps

> docker-compose down

*After starting the containers, go to your web browser and type __http://localhost:80__ to check.*

