FROM tomcat
RUN apt-get update && apt-get install -y libreoffice --no-install-recommends && apt-get clean; \
 rm -rf /usr/local/tomcat/webapps/*; \
 mkdir -p /usr/local/docroot/output
EXPOSE 8080
ENTRYPOINT ["sh", "./entrypoint.sh"]
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
