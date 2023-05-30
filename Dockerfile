# Start from a base Python 3.9 image
FROM python:3.9-slim-buster

# Set a directory for the app
WORKDIR /usr/src/app

# Copy all the files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs in
EXPOSE 8000

# Define the command to start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
