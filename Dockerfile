FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run_pipeline.sh
CMD ["./run_pipeline.sh"]
