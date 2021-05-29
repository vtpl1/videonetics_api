# Submit Task

## Task

Task is defined as a Selection of an application from the list of predefined [available applications](/avaliable-apps/).

## Supported Streaming media

Publicly accessible rtsp camera with either H264 or H265 streams.

*[rtsp]: Real Time Streaming Protocol

## Supported Video files
* mp4
* avi
* mkv

### Supported codecs
* H264
* H265

## Event
Event is defined as usable information produced by Videonetics Ananlytics Engine by processing the video content referenced in the [Task](#task)

## Submitting a Task

### Video file upload
Upload the video file to file storage first and then get the [file reference](#file-reference).

=== "bash"
    ``` bash
    $ curl -X POST -H "Authorization: Token {{api.token}}" 
    -H "Content-Type: multipart/form-data"     
    -F "data=@test.mp4" {{api.base}}/{{api.relative}}/vs3
    ```
=== "python"
    ``` python
    import requests
    URL = '{{api.base}}/{{api.relative}}/vs3'
    TOKEN = '{{api.token}}'
    HEADERS = {'Authorization': f'token {TOKEN}'}
    response = requests.post(URL, headers=HEADERS)
    print(response.json())
    ```

**Example response:**
``` json
{
    "items": [
        {
            "Location": "/{{api.relative}}/vs3/test.mp4"
        }
    ]
}
```

#### File reference:
``` json
"{{api.base}}/{{api.relative}}/vs3/test.mp4"
```

#### Public stream refence:
Get the publicly accessible stream from the RTSP camera.

### Post a task:

Post a task with either [file reference](#file-reference) or [public steam reference](#public-stream-refence)


=== "bash"
    ``` bash
    $ curl -X POST -H "Authorization: Token {{api.token}}"
    -H "Content-Type: application/json"    
    -H "accept: application/json"
    -d "{
    "capbilitiesType": 201,
    "source": {
        "sourceList": [
        {
            "baseUrl": "{{api.base}}/{{api.relative}}/vs3/test.mp4",
        }
        ],
    }" "{{api.base}}/{{api.relative}}/engineTasks"
    ```
    
=== "python"
    ``` python
    import requests
    URL = '{{api.base}}/{{api.relative}}/engineTasks'
    TOKEN = '{{api.token}}'
    HEADERS = {'Authorization': f'token {TOKEN}'}
    response = requests.post(URL, headers=HEADERS)
    print(response.json())
    ```

**Example response:**
``` json
{
    "created": 1622295834261,
    "etag": "fe55d40f13fd5c0750d0a9e99557335b648dfc99",
    "id": "60b242fca89ba9017b7daba3",
    "links": {
        "_self": {
            "href": "engineTasks/60b242fca89ba9017b7daba3",
            "title": "Enginetask"
        }
    },
    "status": "OK",
    "updated": 1622295834261
}
```

The response returns a
