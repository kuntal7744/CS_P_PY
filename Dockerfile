From python:3.12.4
copy . /app
workdir /app
run pip install requirement.txt
CMD ["python","manage.py",8000:8000]
