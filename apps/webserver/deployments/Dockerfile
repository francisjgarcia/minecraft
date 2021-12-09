FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY app .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "app.py" ]
