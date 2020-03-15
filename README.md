# Phi Suite Data.py

| **Homepage** | [https://phisuite.com][0]        |
| ------------ | -------------------------------- | 
| **GitHub**   | [https://github.com/phisuite][1] |

## Overview

This project contains the Python module to create the **Data API** server & client.  
For more details, see [Phi Suite Data][2].

## Installation

```bash
pip install phisuite.data
```

## Creating the server

```python
from phisuite import data

class EventAPIServicer(data.EventAPIServicer):
    def Publish(self, request, context):
        ...

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
data.add_EventAPIServicer_to_server(EventAPIServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
```
For more details, see [gRPC Basics - Python: Creating the server][10].

## Creating the client

```python
from phisuite import data

channel = grpc.insecure_channel('localhost:50051')

stub = data.EventAPIStub(channel)
event = stub.Publish(event)
```
For more details, see [gRPC Basics - Python: Creating the client][11].

[0]: https://phisuite.com
[1]: https://github.com/phisuite
[2]: https://github.com/phisuite/data
[10]: https://www.grpc.io/docs/tutorials/basic/python/#server
[11]: https://www.grpc.io/docs/tutorials/basic/python/#client
