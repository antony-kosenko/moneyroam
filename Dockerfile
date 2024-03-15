FROM python:3.11.8-alpine3.18

ENV POETRY_VERSION 1.7.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

ENTRYPOINT [ "poetry", "install"]   

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
