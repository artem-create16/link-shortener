FROM python:3.8

WORKDIR /usr/src/app
ADD . /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "run.py"]