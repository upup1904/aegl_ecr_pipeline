FROM python:3.10-bullseye




WORKDIR /src

COPY start-app.py /src

RUN chown -R 1000 /src

ENTRYPOINT ["python", "start-app.py"]