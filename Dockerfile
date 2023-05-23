FROM python:3.11

# host container och plats, alltså här där Dockerfile står iom .
ADD main.py .

# installs from the requirements
RUN pip install -r requirements.txt 
# command = CMD [] med de språk och script man vill köra när docker spinner upp
CMD ["python", "./main.py"]

