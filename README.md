# BuildVu Docker Image

## Build image
```
cd docker
docker build -t idrsolutions\buildvu . 
```

## Run container
### Trial Version
```
docker run -p 80:80 --env TOKEN=<YOUR TRIAL TOKEN> idrsolutions\buildvu
```
### Full Version
```
docker run -p 80:80 --env USERNAME=<YOUR USERNAME> --env PASSWORD=<YOUR PASSWORD> --env PRODUCT=<[buildvu|buildvu_html|buildvu_svg]> idrsolutions\buildvu
```
A username and password will be generated for you and printed on the console. The BuildVu API can be reached on `0.0.0.0/buildvu`. 

##[Recommended] Enabling HTTPS
For production use, we strongly recommend enabling HTTPS encryption. The container is pre-configured to switch to HTTPS
if it finds the files `server.crt` and `server.key` in the `/opt/ssl/` directory. All you need to do is mount a directory
containing your certificate and key like this:
```
docker run -p 80:80 -p 443:443 --env TOKEN=<YOUR TRIAL TOKEN> --mount "source=/path/to/ssl,target=/opt/ssl,type=bind,readonly" idrsolutions/buildvu
```

##[Optional] Define your own credentials
If you wish to set your own username and/or password for the service, you can do so by providing additional environment
variables to the container as follows:

### Trial Version
```
docker run -p 80:80 --env TOKEN=<YOUR TRIAL TOKEN> --env BUILDVU_USER=<username> --env BUILDVU_PASSWORD=<password> idrsolutions\buildvu
```
### Full Version
```
docker run -p 80:80 --env USERNAME=<YOUR USERNAME> --env PASSWORD=<YOUR PASSWORD> --env PRODUCT=<[buildvu|buildvu_html|buildvu_svg]> --env BUILDVU_USER=<username> --env BUILDVU_PASSWORD=<password> idrsolutions\buildvu
```

#### [Advanced] Adding multiple users
If you need more than one user, you can provide your own `tomcat-users.xml` file and mount it at `/usr/local/tomcat/conf/tomcat-users.xml`

## [Optional] Mount volume
If you need to access the converted files from the host machine without using the API, you can mount a directory:
```
mkdir -p /path/to/docroot/output
docker run -p 80:80 --env TOKEN=<YOUR TRIAL TOKEN> --mount "source=/path/to/docroot,target=/usr/local/docroot,type=bind" buildvu
```

