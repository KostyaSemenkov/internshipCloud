FROM python
WORKDIR /test_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
