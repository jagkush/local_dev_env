FROM python:3.9.5

#copy the environment requirement
COPY ./requirements.txt /requirements.txt

#set the location of code
WORKDIR /

#install python requiremnent
RUN pip install -r requirements.txt

# COPY all files from app1 folder to docker
COPY . /

ENTRYPOINT [ "python3" ]

#keep the docker container application running
CMD [ "app1.py" ]
