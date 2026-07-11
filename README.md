# Build with Ruba in Python

This package provides synchronous and asynchronous Python clients for the Ruba API. It targets Python 3.11 and newer.

## Installation

```bash
pip install ruba-sdk
```

## Synchronous client

```python
import os

from ruba import Ruba

with Ruba(access_token=os.environ["RUBA_ACCESS_TOKEN"]) as ruba:
    products = ruba.products.list(limit=10)
    for product in products.items:
        print(product.name)
```

## Asynchronous client

```python
import os

from ruba import RubaAsync

async with RubaAsync(access_token=os.environ["RUBA_ACCESS_TOKEN"]) as ruba:
    products = await ruba.products.list(limit=10)
```

The default endpoint is `https://api.getruba.com`. Pass `base_url="https://sandbox-api.getruba.com"` when working in the sandbox.

## Help and reference

Full request and response documentation lives in the [Ruba API reference](https://docs.getruba.com/api-reference/introduction). Bugs and SDK-specific requests can be reported through [GitHub Issues](https://github.com/Rubadot/ruba-python/issues).

## License

MIT
