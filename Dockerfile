FROM python:3.9
WORKDIR /workspace
COPY  requirements.txt .
RUN pip install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt
COPY . .