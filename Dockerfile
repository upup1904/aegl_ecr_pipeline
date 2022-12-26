FROM python:3.10-bullseye




WORKDIR /src

COPY start-app.py /src

RUN chown -R 1000 /src

ARG GIT_COMMIT

ENV GIT_COMMIT $GIT_COMMIT

ENTRYPOINT ["python", "start-app.py"]