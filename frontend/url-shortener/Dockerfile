# This is the Dockerfile for frontend/url-shortener/Dockerfile
# We are using multi-stage builds (https://docs.docker.com/develop/develop-images/multistage-build/)

# Stage 1 - the build process
# Builds the React app in a Node.js environment.
# syntax=docker/dockerfile:1

FROM node:20-alpine as build-deps
ENV NODE_ENV=production
WORKDIR /app

# Rather than copy the entire working directory, we only copy the package.json. 
# Takes advantage of cached Docker layers
COPY ["package.json", "package-lock.json*", "./"]

RUN ["npm", "install"]

# After installing our dependencies, we add our source code into the image.
COPY . ./

# Add anonymous Docker volume for node_modules directory to ensure this dir in container isn't overwritten 
# with local node_modules dir when local directory is mounted.
VOLUME /app/node_modules

RUN ["npm", "start"]
RUN ["npm", "run", "build"]

# Stage 2 - the production environment
# Sets up a lightweight Nginx server to serve the static files that were built in the first stage.
FROM nginx:1.21-alpine
COPY --from=build-deps /app/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
