FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH=$PATH:/root/.local/bin

RUN pip install --upgrade pip setuptools

WORKDIR /app

COPY ./requirements/base.txt /app/requirements.txt

RUN ls -la /app/requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "docker/start.sh"]
