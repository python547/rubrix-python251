# -*- coding: utf-8 -*-

"""Rubrix Init Method

Contains methods for accesing the API.
"""

import logging
import os
import re
from typing import Iterable

import datasets
import pkg_resources
from rubrix.client import RubrixClient, models
from rubrix.client.models import *

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    # package is not installed
    pass

_LOGGER = logging.getLogger(__name__)

_client: Optional[
    RubrixClient
] = None  # Client will be stored here to pass it through functions


def init(
    api_url: Optional[str] = None,
    api_key: Optional[str] = None,
    timeout: int = 60,
):
    """Client setup function.

    Calling the RubrixClient init function.
    Passing an api_url disables environment variable reading, which will provide
    default values.

    Parameters
    ----------
    api_url : str
        Address from which the API is serving. It will use the default UVICORN address as default
    api_key: str
        Authentification api key. A non-secured log will be considered the default case. Optional
    timeout : int
        Seconds to considered a connection timeout. Optional
    """

    global _client

    final_api_url = api_url or os.getenv("RUBRIX_API_URL", "http://localhost:6900")

    # Checking that the api_url does not ends in '/'
    final_api_url = re.sub(r"\/$", "", final_api_url)

    # If an api_url is passed, tokens obtained via environ vars are disabled
    if api_url is not None:
        final_key = api_key
    else:
        final_key = api_key or os.getenv("RUBRIX_API_KEY")

    _client = RubrixClient(
        api_url=final_api_url,
        api_key=final_key,
        timeout=timeout,
    )


def log(
    records: Iterable[Any],
    name: str,
    tags: Optional[Dict[str, str]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    chunk_size: int = 500,
):
    """
    Register a set of logs into Rubrix

    Parameters
    ----------
    records:
        The data records list.
    name:
        The dataset name
    tags:
        A set of tags related to dataset. Optional
    metadata:
        A set of extra info for dataset. Optional
    chunk_size:
        The default chunk size for data bulk

    """
    return _client_instance().log(
        records=records, name=name, tags=tags, metadata=metadata, chunk_size=chunk_size
    )


def _client_instance() -> RubrixClient:
    """Checks module instance client and init if not initialized"""

    global _client
    # Calling a by-default-init if it was not called before
    if _client is None:
        _LOGGER.warning(
            "Tried to log data without previous initialization."
            " An initialization by default has been performed."
        )
        init()
    return _client


def snapshots(dataset: str) -> List[models.DatasetSnapshot]:
    """
    Retrieve dataset snapshots

    Parameters
    ----------
    dataset:
        The dataset name

    Returns
    -------

    """
    return _client_instance().snapshots(dataset)


def load(
    name: str, snapshot: Optional[str] = None, task: Optional[str] = None
) -> datasets.Dataset:
    """
    Load datase/snapshot data as a huggingface dataset

    Parameters
    ----------
    name:
        The dataset name
    snapshot:
        The dataset snapshot id. Optional
    task:
        The data task to retrieve (when no snapshots provided). Optional

    Returns
    -------

        A huggingfaces dataset

    """
    return _client_instance().load(name=name, snapshot=snapshot, task=task)
