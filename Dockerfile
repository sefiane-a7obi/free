FROM python:3.11-slim

# Install Wine for running the Windows-compiled SEFIANE STORE Dumper engine
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wine \
        wine64 \
        cabextract \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV WINEDEBUG=-all
ENV WINEPREFIX=/root/.wine
RUN wineboot --init || true

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]
