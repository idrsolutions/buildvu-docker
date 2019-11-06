# !/bin/bash
# TODO: Add error handling for expired/failed downloads
if [ "$TOKEN" != "" ];
  then
    wget -O /usr/local/tomcat/webapps/ROOT.war https://files.idrsolutions.com/ed-war-test/buildvu-microservice.war?token=$TOKEN;
    catalina.sh run
  else
    echo "Token not set. Please provide a valid token to download BuildVu."
fi
