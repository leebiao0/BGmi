# -*- coding: utf-8 -*-

import os
import unittest
from unittest.mock import MagicMock, patch
import sys

from unittest import mock
# from bgmi.lib.fetch import website
from bgmi.config import ARIA2_RPC_TOKEN
from bgmi.website import DATA_SOURCE_MAP
from bgmi.website.base import BaseWebsite
import bgmi.website
from bgmi.downloader.aria2_rpc import Aria2DownloadRPC
import bgmi.lib.download

from bgmi.downloader.base import BaseDownloadService


class S(BaseWebsite):

    def __contains__(self, item):
        if item == 'd':
            return True
        else:
            return False


@mock.patch('bgmi.lib.download.DOWNLOAD_DELEGATE_DICT', MagicMock(get=MagicMock(return_value=S)))
@mock.patch('bgmi.lib.download.DOWNLOAD_DELEGATE', 'd')
class Aria2cTest(unittest.TestCase):
    cls = Aria2DownloadRPC

    def test_install(self):
        pass

    def test_get_download_class(self):
        pass

    def test_download_prepare(self):
        """
        list[dict]
        dict[
        name:str, keyword you use when search
        title:str, title of episode
        episode:int, episode of bangumi
        download:str, link to download
        ]
        :param data:
        :return:
        """
        pass

    def test_save_to_bangumi_download_queue(self):
        """
        list[dict]
        dict:{
        name;str, keyword you use when search
        title:str, title of episode
        episode:int, episode of bangumi
        download:str, link to download
        }
        :param data:
        :return:
        """
        pass
