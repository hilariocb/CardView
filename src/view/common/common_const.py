#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2007  Donald N. Allingham
# Copyright (C) 2015-2016  Nick Hall
# Copyright (C) 2021-2022  Christopher Horn
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

"""
Common constants
"""

# ------------------------------------------------------------------------
#
# GTK Modules
#
# ------------------------------------------------------------------------
from gi.repository import Gdk

# ------------------------------------------------------------------------
#
# Gramps Modules
#
# ------------------------------------------------------------------------
from gramps.gen.const import GRAMPS_LOCALE as glocale
from gramps.gen.lib import (
    Address,
    Attribute,
    ChildRef,
    Citation,
    Event,
    EventRef,
    Family,
    LdsOrd,
    Media,
    MediaRef,
    Name,
    Note,
    Person,
    PersonRef,
    Place,
    PlaceRef,
    RepoRef,
    Repository,
    Source,
    SrcAttribute,
    Tag,
    Url,
)
from gramps.gui.ddtargets import DdTargets

# ------------------------------------------------------------------------
#
# Plugin Modules
#
# ------------------------------------------------------------------------
_ = glocale.translation.sgettext


BUTTON_PRIMARY = Gdk.BUTTON_PRIMARY
BUTTON_MIDDLE = Gdk.BUTTON_MIDDLE
BUTTON_SECONDARY = Gdk.BUTTON_SECONDARY

_RETURN = Gdk.keyval_from_name("Return")
_KP_ENTER = Gdk.keyval_from_name("KP_Enter")
_SPACE = Gdk.keyval_from_name("space")

_GENDERS = {
    Person.MALE: "\u2642",
    Person.FEMALE: "\u2640",
    Person.UNKNOWN: "\u2650",
}

_BIRTH_EQUIVALENTS = ["Baptism", "Christening"]

_DEATH_EQUIVALENTS = ["Burial", "Cremation", "Probate"]

_MARRIAGE_EQUIVALENTS = ["Marriage License", "Marriage Banns"]

_DIVORCE_EQUIVALENTS = ["Annulment"]

_CONFIDENCE = {
    Citation.CONF_VERY_LOW: _("Very Low"),
    Citation.CONF_LOW: _("Low"),
    Citation.CONF_NORMAL: _("Normal"),
    Citation.CONF_HIGH: _("High"),
    Citation.CONF_VERY_HIGH: _("Very High"),
}

CITATION_TYPES = {0: _("Direct"), 1: _("Indirect")}

CONFIDENCE_COLOR_SCHEME = {
    Citation.CONF_VERY_LOW: "very-low",
    Citation.CONF_LOW: "low",
    Citation.CONF_NORMAL: "normal",
    Citation.CONF_HIGH: "high",
    Citation.CONF_VERY_HIGH: "very-high",
}

GRAMPS_OBJECTS = [
    (Person, "Person", _("Person"), DdTargets.PERSON_LINK, "gramps-person"),
    (ChildRef, "ChildRef", _("ChildRef"), DdTargets.CHILDREF, "stock_link"),
    (Event, "Event", _("Event"), DdTargets.EVENT, "gramps-event"),
    (EventRef, "EventRef", _("EventRef"), DdTargets.EVENTREF, "gramps-event"),
    (
        Citation,
        "Citation",
        _("Citation"),
        DdTargets.CITATION_LINK,
        "gramps-citation",
    ),
    (Source, "Source", _("Source"), DdTargets.SOURCE_LINK, "gramps-source"),
    (Media, "Media", _("Media"), DdTargets.MEDIAOBJ, "gramps-media"),
    (MediaRef, "MediaRef", _("MediaRef"), DdTargets.MEDIAREF, "stock_link"),
    (Note, "Note", _("Note"), DdTargets.NOTE_LINK, "gramps-notes"),
    (Family, "Family", _("Family"), DdTargets.FAMILY_LINK, "gramps-family"),
    (
        Attribute,
        "Attribute",
        _("Attribute"),
        DdTargets.ATTRIBUTE,
        "gramps-attribute",
    ),
    (
        SrcAttribute,
        "Attribute",
        _("Attribute"),
        DdTargets.SRCATTRIBUTE,
        "gramps-attribute",
    ),
    (Name, "Name", _("Name"), DdTargets.NAME, "gramps-person-name"),
    (Url, "Url", _("Url"), DdTargets.URL, "gramps-url"),
    (
        PersonRef,
        "PersonRef",
        _("PersonRef"),
        DdTargets.PERSONREF,
        "stock_link",
    ),
    (Place, "Place", _("Place"), DdTargets.PLACE_LINK, "gramps-place"),
    (PlaceRef, "PlaceRef", _("PlaceRef"), DdTargets.PLACEREF, "stock_link"),
    (Address, "Address", _("Address"), DdTargets.ADDRESS, "gramps-address"),
    (
        Repository,
        "Repository",
        _("Repository"),
        DdTargets.REPO_LINK,
        "gramps-repository",
    ),
    (RepoRef, "RepoRef", _("RepoRef"), DdTargets.REPOREF, "stock_link"),
    (Tag, "Tag", _("Tag"), None, "gramps-tag"),
    (LdsOrd, "LdsOrd", _("LdsOrd"), None, "gramps-temple"),
]

GROUP_LABELS = {
    "address": _("Addresses"),
    "association": _("Associations"),
    "attribute": _("Attributes"),
    "child": _("Children"),
    "citation": _("Citations"),
    "event": _("Events"),
    "family": _("Families"),
    "media": _("Media Items"),
    "name": _("Nombres"),
    "note": _("Notes"),
    "todo": _("To Do Notes"),
    "research": _("Research Notes"),
    "ldsord": _("Ordenanzas"),
    "ordinance": _("Ordenanzas"),
    "parent": _("Parents"),
    "people": _("People"),
    "person": _("People"),
    "place": _("Places"),
    "enclosing": _("Enclosing Places"),
    "enclosed": _("Enclosed Places"),
    "reference": _("References"),
    "repository": _("Repositories"),
    "spouse": _("Spouses"),
    "timeline": _("Timeline"),
    "source": _("Sources"),
    "uncited": _("Uncited Events"),
    "url": _("Urls"),
    "paternal": _("Paternal Lineage"),
    "maternal": _("Maternal Lineage"),
    "stats-person": _("People"),
    "stats-family": _("Families"),
    "stats-child": _("Children"),
    "stats-association": _("Associations"),
    "stats-event": _("Events"),
    "stats-ldsordperson": _("Person Ordinances"),
    "stats-ldsordfamily": _("Family Ordinances"),
    "stats-participant": _("Participants"),
    "stats-place": _("Places"),
    "stats-media": _("Media"),
    "stats-source": _("Sources"),
    "stats-citation": _("Citations"),
    "stats-repository": _("Repositories"),
    "stats-note": _("Notas"),
    "stats-tag": _("Tags"),
    "stats-bookmark": _("Bookmarks"),
    "stats-uncited": _("Uncited Information"),
    "stats-privacy": _("Privacy"),
}

GROUP_LABELS_SINGLE = {
    "address": _("Address"),
    "association": _("Association"),
    "attribute": _("Attribute"),
    "child": _("Child"),
    "sibling": _("Sibling"),
    "citation": _("Citation"),
    "event": _("Event"),
    "family": _("Family"),
    "media": _("Media Item"),
    "name": _("Name"),
    "note": _("Note"),
    "todo": _("To Do Note"),
    "research": _("Research Note"),
    "ldsord": _("Ordinance"),
    "ordinance": _("Ordinance"),
    "parent": _("Parent"),
    "people": _("Person"),
    "person": _("Person"),
    "place": _("Place"),
    "enclosing": _("Enclosing Place"),
    "enclosed": _("Enclosed Place"),
    "reference": _("Reference"),
    "repository": _("Repository"),
    "spouse": _("Spouse"),
    "timeline": _("Timeline"),
    "source": _("Source"),
    "uncited": _("Uncited Event"),
    "url": _("Url"),
    "paternal": _("Paternal Lineage"),
    "maternal": _("Maternal Lineage"),
}


PAGE_LABELS = {
    "Person": _("Person"),
    "PersonRef": _("Person Reference"),
    "Family": _("Family"),
    "ChildRef": _("Child Reference"),
    "Event": _("Event"),
    "EventRef": _("Event Reference"),
    "Place": _("Place"),
    "PlaceRef": _("Place Reference"),
    "Note": _("Note"),
    "Media": _("Media"),
    "MediaRef": _("Media Reference"),
    "Citation": _("Citation"),
    "Source": _("Source"),
    "Repository": _("Repository"),
    "RepoRef": _("Repository Reference"),
    "Address": _("Address"),
    "Name": _("Name"),
    "Attribute": _("Attribute"),
    "LdsOrd": _("LDS Ordinance"),
    "Tag": _("Tag"),
}
