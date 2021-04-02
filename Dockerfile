FROM python
WORKDIR /Liverpool
COPY . .
RUN pip install -r req.txt
CMD python /Liverpool/app.py
