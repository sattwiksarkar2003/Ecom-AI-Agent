# FROM python:3.10-slim
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["python", "app.py"]


FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Run the app
CMD ["python", "app.py"]