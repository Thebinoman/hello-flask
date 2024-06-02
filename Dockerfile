FROM python:alpine3.20
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
CMD python -m app