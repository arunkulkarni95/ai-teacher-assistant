FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port and start the server
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
