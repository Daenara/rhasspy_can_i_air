FROM python:3.7
RUN apt-get update && apt-get install -y git python3-pip && \
	pip install rhasspy-hermes-app rhasspy-hermes

COPY main.py /
COPY config.ini /
	
WORKDIR /
ENTRYPOINT ["python", "-u", "main.py"]