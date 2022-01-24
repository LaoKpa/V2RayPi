# encoding: utf-8
import sys
from os import path
class V2rayDefaultPath:
    @classmethod
    def access_log(cls) -> str:
        if sys.platform == 'darwin':
            return path.expanduser('~/Library/Logs/v2ray-core/access.log')
        else:
            return '/var/log/v2ray/access.log'

    @classmethod
    def error_log(cls) -> str:
        if sys.platform == 'darwin':
            return path.expanduser('~/Library/Logs/v2ray-core/error.log')
        else:
            return '/var/log/v2ray/error.log'

    @classmethod
    def config_file(cls) -> str:
        if sys.platform == 'darwin':
            return '/usr/local/etc/v2ray/config.json'
        else:
            return '/etc/v2ray/config.json'

    @classmethod
    def asset_path(cls) -> str:
        if sys.platform == 'darwin':
            return '/usr/local/share/v2ray-core/'
        else:
            return '/usr/local/share/v2ray/'