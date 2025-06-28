FROM python:3.13.5

LABEL NAME="User-Network-Projet" \
      VERSION="0.0.1" \
      DESC="Project to create a User Network of Online Communities & Visualize the Users and their connections."

# Set the working directory inside the Docker Image.
WORKDIR /target
COPY . /target

# Install Dependencies
RUN pip install -r requirements.txt

# Install the App
RUN pip install -e