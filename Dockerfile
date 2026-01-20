FROM tomcat:9-jdk21
RUN apt-get update && apt-get install -y libreoffice unzip python3-pip --no-install-recommends && apt-get clean; \
 pip3 install jinja2 --break-system-packages; \
 rm -rf /usr/local/tomcat/webapps/*; \
 mkdir -p /usr/local/docroot/output;
RUN \
 mkdir noto ;\
 wget -q -O noto/noto.zip https://files.idrsolutions.com/docker/Noto-hinted.zip; \
 unzip -q noto/noto.zip -d noto/ ; \
 mkdir -p /usr/share/fonts/opentype/noto/ ; \
 mv noto/*otf /usr/share/fonts/opentype/noto/ ; \
 chmod a+r /usr/share/fonts/opentype/noto/ ; \
 fc-cache -f -v; \
 rm -rf noto
RUN ["/bin/bash", "-c", "value=`cat /usr/local/tomcat/conf/server.xml` && echo \"${value//8080/80}\" >| /usr/local/tomcat/conf/server.xml"]
EXPOSE 80
ENV JAVA_OPTS='-Xms512m -Xmx1g'
ENTRYPOINT ["python3", "-u", "./entrypoint.py"]
COPY templates/* ./templates/
COPY scripts/setenv.sh ./bin
COPY scripts/entrypoint.py .
