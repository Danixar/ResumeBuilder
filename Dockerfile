# docker build -t resumebuilder .
# docker run --rm -it \
# 	-v /Users/evanwiegers/Downloads:/home/resumes \
# 	resumebuilder

FROM python:latest

MAINTAINER 'Evan (Evangellos) Wiegers'

RUN python3 -m pip install --upgrade pip && \
	python3 -m pip install --upgrade Pillow && \
	python3 -m pip install --upgrade reportlab && \
	python3 -m pip install --upgrade beautifulsoup4

ADD . /home/

WORKDIR /home/

CMD python Main.py
