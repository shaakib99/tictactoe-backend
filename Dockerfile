FROM python:3.12-alpine

WORKDIR /code

RUN apk update && apk add git

RUN apk update && apk add git

ARG USERNAME
ARG PASSWORD

RUN git clone https://${USERNAME}:${PASSWORD}@github.com/your_username/your_repository.git /tmp/your_repository

RUN cp -r /tmp/your_repository/* /code/

COPY . /code/
COPY ../tic-tac-toe-lib /code/__lib__/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "py", "main.py" ]