FROM python:3.11.0

ENV POETRY_VERSION=1.2.2

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

CMD ["python", "src/main.py"]