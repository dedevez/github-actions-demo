# Contains commands a user could call on the command line to assemble an image.

# Define base image
FROM python:3.12

# set working directory
WORKDIR /app

# Copy all file in directory
COPY . /app

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Expose application port
EXPOSE 5000

#Define run command
CMD ["python", "-m", "flask", "run","--host=0.0.0.0"]