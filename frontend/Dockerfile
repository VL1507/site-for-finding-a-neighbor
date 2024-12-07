FROM node:alpine

WORKDIR /frontend

COPY package.json package-lock.json /frontend/

RUN npm install

COPY . .

EXPOSE 3000

# CMD [ "npm", "start" ]