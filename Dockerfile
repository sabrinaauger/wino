FROM python:3.10.6
#Set the working directory in the container
WORKDIR /app
#COPY the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Copy the entire application directory into the container
COPY . /app
#Expose the port our app runs on
EXPOSE 5000
#Command to run the application
CMD ["python","app.py"]
