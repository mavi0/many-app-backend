
FROM python:3.6-stretch

WORKDIR /many

RUN pip3 install Flask \
  coloredlogs \
  requests 

COPY . /many

EXPOSE 5000

CMD ["python3", "main.py"]