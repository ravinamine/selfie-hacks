FROM ubuntu
RUN apt update && apt -y upgrade && apt-get install -y curl
RUN apt-get install build-essential -y
RUN apt install -y vim git g++ python3 python3-pip
RUN cd /home && git clone https://github.com/ravinamine/selfie-hacks.git
WORKDIR /home/selfie-hacks
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH = "/root/.cargo/bin:${PATH}"
CMD ["echo", "Good luck and have fun with Selfie Hacks ii!"]
