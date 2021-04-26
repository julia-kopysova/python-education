FROM python:3.9.4-alpine

COPY . .

RUN chmod +x /current_info.py

ENV TZ Europe/Kiev

CMD ["python", "current_info.py"]