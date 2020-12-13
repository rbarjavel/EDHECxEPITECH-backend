FROM python:3.8

WORKDIR ./

COPY requirements.txt ./

RUN pip3 -V
RUN pip3 install -r requirements.txt

COPY ./program ./program

CMD ["python",  "./program/start.py"]
