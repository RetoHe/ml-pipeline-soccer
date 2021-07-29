FROM python:3.7
EXPOSE 8501
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./data /data
COPY ./app /app
#COPY ./app/pipeline.py /app/pipeline.py
RUN python3 /app/pipeline.py