FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm i

COPY . .
RUN npm run build

# runtime stage
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80