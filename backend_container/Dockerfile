
FROM cnstark/pytorch:2.1.0-py3.10.15-ubuntu22.04




WORKDIR /app

COPY requirements.txt .


RUN sed -i '/torch/d' requirements.txt


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000
ENV PYTHONPATH="${PYTHONPATH}:/app"


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
