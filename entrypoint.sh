# !/bin/bash
if [ "$TOKEN" != "" ];
  then
    wget -O /usr/local/tomcat/webapps/buildvu-microservice.war https://files.idrsolutions.com/ed-war-test/buildvu-microservice.war?token=$TOKEN;
    catalina.sh run
  else
    echo "Token not set. Please provide a valid token to download BuildVu."
fi
