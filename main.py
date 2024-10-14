import mitmproxy
import json


import mitmproxy.http
#仅供学习

class ONE:
    def request(self,flow:mitmproxy.http.HTTPFlow):
        request = flow.request

    def response(self,flow):
        response = flow.response
        request = flow.request
        if "https://xyks.yuanfudao.com/leo-math/android/exams?" in request.url:
            data = response.json()

            for i in data["questions"]:
                i["answer"]="1"
                i["answers"]=["1"]

            response.set_text(json.dumps(data))

addons = [ ONE() ]