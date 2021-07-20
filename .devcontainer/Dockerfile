
FROM mcr.microsoft.com/vscode/devcontainers/python:3

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && apt-get -y install apt-transport-https ca-certificates \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt-get update && apt-get -y install google-cloud-sdk openjdk-11-jdk

RUN curl -sL firebase.tools | bash

ENV GOOGLE_CLOUD_PROJECT=drydentest