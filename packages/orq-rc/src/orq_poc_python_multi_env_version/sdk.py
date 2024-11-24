"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from orq_poc_python_multi_env_version import models, utils
from orq_poc_python_multi_env_version._hooks import SDKHooks
from orq_poc_python_multi_env_version.deployments_sdk import DeploymentsSDK
from orq_poc_python_multi_env_version.evals import Evals
from orq_poc_python_multi_env_version.evaluators import Evaluators
from orq_poc_python_multi_env_version.feedback import Feedback
from orq_poc_python_multi_env_version.files import Files
from orq_poc_python_multi_env_version.remoteconfig import Remoteconfig
from orq_poc_python_multi_env_version.types import OptionalNullable, UNSET
from typing import Any, Callable, Dict, Optional, Union


class Orq(BaseSDK):
    r"""[Dev] orq.ai API: The Orquesta API
    https://docs.orq.ai - orq.ai Documentation
    """

    feedback: Feedback
    deployments: DeploymentsSDK
    files: Files
    evaluators: Evaluators
    evals: Evals
    remoteconfig: Remoteconfig

    def __init__(
        self,
        api_key: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(api_key):
            security = lambda: models.Security(api_key=api_key())  # pylint: disable=unnecessary-lambda-assignment
        else:
            security = models.Security(api_key=api_key)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.feedback = Feedback(self.sdk_configuration)
        self.deployments = DeploymentsSDK(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.evaluators = Evaluators(self.sdk_configuration)
        self.evals = Evals(self.sdk_configuration)
        self.remoteconfig = Remoteconfig(self.sdk_configuration)
