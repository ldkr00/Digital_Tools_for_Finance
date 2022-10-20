#syntax=docker/dockerfile:1

FROM python:3.8

COPY . .

RUN pip install pandas numpy matplotlib

CMD ["python", "./plot.py"]