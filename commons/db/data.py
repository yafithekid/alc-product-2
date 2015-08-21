from django.core.urlresolvers import reverse
from django.http import HttpRequest, QueryDict
from math import ceil


class ResultWithPagination:
    def __init__(self, models, current_page, total_page, request: HttpRequest):
        self.models = models
        self.current_page = current_page
        self.total_page = total_page
        self.request = request

    def render_pagination(self):
        # TODO HIGH limit if too many pages!
        ret = "<ul class='pagination'>"
        # TODO impl
        for i in range(self.total_page):
            next_request = HttpRequest()
            next_request.path = self.request.path
            next_get = self.request.GET.copy()
            # update the page in ?page=
            try:
                next_get.pop("page")
            except KeyError:
                pass
            next_get.update({"page": i + 1})
            print(str(next_get.urlencode()))
            ret += "<li><a href='" + next_request.get_full_path() + "?" + next_get.urlencode() + "'>" + str(
                i + 1) + "</a>"
        ret += "</ul>"
        return ret


class DaoWithPagination:
    def find(self, query: dict, sort: dict, limit: int, skip: int):
        raise NotImplementedError
        # ret = []
        # for i in range(skip, skip + limit):
        #     ret.append(i)
        # return ret

    def count(self, query: dict):
        raise NotImplementedError
        # return 10

    def paginate(self, query: dict, sort: list, limit: int, request: HttpRequest):
        # current page is start from one
        current_page = (request.GET.get("page", 1))
        try:
            current_page = int(current_page)
        # defend from url tampering
        except ValueError as ve:
            current_page = 1
        current_page -= 1
        count = self.count(query)
        total_page = int(ceil(count / limit))
        skip = current_page * limit
        models = self.find(query, sort, limit, skip)
        print(models)
        return ResultWithPagination(models=models, current_page=current_page, total_page=total_page, request=request)
