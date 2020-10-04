# Web App API

This API serves as the gateway to the backend for the desktop web UI.

## Build

1. `cd` into this directory.
2. Run `pipenv install` to generate a Python virtual environment from
the [Pipfile](Pipfile).
3. Once the virtual environment has been generated, run
`pipenv run flask run` to launch the Flask development server.

## API requests

### Read events

Send a GET request to `/api/events`. The `events` attribute in the
response's JSON corresponds to a list of event objects, each containing
the following attributes.

| Attribute | Type     | Description         |
| --------- | -------- | ------------------- |
| title     | `string` | Title               |
| start     | `string` | Start date and time |
| end       | `string` | End date and time   |
