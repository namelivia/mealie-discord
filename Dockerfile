FROM python:3.10-alpine AS builder
WORKDIR /app
COPY . /app
RUN pip install -I pipenv==2022.10.25

FROM builder AS development
RUN pipenv install --dev

FROM builder AS production
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]
