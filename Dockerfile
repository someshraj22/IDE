FROM ubuntu

COPY . /IDE

EXPOSE 5000

WORKDIR /IDE/Python_IDE

RUN apt-get update

RUN apt-get install python-pip -y

RUN pip --no-cache-dir install -r requirements.txt

RUN rm /usr/local/lib/python2.7/dist-packages/flask_whooshalchemy.py

COPY flask_whooshalchemy.py /usr/local/lib/python2.7/dist-packages/


ENTRYPOINT ["python"]
CMD ["__main__.py"]

