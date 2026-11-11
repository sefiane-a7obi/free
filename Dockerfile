FROM python:3.11-slim

# Install official Microsoft .NET 9 Runtime for Linux
COPY --from=mcr.microsoft.com/dotnet/runtime:9.0 /usr/share/dotnet /usr/share/dotnet
ENV DOTNET_ROOT=/usr/share/dotnet
ENV PATH=$PATH:/usr/share/dotnet

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]
