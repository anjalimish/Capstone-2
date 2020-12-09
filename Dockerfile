FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y cmake \
	libxrender1 \
	libsm6 \
	libxext6 \
	build-essential
RUN pip install pandas
RUN pip install Flask
RUN pip install numpy
RUN pip install opencv-python
RUN pip install gunicorn
RUN pip install pytest
RUN pip install app
RUN pip install flask_app


COPY . /code/
