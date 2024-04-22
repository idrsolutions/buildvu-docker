# BuildVu Docker Image #

BuildVu is a PDF to HTML or SVG conversion tool to allow you to display documents natively in the web browser on any smartphone, tablet, PC or Mac. This docker image can be used to containerise BuildVu making it accessible via a REST API which is perfect for cloud deployments.

## Getting Started ##

In order to use the BuildVu Docker image you will need a license to access the BuildVu war file. If you have not got a license yet, you can [sign up for a free trial](https://www.idrsolutions.com/buildvu/trial-download).

Once you have the BuildVu war file, you can pull and run the docker image with the following commands:
```bash
docker pull idrsolutions/buildvu:latest
docker run -p 80:80 --mount "source=/path/to/war/buildvu-microservice.war,target=/usr/local/tomcat/webapps/ROOT.war,type=bind" idrsolutions/buildvu
```
A full tutorial with additional options can be [found here](https://support.idrsolutions.com/buildvu/tutorials/cloud/docker/deploy-buildvu-on-docker).

## Building the Image ##

To build the image from source, use the following steps.

- Clone the project from [here](https://github.com/idrsolutions/buildvu-docker)
- Navigate to the project directory in a terminal
- Run the following command  
  ```docker build -t idrsolutions/buildvu .```

## Documentation ## 

[BuildVu Cloud Documentation](https://support.idrsolutions.com/buildvu/host-a-web-service/)  
[BuildVu Docker Documentation](https://support.idrsolutions.com/buildvu/host-docker-web-service/)  
[Contact IDRsolutions](https://www.idrsolutions.com/contact-us)