# build stage
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# run stage (vite preview или static)
FROM node:20-alpine

WORKDIR /app

# RUN npm install -g vite

COPY --from=build /app .

