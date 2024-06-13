FROM node:20.11-alpine As builder

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build-prod

FROM nginx:1.27-alpine

RUN rm /etc/nginx/conf.d/*

COPY docker/nginx-default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /usr/src/app/dist/another-webapp-example/browser /usr/share/nginx/html
