# A docker container to run the Arbitrary Aesop bot.

FROM ubuntu:latest
MAINTAINER Matthew Farrell <bobisphat.soisfarrell@gmail.com>

ADD /text_files/ /srv/text_files/

RUN apt-get update -qq && apt-get upgrade && \ 
apt-get install -y python 

RUN pip install tweepy

CMD /usr/bin/python /srv/text_files/aesop.py
