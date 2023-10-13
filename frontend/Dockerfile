FROM node:18.12.1-alpine3.16

RUN addgroup app && adduser -S -G app app
RUN mkdir -p /usr/src/app && chown -R app:app /usr/src/app
USER app

WORKDIR /usr/src/app

COPY --chown=app:app package*.json ./
RUN npm install

COPY --chown=app:app . .
