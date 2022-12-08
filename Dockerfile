FROM python:3.8.3-slim
RUN apt-get update \
    && pip install pymysql
# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 6000
CMD [ "flask", "run","--host","0.0.0.0","--port","6000"]