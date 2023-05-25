FROM ubuntu

WORKDIR /django/app

COPY . .

RUN apt clean && apt update
RUN apt -qy install python3-pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]