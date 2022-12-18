FROM jupyter/base-notebook:latest

COPY . /app

WORKDIR /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root", "--port=8888", "--no-browser"]
