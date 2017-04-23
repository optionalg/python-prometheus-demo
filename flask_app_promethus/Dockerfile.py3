FROM python:3.6.1-alpine
ADD . /application
WORKDIR /application
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;
EXPOSE 5000
RUN python --version
CMD uwsgi --http :5000  --manage-script-name --mount /myapplication=flask_app:app --enable-threads --processes 5