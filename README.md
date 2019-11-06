# BuildVu Docker Image

## Build image
```shell script
cd docker
docker build -t buildvu . 
```

## Run container
```shell script
docker run -p 8080:8080 --env TOKEN=<YOUR TRIAL TOKEN> buildvu
```
The BuildVu API can be reached on `0.0.0.0:8080/buildvu-microservice/buildvu`.

## [Optional] Mount volume
If you need to access the converted files from the host machine without using the API, you can mount a directory:
```shell script
mkdir -p /path/to/docroot/output
docker run -p 8080:8080 --env TOKEN=<YOUR TRIAL TOKEN> --mount "source=/path/to/docroot,target=/usr/local/docroot,type=bind" buildvu
```
