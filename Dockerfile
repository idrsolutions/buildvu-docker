FROM tomcat
RUN rm -rf /usr/local/tomcat/webapps/*; mkdir -p /usr/local/docroot/output
EXPOSE 8080
ENTRYPOINT ["sh", "./entrypoint.sh"]
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
