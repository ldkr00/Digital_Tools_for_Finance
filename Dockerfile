FROM jupyter/base-notebook:latest

COPY . /app

WORKDIR /app

RUN pip install --prefer-binary -r requirements.txt

CMD jupyter nbconvert --execute /app/digital_tools_project.ipynb --output-dir /app/
