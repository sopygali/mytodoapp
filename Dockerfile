# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10.10

WORKDIR /app

COPY requirements.txt requirements.txt
EXPOSE 8000
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload" ]
