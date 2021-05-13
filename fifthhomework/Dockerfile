FROM python:3.9

RUN mkdir -p /usr/app/
WORKDIR /usr/app/

COPY . /usr/app/
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

#docker build -t web-flask .
#docker run --rm --name web -p 5000:5000 web-flask
