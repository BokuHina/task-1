FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY ../txt_files/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD ["uvicorn", "src.visual_shells.main:app", "--host", "0.0.0.0", "--port", "8000"]
