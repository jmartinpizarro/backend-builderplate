# select python version
FROM python:3.12-slim 

# then create the app/ working dir
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# port where the flask app will work
EXPOSE 5000

# executes the app
CMD ["flask", "run", "--host=0.0.0.0"]

