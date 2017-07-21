FROM python:{{cookiecutter.python_version}}

COPY ./src /opt/src
WORKDIR /opt/src

RUN pip install eve

CMD python app.py