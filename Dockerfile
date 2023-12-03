FROM huggingface/transformers-pytorch-gpu

RUN apt-get update
RUN apt-get install curl -y
RUN curl https://ollama.ai/install.sh | sh

RUN mkdir GymNotes
WORKDIR GymNotes
COPY . .

EXPOSE 8081

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmod a+x start.sh

ENV PYTHONUNBUFFERED TRUE
