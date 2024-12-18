# Use Python 3.7 base image
FROM python:3.7

# Set the working directory inside the container
WORKDIR /orderapp

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /orderapp/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /orderapp

# Check and clean up the migrations folder before running the commands
# Run Flask migrations and start the app
ENTRYPOINT ["bash", "-c", "rm -rf /orderapp/migrations && flask db init && flask db migrate && flask db upgrade && python run.py"]
