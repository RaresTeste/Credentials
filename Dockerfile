
FROM python:3.10-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-6 \
    tk \
    libffi-dev \
    libtcl8.6 \
    libpq-dev \
    build-essential \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY pgconnection.py /app/


CMD ["xvfb-run", "python", "./pgconnection.py"]

 HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1
