FROM python:3.9-slim
WORKDIR /Dataset
COPY . /Dataset
RUN pip install --no-cache-dir -r Dataset.txt
CMD ["python","Dataset.py"]