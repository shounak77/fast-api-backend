# using slim for minimal setup
FROM python:3.10-slim 

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

# Install pip packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all 
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
