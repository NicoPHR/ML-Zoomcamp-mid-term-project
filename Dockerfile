FROM python:3.12.12-slim

RUN pip install uv

WORKDIR /app

COPY ["pyproject.toml", "uv.lock", "./"]

RUN uv sync --no-dev --locked

COPY ["predict.py", "model_1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["uv", "run", "uvicorn", "predict:app", "--host=0.0.0.0", "--port=9696"]