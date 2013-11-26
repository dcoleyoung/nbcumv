#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import tweepy
from tweepy import OAuthHandler
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        consumer_key="Sz6aYnB2rV34LdAoKqxXg"
        consumer_secret="J1RckuFY5eyfNcRxfGSKsoK8hOfuROnGu56oGDRE"
	
        access_token="2208251772-TtDN4d2Q51Sb7g6Kd3F1n51ZbW9Ne7NX2iCVXHK"
        access_token_secret="8sM1Uix4C6F9FcDpxstzEA0seQUD9U0ghRX5bXusWHfIG"
	
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        results = api.search(q="from:@nbc")
        for r in results:
            self.response.write(r.text)
            self.response.write("<br>")
            

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
