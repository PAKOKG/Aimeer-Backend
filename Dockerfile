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
    poetry add --no-root

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# copy the rest of the app
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]