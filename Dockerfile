FROM python
COPY . /Liverpool
RUN pip install flask && pip install flask-sqlalchemy
CMD python /Liverpool/app.py
