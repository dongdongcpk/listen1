# coding=utf8
import logging

from handlers.base import BaseHandler

from replay import get_provider_list

logger = logging.getLogger('listenone.' + __name__)


class SearchHybridHandler(BaseHandler):
    def get(self):
        source = self.get_argument('source', '0')
        keywords = self.get_argument('keywords', '')
        result = dict(result=[])
        if keywords == '':
            self.write(result)

        provider_list = get_provider_list()

        index = int(source)

        track_list = []
        track_len_list = []
        for i in xrange(3):
          provider = provider_list[i]
          track_list.append(provider.search_track(keywords))
          track_len_list.append(len(track_list[i]))

        min_len = min(track_len_list)
        result_list = []
        for i in xrange(3 if min_len > 3 else min_len):
          for j in xrange(3):
            result_list.append(track_list[j][i])

        result = dict(result=result_list)
        self.write(result)
