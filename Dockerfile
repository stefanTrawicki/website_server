FROM python:3.12-slim
WORKDIR /
COPY . .
RUN pip install poetry && poetry install
CMD [ "poetry", "run", "python", "-m", "app" ]