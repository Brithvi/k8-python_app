From python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
        APP_ENV=dev

WORKDIR /app

RUN useradd --system --uid 10001 appuser

COPY --chown=appuser:appuser app/app.py /app/app.py

USER 10001

EXPOSE 8080

CMD ["python", "/app/app.py"]