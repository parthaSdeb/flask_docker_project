FROM python:3.8-buster

WORKDIR /app

ENV PORT=5000

COPY ./requirements.txt ./

# RUN apt-get update && apt-get install build-essential libssl-dev libffi-dev python3-dev

RUN pip3 install -r requirements.txt

EXPOSE ${PORT}

COPY ./ ./

CMD [ "python", "src_code/app.py" ]
