# Remoteconfig
(*remoteconfig*)

## Overview

### Available Operations

* [get_config](#get_config) - Get Configurations

## get_config

Get Configurations

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.remoteconfig.get_config()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.RemoteConfigsGetConfigRequestBody](../../models/remoteconfigsgetconfigrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.RemoteConfigsGetConfigResponseBody](../../models/remoteconfigsgetconfigresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |