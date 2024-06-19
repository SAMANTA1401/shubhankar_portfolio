FROM ubuntu

WORKDIR /app

COPY requirements.txt /app

COPY authapp /app
COPY media /app
COPY myportfolio /app
COPY portfolio /app

COPY staticfiles /app
COPY templates /app
COPY manage.py /app

RUN apt-get update 
RUN apt-get install -y python3 python3-pip 
RUN pip install -r requirements.txt  

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]