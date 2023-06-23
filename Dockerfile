FROM python:3.8.10
COPY ./ /app/
WORKDIR /app/

RUN pip install -r requirements.txt

#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
