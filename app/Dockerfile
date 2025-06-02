FROM python:3.11

WORKDIR /app

COPY main.py .

RUN pip install streamlit pandas psycopg2-binary sqlalchemy

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
