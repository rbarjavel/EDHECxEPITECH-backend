FROM python:3.6

RUN mkdir /app  
WORKDIR /app 
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ADD . /app/  
RUN pip install -r requirements.txt  

EXPOSE 5000  
CMD ["python", "/app/main.py"]`
