FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY . .
RUN conda env create -f environment.yml

# Activate the environment, and make sure it's activated:
RUN conda activate appPDF

# The code to run when container is started:
EXPOSE 9000
ENTRYPOINT ["python3", "main.py"]