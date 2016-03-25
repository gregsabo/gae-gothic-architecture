#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(
            'A list of things which ' +
            'are not Gothic Architecture:'
        )


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
