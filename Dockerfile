FROM python:3.10-bullseye




WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py /src/

RUN chown -R 1000 /src 

ARG GIT_COMMIT

ENV GIT_COMMIT $GIT_COMMIT

ARG GIT_COMMIT

ENV GIT_COMMIT $GIT_COMMIT

ENTRYPOINT ["python", "start-app.py"]