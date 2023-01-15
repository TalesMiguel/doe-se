FROM node:14.20-slim

WORKDIR /frontend

RUN apt-get update

COPY ./package.json ./package-lock.json ./

RUN npm install

COPY . ./

RUN npm run build

ENV SHELL=/bin/bash LANG=en_US.UTF-8

COPY . ./

EXPOSE 3000
