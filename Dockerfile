FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev python3-distutils python3-gunicorn gunicorn build-essential git curl
COPY . /pylect
WORKDIR /pylect
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "atomic:app", "-b", "0.0.0.0:8080"]
