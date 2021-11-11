FROM python:3.8.2
ADD . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
ENV FLASK_APP main.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]