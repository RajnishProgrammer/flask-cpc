FROM python:3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

# rest of the Dockerfile