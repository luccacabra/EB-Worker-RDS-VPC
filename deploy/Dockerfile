FROM python:2.7

COPY job_server/requirements.txt requirements.txt

RUN pip install pip==8.1.0 --upgrade

RUN pip install -r requirements.txt

COPY job_server /job_server

WORKDIR /job_server

RUN pip install .

EXPOSE 8080

CMD ["python", "src/job_server/app.py"]