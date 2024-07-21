from flask_appbuilder import BaseView, expose
from flask import render_template


class AnalyticsView(BaseView):
    route_base = "/analytics"

    @expose("/<report_name>")
    def report(self, report_name):
        print("*"*10)
        print(report_name)
        print("*"*10)
        voila_url = f"http://localhost:8866/voila/render/{report_name}"
        # Render a template, passing the Voilà URL to be used in the iframe
        return self.render_template("appbuilder/voila.html", voila_url=voila_url)
