FROM tomcat:jdk11
RUN apt-get update && apt-get install -y libreoffice unzip --no-install-recommends && apt-get clean; \
 rm -rf /usr/local/tomcat/webapps/*; \
 mkdir -p /usr/local/docroot/output;
RUN \
 mkdir noto ;\
 wget -O noto/noto.zip https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip; \
 unzip noto/noto.zip -d noto/ ; \
 mkdir -p /usr/share/fonts/opentype/noto/ ; \
 mv noto/*otf /usr/share/fonts/opentype/noto/ ; \
 chmod a+r /usr/share/fonts/opentype/noto/ ; \
 fc-cache -f -v; \
 rm -rf noto
EXPOSE 8080
ENV JAVA_OPTS='-Xms512m -Xmx1g'
ENTRYPOINT ["sh", "./entrypoint.sh"]
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
