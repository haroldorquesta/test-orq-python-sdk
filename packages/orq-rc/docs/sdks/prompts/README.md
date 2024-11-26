# Prompts
(*prompts*)

## Overview

### Available Operations

* [create](#create) - Create a new prompt
* [delete](#delete) - Delete a prompt
* [get_one](#get_one) - Get one prompt
* [duplicate](#duplicate) - Duplicate a prompt
* [get_all](#get_all) - Get all prompts

## create

Create a new prompt

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.prompts.create()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreatePromptRequestBody](../../models/createpromptrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreatePromptResponseBody](../../models/createpromptresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a prompt

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    s.prompts.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Prompt ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_one

Get one prompt

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    s.prompts.get_one(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Prompt ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## duplicate

Duplicate a prompt

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    s.prompts.duplicate(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Prompt ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_all

Get all prompts

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.prompts.get_all()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `page`                                                                                | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `limit`                                                                               | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `request_body`                                                                        | [Optional[models.GetAllPromptsRequestBody]](../../models/getallpromptsrequestbody.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetAllPromptsResponseBody](../../models/getallpromptsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |