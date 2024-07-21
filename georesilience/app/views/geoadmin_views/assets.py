from flask_admin.form import rules
from .myview import GeoView, NonGeoView
from ... import models
from sqlalchemy import func


class AssetTypeView(NonGeoView):
    # can_create = False
    column_list = ["id", "name", "created_by", "created_on"]
    can_delete = False
    can_edit = False

    page_size = 100


class AssetView(NonGeoView):
    # can_create = False
    can_delete = False
    can_edit = False
    column_list = ["id", "name", "type", "description"]
    column_sortable_list = ["name", "type", "description"]

    page_size = 100


class BusStopView(GeoView):

    # Define fields to be displayed in the list view
    column_list = ["stop_id", "stop_name", "stop_desc", "geometry", "children"]

    # Set the number of items per page in list view
    page_size = 100

    form_rules = (
        (
            (
                rules.HTML(
                    "<div><h3 style='text-align: center;'>On bus stops</h3></div>"
                ),
            ),
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>Geo Info</h3></div><br>"
                ),
                "geometry",
            ),
        ),
        (
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>GTFS Info</h3></div><br>"
                ),
                "stop_id",
                "stop_code",
                "stop_name",
                "stop_desc",
                "wheelchair_boarding",
            )
        ),
        (
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>Infrastructure</h3></div><br>"
                ),
                "asphalt_quality",
                "pavement_quality",
                "pavement_width",
                "sidewalk_curb_height",
                "road_type_section",
                "engineering_network",
            )
        ),
        (
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>Safety</h3></div><br>"
                ),
                "street_segment_description",
                "distance_from_nearest_intersection",
                "vertical_signage",
                "horizontal_signage",
                "minimum_curb_cab_clearance",
                "seat_from_curb_distance",
                "greening",
            )
        ),
        (
            (
                rules.HTML(
                    "<div style='background-color: #ffdcf1; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>GTFS Extra</h3></div><br>"
                ),
                "zone_id",
                "stop_url",
                "location_type",
                "stop_timezone",
                "level_id",
                "platform_code",
            )
        ),
    )


class OSMAssetView(GeoView):

    # Define fields to be displayed in the list view
    column_list = ["name", "description", "tags", "geometry"]

    """
    def __init__(self, session, asset_type_filter=None, **kwargs):
        self.asset_type_filter = asset_type_filter
        super(OSMAssetView, self).__init__(models.Asset, session, **kwargs)

    def get_query(self):
        query = super(OSMAssetView, self).get_query()
        if self.asset_type_filter:
            query = query.filter(
                models.Asset.asset_type.has(name=self.asset_type_filter)
            )
        return query

    def get_count_query(self):
        query = super(OSMAssetView, self).get_count_query()
        if self.asset_type_filter:
            query = self.session.query(func.count("*")).filter(
                models.Asset.asset_type.has(name=self.asset_type_filter)
            )
        return query
    """
    
    # Set the number of items per page in list view
    page_size = 100

    form_rules = (
        (
            (
                rules.HTML(
                    "<div><h3 style='text-align: center;'>On OSM assets</h3></div>"
                ),
            ),
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>Geo Info</h3></div><br>"
                ),
                "geometry",
            ),
        ),
        (
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>Description</h3></div><br>"
                ),
                "name",
                "description",
                "osm_id",
            )
        ),
        (
            (
                rules.HTML(
                    "<div style='background-color: #e3ffd7; border-top: 3px solid lightgrey;'><h3 style='text-align: center;'>Tags</h3></div><br>"
                ),
                "tags",
            )
        ),
    )
