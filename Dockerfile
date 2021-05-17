FROM python:3

COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt

CMD [ "python", "./chao_adventure/main.py" ]