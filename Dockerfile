FROM python:3

COPY . .

CMD [ "python", "./chao_adventure/main.py" ]