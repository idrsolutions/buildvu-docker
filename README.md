# BuildVu Docker Image

## Build image
```
cd docker
docker build -t buildvu . 
```

## Run container
### Trial Version
```
docker run -p 8080:8080 --env TOKEN=<YOUR TRIAL TOKEN> buildvu
```
### Full Version
```
docker run -p 8080:8080 --env USERNAME=<YOUR USERNAME> --env PASSWORD=<YOUR PASSWORD> --env PRODUCT=<[buildvu|buildvu_html|buildvu_svg]> buildvu
```
The BuildVu API can be reached on `0.0.0.0:8080/buildvu`.

## [Optional] Mount volume
If you need to access the converted files from the host machine without using the API, you can mount a directory:
```
mkdir -p /path/to/docroot/output
docker run -p 8080:8080 --env TOKEN=<YOUR TRIAL TOKEN> --mount "source=/path/to/docroot,target=/usr/local/docroot,type=bind" buildvu
```
