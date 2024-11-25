# Evals
(*evals*)

## Overview

### Available Operations

* [delete_v2_resources_evaluators_id_](#delete_v2_resources_evaluators_id_) - Delete an eval

## delete_v2_resources_evaluators_id_

Delete an eval

### Example Usage

```python
from orq_poc_python_multi_env_version import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

s.evals.delete_v2_resources_evaluators_id_(id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.DeleteV2ResourcesEvaluatorsIDResponseBody | 404                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |