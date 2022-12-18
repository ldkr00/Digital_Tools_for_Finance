FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "digital_tools_project.ipynb"]