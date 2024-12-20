# orq-poc-python-multi-env-version

Developer-friendly & type-safe Python SDK specifically catered to leverage *orq-poc-python-multi-env-version* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=orq-poc-python-multi-env-version&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/orq/orq). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

[Dev] orq.ai API: The Orquesta API

For more information about the API: [orq.ai Documentation](https://docs.orq.ai)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Server-sent event streaming](#server-sent-event-streaming)
* [File uploads](#file-uploads)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install orq-poc-python-multi-env-version
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add orq-poc-python-multi-env-version
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.contacts.create(external_id="<id>")

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from orq_poc_python_multi_env_version import Orq
import os

async def main():
    async with Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    ) as s:
        res = await s.contacts.create_async(external_id="<id>")

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [contacts](docs/sdks/contacts/README.md)

* [create](docs/sdks/contacts/README.md#create) - Update user information

### [deployments](docs/sdks/deploymentssdk/README.md)

* [all](docs/sdks/deploymentssdk/README.md#all) - List all deployments
* [invalidate](docs/sdks/deploymentssdk/README.md#invalidate) - Invalidates cache
* [get_config](docs/sdks/deploymentssdk/README.md#get_config) - Get config
* [invoke](docs/sdks/deploymentssdk/README.md#invoke) - Invoke

#### [deployments.metrics](docs/sdks/metrics/README.md)

* [create](docs/sdks/metrics/README.md#create) - Add metrics

### [feedback](docs/sdks/feedback/README.md)

* [create](docs/sdks/feedback/README.md#create) - Submit feedback

### [files](docs/sdks/files/README.md)

* [upload](docs/sdks/files/README.md#upload) - Upload file
* [bulk_upload](docs/sdks/files/README.md#bulk_upload) - Bulk upload file


### [prompt](docs/sdks/prompt/README.md)


#### [prompt.snippets](docs/sdks/snippets/README.md)

* [find_one](docs/sdks/snippets/README.md#find_one) - Get one prompt snippet

#### [prompt.templates](docs/sdks/templates/README.md)

* [get_all](docs/sdks/templates/README.md#get_all) - Get all prompt templates

### [prompts](docs/sdks/prompts/README.md)

* [create](docs/sdks/prompts/README.md#create) - Create a new prompt
* [create_version](docs/sdks/prompts/README.md#create_version) - Create a new prompt version
* [delete](docs/sdks/prompts/README.md#delete) - Delete a prompt
* [get_one](docs/sdks/prompts/README.md#get_one) - Get one prompt
* [update](docs/sdks/prompts/README.md#update) - Update a prompt
* [duplicate](docs/sdks/prompts/README.md#duplicate) - Duplicate a prompt
* [get_all](docs/sdks/prompts/README.md#get_all) - Get all prompts

### [remoteconfig](docs/sdks/remoteconfig/README.md)

* [get_config](docs/sdks/remoteconfig/README.md#get_config) - Get Configurations

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.deployments.invoke(key="<key>")

    if res is not None:
        with res as event_stream:
            for event in event_stream:
                # handle event
                print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.files.upload()

    if res is not None:
        # handle response
        pass

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from orq.utils import BackoffStrategy, RetryConfig
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.contacts.create(external_id="<id>",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    if res is not None:
        # handle response
        pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from orq.utils import BackoffStrategy, RetryConfig
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.contacts.create(external_id="<id>")

    if res is not None:
        # handle response
        pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `all_async` method may raise the following exceptions:

| Error Type          | Status Code | Content Type     |
| ------------------- | ----------- | ---------------- |
| models.HonoAPIError | 500         | application/json |
| models.APIError     | 4XX, 5XX    | \*/\*            |

### Example

```python
from orq_poc_python_multi_env_version import Orq, models
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = None
    try:
        res = s.deployments.all()

        if res is not None:
            # handle response
            pass

    except models.HonoAPIError as e:
        # handle e.data: models.HonoAPIErrorData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    server_url="https://my.orq.ai",
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.contacts.create(external_id="<id>")

    if res is not None:
        # handle response
        pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from orq_poc_python_multi_env_version import Orq
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Orq(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from orq_poc_python_multi_env_version import Orq
from orq_poc_python_multi_env_version.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Orq(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      | Environment Variable |
| --------- | ---- | ----------- | -------------------- |
| `api_key` | http | HTTP Bearer | `ORQ_API_KEY`        |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from orq_poc_python_multi_env_version import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.contacts.create(external_id="<id>")

    if res is not None:
        # handle response
        pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from orq_poc_python_multi_env_version import Orq
import logging

logging.basicConfig(level=logging.DEBUG)
s = Orq(debug_logger=logging.getLogger("orq_poc_python_multi_env_version"))
```

You can also enable a default debug logger by setting an environment variable `ORQ_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=orq-poc-python-multi-env-version&utm_campaign=python)
