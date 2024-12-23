# Use Python 3.7 base image
FROM python:3.7

# Set working directory
WORKDIR /productapp

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Create database initialization script
RUN echo '#!/bin/bash\n\
# Wait for database to be ready\n\
echo "Waiting for database..."\n\
sleep 7\n\
\n\
# Initialize database if not already done\n\
if [ ! -d "/productapp/migrations" ]; then\n\
    echo "Initializing database..."\n\
    flask db init\n\
    flask db migrate -m "Initial migration"\n\
    flask db upgrade\n\
else\n\
    echo "Running database migrations..."\n\
    flask db upgrade\n\
fi\n\
\n\
# Start the application\n\
python run.py' > init-db.sh

# Make script executable
RUN chmod +x init-db.sh

# Set entrypoint to our initialization script
ENTRYPOINT ["./init-db.sh"]