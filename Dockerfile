FROM ubuntu:20.04

WORKDIR /app

RUN apt update

RUN apt-get install -y tzdata
RUN echo "America/Sao_Paulo" > /etc/timezone    
RUN dpkg-reconfigure -f noninteractive tzdata

RUN apt install curl git wget python3-pip tesseract-ocr -y

COPY . .

RUN pip3 install -r requirements.txt

RUN apt install ocrmypdf -y

EXPOSE 9000

CMD ["python3", "main.py"]
