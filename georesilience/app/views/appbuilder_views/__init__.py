from . import assets as aa
from . import analytics as an
from . import fieldwork as la

from . import charts as cha
from . import documentation as docs
from . import reporting as ra

from ... import appbuilder

appbuilder.add_link(name=" ", href="#")

# Assets

appbuilder.add_link(name="GeoAssets**", href="admin", category="Assets")
appbuilder.add_view(aa.AssetView, name="All Assets", category="Assets")
appbuilder.add_view(aa.AssetTypeView, name="Asset Types", category="Assets")
# appbuilder.add_view(aa.AssetTagsView, name="Asset Tags", category="Assets")

appbuilder.add_separator(category="Assets")
appbuilder.add_view(aa.RelationView, name="Relations", category="Assets")


# Fieldwork

appbuilder.add_view(
    la.ProcessView, name="Activities per Lifecycle", category="Fieldwork"
)
appbuilder.add_view(
    la.DetailLifecycleView, name="Lifecycle Details", category="Fieldwork"
)
appbuilder.add_view_no_menu(la.LifecycleProfileModelView)
appbuilder.add_view_no_menu(la.ActivityView)
appbuilder.add_view(
    la.CostMasterView, name="Costs per Activity per Asset", category="Fieldwork"
)
appbuilder.add_view(la.CostView, name="Costs", category="Fieldwork")

appbuilder.add_separator(category="Fieldwork")

appbuilder.add_view(ra.ReportView, name="Report on Conditions", category="Fieldwork")
appbuilder.add_view(
    ra.DetailReportingView, name="Fieldwork Details", category="Fieldwork"
)
appbuilder.add_view(ra.ConditionTypeView, name="Condition Types", category="Fieldwork")
appbuilder.add_separator(category="Fieldwork")

appbuilder.add_view_no_menu(ra.MaterialReportView)
appbuilder.add_view_no_menu(ra.ConditionView)


# Issues
appbuilder.add_link(name="Issues**", href="admin/issue/new/?url=/admin/issue/",category="Issues")
appbuilder.add_link(name="Suggestions**", href="http://Issues.cc", category="Issues")
appbuilder.add_view(ra.EventModelView, name="Events**", category="Issues")
# appbuilder.add_view(ra.EventModelView, name="Scenarios", category="Events")

# CONFIG

appbuilder.add_separator(category="Assets")
appbuilder.add_view(aa.TagView, name="Tags", category="Assets")
appbuilder.add_view(aa.StandardTagView, name="Standard Tags", category="Assets")
appbuilder.add_view(aa.AllowedTagValueView, name="Allowed Tags", category="Assets")

appbuilder.add_separator(category="Security")
appbuilder.add_view(la.ActivityTypesView, name="Activity Types", category="Security")
appbuilder.add_view(la.CostTypeView, name="Cost Type", category="Security")

# DOCUMENTATION
appbuilder.add_separator(category="Security")
appbuilder.add_view(docs.FileView, name="Legislation Files", category="Security")
appbuilder.add_view(docs.ImageView, name="Images", category="Security")

appbuilder.add_link(name=" ", href="#")

appbuilder.add_link(name="Asset Stats", href="analytics/resmi-Assets.ipynb",category="Reports")
appbuilder.add_link(name="Fieldwork Stats", href="analytics/resmi-ToDo.ipynb", category="Reports")
# appbuilder.add_link(name="Fieldwork Stats**", href="analytics?", category="Reports")


appbuilder.add_link(
    "Documentation",
    href="file:///home/pomodoren/Desktop/SUTi/ResMI/docs/_build/html/intro.html",
    category_icon="fa-file-text-o",
    category="Documentation",
)

appbuilder.add_link(
    "API",
    href="file:///home/pomodoren/Desktop/SUTi/ResMI/docs/_build/html/intro.html",
    category="Documentation",
)

appbuilder.add_view_no_menu(an.AnalyticsView)

"""

from ...models import AssetType
from .charts import create_chart_view_for_asset_type, AssetsChartView
from ... import db

appbuilder.add_separator(category="Assets")

# Example of how to instantiate and register these views
for asset_type in db.session.query(AssetType).all():
    view = create_chart_view_for_asset_type(asset_type)
    appbuilder.add_view(view, f"{asset_type.name} Distribution", category="Assets")


"""