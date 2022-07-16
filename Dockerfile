FROM ubuntu
RUN apt update && apt -y upgrade
RUN apt install -y vim git g++ python3 python3-pip
RUN cd /home && git clone https://github.com/ravinamine/selfie-hacks.git
WORKDIR /home/selfie-hacks
CMD ["echo", "Good luck and have fun with Selfie Hacks ii!"]
