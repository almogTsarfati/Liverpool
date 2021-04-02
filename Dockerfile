FROM python
COPY . /Liverpool
RUN pip install -r req.txt
CMD python /Liverpool/app.py
