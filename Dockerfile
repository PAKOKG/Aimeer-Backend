# pull python base image with Poetry
FROM python:3.9

# install poetry
RUN pip install poetry

# set working directory
WORKDIR /app/

# copy poetry files
COPY pyproject.toml poetry.lock ./

# install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# modify entrypoint.sh permissions
RUN chmod +x /app/entrypoint.sh

# copy the rest of the app
COPY . /app

# run entrypoint.sh
CMD ["/app/entrypoint.sh"]