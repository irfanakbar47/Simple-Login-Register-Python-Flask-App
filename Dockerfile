FROM python:3.8.5-alpine


RUN apk add --no-cache python3-dev
RUN apk add py3-pip \
	&& pip3 install --upgrade pip
#RUN apk pip install pygame --pre

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
#CMD ["app.py"]
