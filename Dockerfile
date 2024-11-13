# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/
COPY llama-2-7b-chat.Q2_K.gguf /app/llama-2-7b-chat.Q2_K.gguf

# Install any needed packages specified in requirements.txt
RUN pip install llama-cpp-python
RUN pip install fastapi uvicorn jinja2

# Expose port 5000 to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]