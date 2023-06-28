FROM nginx:1.21.6
WORKDIR /usr/share/nginx/html/
RUN rm /usr/share/nginx/html/index.html
COPY index.html .
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]