<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_poc_python_multi_env_version import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.feedback.create(value=[
    "good",
], trace_id="67HTZ65Z9W91HSF51CW68KK1QH", property2="rating")

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
    s = Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    )
    res = await s.feedback.create_async(value=[
        "good",
    ], trace_id="67HTZ65Z9W91HSF51CW68KK1QH", property2="rating")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->