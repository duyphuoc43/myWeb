FROM python:3.10.10

WORKDIR /backend

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./ ./backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8001"]