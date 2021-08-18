# BuildVu Docker Image #

BuildVu is a PDF to HTML or SVG conversion tool to allow you to display documents natively in the web browser on any smartphone, tablet, PC or Mac. This docker image can be used to containerise BuildVU making it accessible via a REST API which is perfect for could deployments.

## Building the Image ##

To build the image from the source use the following steps.

- Clone the project from [here](https://github.com/idrsolutions/buildvu-docker)
- Navigate to the project directory in a terminal
- Run the following command  
  ```docker build -t idrsolutions/buildvu .```

## Getting Started ##

In order to use the BuildVu Docker image you will need a license to access the BuildVu war file. If you have not got a license yet, you can find a [free trial or contact us here](https://www.idrsolutions.com/buildvu/pricing).

Once you have access you can get and run the docker image with the following commands.
```bash
docker pull idrsolutions/buildvu:latest
docker run -p 80:80 --mount "source=/path/to/war/buildvu-microservice.war,target=/usr/local/tomcat/webapps/ROOT.war,type=bind" idrsolutions/buildvu
```
A full tutorial with additional options can be [found here](https://support.idrsolutions.com/buildvu/tutorials/cloud/docker/deploy-buildvu-on-docker).

## Documentation ## 

[IDRSolutions BuildVu Cloud Support Page](https://support.idrsolutions.com/buildvu/tutorials/cloud/).  
[IDRSolutions BuildVu Docker Support Page](https://support.idrsolutions.com/buildvu/tutorials/cloud/docker).