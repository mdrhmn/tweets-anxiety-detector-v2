FROM node:lts-alpine

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add git

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY package-lock.json .

RUN npm install && npm cache clean --force