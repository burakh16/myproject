FROM node:lts-alpine
COPY frontend /app
WORKDIR /app

RUN npm install -g npm
RUN npm install -g @vue/cli

RUN npm install

EXPOSE 8080