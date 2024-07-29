FROM python:3.9-slim
WORKDIR /test
COPY . /test
RUN pip install --no-cache-dir -r test.txt
CMD ["python", "-m", "unittest", "test.py"]