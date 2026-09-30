FROM python:3.13
WORKDIR /sandbox

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY simple_app.py .

EXPOSE 8000

CMD ["python", "simple_app.py"]
