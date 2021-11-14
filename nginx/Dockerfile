FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY certs.sh /etc/ssl/certs/certs.sh
RUN chmod +x /etc/ssl/certs/certs.sh
WORKDIR /etc/ssl/certs
RUN ["/bin/bash","/etc/ssl/certs/certs.sh"]