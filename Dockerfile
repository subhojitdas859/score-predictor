#Please see README file for instructions.
FROM rockylinux/rockylinux
RUN dnf install python39 -y
RUN dnf install python39-pip

WORKDIR ../score_pred_workdir
COPY requirements.txt .
RUN pip3 install -r requirements.txt 

COPY model.py .
COPY dataset.csv .
RUN python3 model.py

COPY index.html .
COPY result.html .

COPY flaskapp.py .
EXPOSE 5000
CMD ["python3.8","flaskapp.py"]


