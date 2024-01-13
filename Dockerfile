######## Lucifer #######

FROM python:3.10

WORKDIR /root/jonesroot/

COPY . /root/jonesroot/

RUN bash installer.sh

# changing workdir
WORKDIR "/root/jonesroot"

# start the bot.
CMD ["bash", "start"]
