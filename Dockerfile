FROM node:22-alpine AS frontend
WORKDIR /build
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY abverdict/ abverdict/
RUN pip install --no-cache-dir ".[server]"
COPY --from=frontend /build/dist frontend/dist
EXPOSE 8000
CMD ["uvicorn", "abverdict.api:app", "--host", "0.0.0.0", "--port", "8000"]
