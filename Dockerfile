FROM python:3.11-slim

# Install official Microsoft .NET 9 Runtime for Linux & libicu
COPY --from=mcr.microsoft.com/dotnet/runtime:9.0 /usr/share/dotnet /usr/share/dotnet
ENV DOTNET_ROOT=/usr/share/dotnet
ENV PATH=$PATH:/usr/share/dotnet
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1

# Low-memory GC configuration for 512MB RAM containers
ENV DOTNET_gcServer=0
ENV DOTNET_GCHeapHardLimit=0x15E00000
ENV DOTNET_GCLargeObjectHeapCompactionMode=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends libicu-dev ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]
