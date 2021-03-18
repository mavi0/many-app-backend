# MANY App Backend

Backend api for the many speedtest app, used to auth ID's and translate json objects to influx

## API Endpoints:

### Authenticate ID

Authenticating a given user ID with the system: ```/api/authid```

Example of a valid POST request:
```json
{
    "id": 1234
}
```

Responses:

- 200: User authenticated
- 404: User does not exist

### Push Result

Pushing a result to the system: ```/api/pushresult```

Example of a valid POST request:
```json
{
    "id": 1234,
    "ul": 12.42,
    "dl": 556.324,
    "ping": 32.4,
    "jitter": 2.559
}
```

Responses:

- 200: Result submited