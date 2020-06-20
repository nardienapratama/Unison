FROM python:3.7.4
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "index.py"]