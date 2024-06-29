FROM python:3.10

# Set the working directory
WORKDIR /backend

# Copy the requirements file
COPY requirements.txt .

# Install dependencies using pip with cache to improve build times
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
