# syntax=docker/dockerfile:1

FROM python:3.8

# WORKDIR /app

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash myuser
USER myuser
WORKDIR /home/myuser

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY ./requirements.txt /home/myuser/requirements.txt

RUN pip3 install -r requirements.txt

COPY --chown=myuser:myuser . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]