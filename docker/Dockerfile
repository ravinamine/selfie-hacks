FROM ubuntu
RUN apt update && apt -y upgrade
RUN apt install -y vim git openssh-client g++ python3 python3-pip
RUN git config --global user.email "ravinamine@gmail.com" && git config --global user.name "ravinamine"
RUN cd /home && git clone https://github.com/ravinamine/selfie-hacks.git
WORKDIR /home/selfie-hacks
RUN git remote set-url origin git@github.com:ravinamine/selfie-hacks.git

ARG SSH_PRIVATE_KEY
RUN mkdir ~/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > ~/.ssh/id_rsa
RUN chmod 600 ~/.ssh/id_rsa
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts
#CMD ssh-keygen -q -t rsa -N '' -f /keys/id_rsa -C "ravinamine@gmail.com"
