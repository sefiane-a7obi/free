#11 17.48    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.0/4.0 MB 1.6 MB/s eta 0:00:00
#11 17.57 Downloading watchfiles-1.3.0-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (458 kB)
#11 18.01    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 458.4/458.4 kB 1.0 MB/s eta 0:00:00
#11 18.09 Downloading websockets-17.4-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (226 kB)
#11 18.29    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 226.0/226.0 kB 1.2 MB/s eta 0:00:00
#11 18.38 Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)
#11 18.48 Downloading idna-3.20-py3-none-any.whl (69 kB)
#11 18.53    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.6/69.6 kB 1.6 MB/s eta 0:00:00
#11 18.65 Installing collected packages: websockets, uvloop, typing-extensions, pyyaml, python-multipart, python-dotenv, idna, httptools, h11, click, annotated-types, annotated-doc, uvicorn, typing-inspection, pydantic-core, opentelemetry-api, anyio, watchfiles, starlette, pydantic, fastapi
#11 19.73 Successfully installed annotated-doc-0.0.6 annotated-types-0.8.0 anyio-4.16.0 click-8.5.1 fastapi-0.162.4 h11-0.16.0 httptools-0.9.0 idna-3.20 opentelemetry-api-1.45.2 pydantic-2.14.3 pydantic-core-2.50.4 python-dotenv-1.2.4 python-multipart-0.0.33 pyyaml-6.0.3 starlette-1.10.0 typing-extensions-4.16.0 typing-inspection-0.4.5 uvicorn-0.54.0 uvloop-0.23.0 watchfiles-1.3.0 websockets-17.4
#11 19.73 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#11 20.17 
#11 20.17 [notice] A new release of pip is available: 24.0 -> 26.3
#11 20.17 [notice] To update, run: pip install --upgrade pip
#11 DONE 22.1s

#12 [7/7] COPY . .
#12 DONE 0.1s

#13 exporting to image
#13 exporting layers
#13 exporting layers 4.9s done
#13 pushing layers
#13 ...

#14 exporting cache to registry
#14 sending cache export
#14 ...

#13 exporting to image
#13 pushing layers 6.0s done
#13 DONE 11.1s

#14 exporting cache to registry
#14 sending cache export 8.6s done
#14 DONE 8.6s
==> Deploying...
==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
============================================================
SEFIANE STORE IL2CPP Dumper Server running at: http://0.0.0.0:10000
============================================================
INFO:     127.0.0.1:58444 - "HEAD / HTTP/1.1" 405 Method Not Allowed
==> Your service is live 🎉
INFO:     10.28.35.39:0 - "GET / HTTP/1.1" 200 OK
==> 
==> ///////////////////////////////////////////////////////////
==> 
==> Available at your primary URL https://sefianetools.onrender.com
==> 
==> ///////////////////////////////////////////////////////////
INFO:     10.27.36.151:0 - "GET / HTTP/1.1" 200 OK
INFO:     10.27.36.151:0 - "GET /assets/index-BR2qtfQq.js HTTP/1.1" 200 OK
INFO:     10.27.36.151:0 - "GET /assets/index-DvcAW-E4.css HTTP/1.1" 200 OK
INFO:     10.27.36.151:0 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     10.28.35.39:0 - "GET /assets/index-DvcAW-E4.css HTTP/1.1" 304 Not Modified
