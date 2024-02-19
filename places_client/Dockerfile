FROM node:18-alpine as build

WORKDIR /home

COPY package*.json ./

RUN rm -rf node_modules
RUN rm -rf build

COPY . .

RUN npm install
RUN npm run build



FROM node:18-alpine as production

ENV ORIGIN=http://places-server:8200

WORKDIR /home

COPY --from=build /home/package.json ./package.json
COPY --from=build /home/build ./build

RUN npm install --production

EXPOSE 8100

ENTRYPOINT ["npm", "run", "start"]