# Image from dockerhub
FROM node:lts-alpine

# Make /app as a working directory in the container
WORKDIR /app

# Upgrade APK
RUN apk update && apk upgrade
RUN apk add git

# Set env path
ENV PATH /app/node_modules/.bin:$PATH

# Copy packages 
COPY package.json .
COPY package-lock.json .

# Install packages
RUN npm install && npm cache clean --force