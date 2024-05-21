FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# use python3 as the default python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install poetry
RUN pip3 install poetry

# Install the dependencies
RUN poetry install

# Run the python script test.py using poetry
CMD ["poetry", "run", "python", "test.py"]
