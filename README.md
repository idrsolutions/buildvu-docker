# BuildVu Docker Image

## Build image
```
cd docker
docker build -t idrsolutions/buildvu . 
```

## Run container
### Trial Version
```
docker run -p 80:80 --env TOKEN=<YOUR TRIAL TOKEN> idrsolutions/buildvu
```
### Full Version
```
docker run -p 80:80 --env LICENSE_USERNAME=<YOUR USERNAME> --env LICENSE_PASSWORD=<YOUR PASSWORD> --env PRODUCT=<[buildvu|buildvu_html|buildvu_svg]> idrsolutions/buildvu
```

## [Recommended] Enabling HTTPS
For production use, we strongly recommend enabling HTTPS encryption. The container is pre-configured to switch to HTTPS
if it finds an SSL certificate, private key and certificate chain in the `/opt/ssl/` directory.  All you need to do is mount a directory
containing files called `certificate.crt`, `private.key` and `ca_bundle.crt`. like this:
```
docker run -p 80:80 -p 443:443 --env TOKEN=<YOUR TRIAL TOKEN> --mount "source=/local/path/to/ssl/directory,target=/opt/ssl,type=bind,readonly" idrsolutions/buildvu
```

## [Optional] Define auth credentials
If you wish to set a username and password for the service, you can do so by providing additional environment
variables to the container as follows:

### Trial Version
```
docker run -p 80:80 --env TOKEN=<YOUR TRIAL TOKEN> --env ACCESS_USERNAME=<username> --env ACCESS_PASSWORD=<password> idrsolutions/buildvu
```
### Full Version
```
docker run -p 80:80 --env LICENSE_USERNAME=<YOUR USERNAME> --env LICENSE_PASSWORD=<YOUR PASSWORD> --env PRODUCT=<[buildvu|buildvu_html|buildvu_svg]> --env ACCESS_USERNAME=<username> --env ACCESS_PASSWORD=<password> idrsolutions/buildvu
```

#### [Advanced] Adding multiple users
If you need more than one user, you can provide your own `tomcat-users.xml` file and mount it at `/usr/local/tomcat/conf/tomcat-users.xml`

## [Optional] Mount volume
If you need to access the converted files from the host machine without using the API, you can mount a directory:
```
mkdir -p /path/to/docroot/output
docker run -p 80:80 --env TOKEN=<YOUR TRIAL TOKEN> --mount "source=/path/to/docroot,target=/usr/local/docroot,type=bind" buildvu
```

