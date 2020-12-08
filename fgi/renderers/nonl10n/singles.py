# -*- coding: utf-8 -*-

# 
# Copyright (C) 2020 Utopic Panther
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

import os
from fgi.i18n import get, conv_doc_markdown
from fgi.seo.sitemap import openw_with_sm

context = {
    "rr": ".",
    "lang": "en",
    "get": get
}

def render(games, env, lctx, output):
    context.update(lctx)

    context["active_languages"] = "actived"
    with open(os.path.join(output, "languages.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("languages.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_languages"]

    """disable privacy policy on next builds
    context["content"] = conv_doc_markdown("privacy-policy", None)
    with open("doc/privacy-policy.md") as f:
        context["content"] = markdowner.convert(f.read())
    with open(os.path.join(output, "privacy-policy.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("simple_md.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["content"]
    """

    context["content"] = conv_doc_markdown("credits", None)
    with openw_with_sm(output, "credits.html") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("simple_md.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["content"]
