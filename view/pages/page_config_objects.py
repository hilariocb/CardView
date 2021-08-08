# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2001-2007  Donald N. Allingham
# Copyright (C) 2008       Raphael Ackermann
# Copyright (C) 2009-2010  Gary Burton
# Copyright (C) 2010       Benny Malengier
# Copyright (C) 2012       Doug Blank <doug.blank@gmail.com>
# Copyright (C) 2015-2016  Nick Hall
# Copyright (C) 2015       Serge Noiraud
# Copyright (C) 2021       Christopher Horn
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
Page configuration dialog functions
"""

# -------------------------------------------------------------------------
#
# Gramps Modules
#
# -------------------------------------------------------------------------
from gramps.gen.const import GRAMPS_LOCALE as glocale


# -------------------------------------------------------------------------
#
# Plugin Modules
#
# -------------------------------------------------------------------------
from ..frames.frame_const import (
    EVENT_DISPLAY_MODES,
    IMAGE_DISPLAY_MODES,
    SEX_DISPLAY_MODES,
)
from ..frames.frame_utils import ConfigReset
from .page_utils import (
    create_grid,
    add_config_reset,
    config_facts_fields,
    config_metadata_attributes,
    config_tag_fields,
)

_ = glocale.translation.sgettext


def build_person_grid(
    configdialog, grstate, space, person, extra=False
):
    """
    Builds a person options section for the configuration dialog
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    configdialog.add_combo(
        grid,
        _("Event display format"),
        1,
        "{}.{}.event-format".format(space, person),
        EVENT_DISPLAY_MODES,
    )
    configdialog.add_checkbox(
        grid,
        _("Show age at death and if selected burial"),
        1,
        "{}.{}.show-age".format(space, person),
        start=3,
    )
    configdialog.add_combo(
        grid,
        _("Sex display mode"),
        2,
        "{}.{}.sex-mode".format(space, person),
        SEX_DISPLAY_MODES,
    )
    configdialog.add_combo(
        grid,
        _("Image display mode"),
        3,
        "{}.{}.image-mode".format(space, person),
        IMAGE_DISPLAY_MODES,
    )
    config_tag_fields(configdialog, "{}.{}".format(space, person), grid, 4)
    configdialog.add_text(grid, _("Fact Display Fields"), 8, bold=True)
    config_facts_fields(configdialog, grstate, space, person, grid, 9)
    if extra:
        configdialog.add_text(
            grid, _("Extra Fact Display Fields"), 8, start=3, bold=True
        )
        config_facts_fields(
            configdialog, grstate, space, person, grid, 9, start_col=3, extra=True
        )
    configdialog.add_text(
        grid, _("Metadata Display Fields"), 8, start=5, bold=True
    )
    config_metadata_attributes(grstate, "{}.{}".format(space, person), grid, 9, start_col=5)
    return add_config_reset(configdialog, grstate, "{}.{}".format(space, person), grid)


def build_media_grid(configdialog, grstate, space):
    """
    Builds a media options section for the configuration dialog
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    config_tag_fields(configdialog, "{}.media".format(space), grid, 1)
    configdialog.add_checkbox(
        grid,
        _("Sort media by date"),
        4,
        "{}.media.sort-by-date".format(space),
        tooltip=_("Enabling this option will sort the media by date."),
    )
    configdialog.add_text(grid, _("Attributes"), 9, bold=True)
    configdialog.add_checkbox(
        grid,
        _("Show date"),
        10,
        "{}.media.show-date".format(space),
        tooltip=_(
            "Enabling this option will show the media date if it is available."
        ),
    )
    configdialog.add_text(
        grid, _("Metadata Display Fields"), 15, start=1, bold=True
    )
    config_metadata_attributes(
        grstate,
        "{}.media".format(space),
        grid,
        16,
        start_col=1,
        number=4,
        obj_selector_type="Media",
    )
    return add_config_reset(configdialog, grstate, "{}.media".format(space), grid)


def build_note_grid(configdialog, grstate, space):
    """
    Builds note options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    configdialog.add_checkbox(
        grid,
        _("Enable preview mode"),
        1,
        "{}.note.preview-mode".format(space),
        tooltip=_(
            "Indicates only a portion of the full note should be displayed."
        ),
    )
    configdialog.add_spinner(
        grid,
        _("Number of lines to preview"),
        2,
        "{}.note.preview-lines".format(space),
        (0, 8),
    )
    config_tag_fields(configdialog, "{}.note".format(space), grid, 3)
    return add_config_reset(configdialog, grstate, "{}.note".format(space), grid)


def build_citation_grid(configdialog, grstate, space):
    """
    Builds citation options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    config_tag_fields(
        configdialog, "{}.citation".format(space), grid, 1
    )
    configdialog.add_combo(
        grid,
        _("Image display mode"),
        3,
        "{}.citation.image-mode".format(space),
        IMAGE_DISPLAY_MODES,
    )
    configdialog.add_checkbox(
        grid,
        _("Sort citations by date"),
        4,
        "{}.citation.sort-by-date".format(space),
        tooltip=_("Enabling this option will sort the citations by date."),
    )
    configdialog.add_checkbox(
        grid,
        _("Include indirect citations about the person"),
        5,
        "{}.citation.include-indirect".format(space),
        tooltip=_(
            "Enabling this option will include citations on nested attributes like names and person associations in addition to the ones directly on the person themselves."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _(
            "Include citations related to the persons family membership as a child"
        ),
        6,
        "{}.citation.include-parent-family".format(space),
        tooltip=_(
            "Enabling this option will include citations related to the membership of the person as a child in other families."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _(
            "Include citations related to the persons family membership as a head of household"
        ),
        7,
        "{}.citation.include-family".format(space),
        tooltip=_(
            "Enabling this option will include citations on the families this person formed with other partners."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _(
            "Include indirect citations related to the persons family membership as a head of household"
        ),
        8,
        "{}.citation.include-family-indirect".format(space),
        tooltip=_(
            "Enabling this option will include citations on nested attributes about the families this person formed with other partners."
        ),
    )
    configdialog.add_text(grid, _("Attributes"), 9, bold=True)
    configdialog.add_checkbox(
        grid,
        _("Show date"),
        10,
        "{}.citation.show-date".format(space),
        tooltip=_(
            "Enabling this option will show the citation date if it is available."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _("Show publisher"),
        11,
        "{}.citation.show-publisher".format(space),
        tooltip=_(
            "Enabling this option will show the publisher information if it is available."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _("Show reference type"),
        12,
        "{}.citation.show-reference-type".format(space),
        tooltip=_(
            "Enabling this option will display what type of citation it is. Direct is one related to the person or a family they formed, indirect would be related to some nested attribute like a name or person association."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _("Show reference description"),
        13,
        "{}.citation.show-reference-description".format(space),
        tooltip=_(
            "Enabling this option will display a description of the type of data the citation supports. For direct citations this would be person or family, indirect ones could be primary name, an attribute, association, address, and so forth."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _("Show confidence rating"),
        14,
        "{}.citation.show-confidence".format(space),
        tooltip=_(
            "Enabling this option will display the user selected confidence level for the citation."
        ),
    )
    configdialog.add_text(
        grid, _("Metadata Display Fields"), 15, start=1, bold=True
    )
    config_metadata_attributes(
        grstate,
        "{}.citation".format(space),
        grid,
        16,
        start_col=1,
        number=4,
        obj_selector_type="Citation",
    )
    return add_config_reset(configdialog, grstate, "{}.citation".format(space), grid)


def build_source_grid(configdialog, grstate, space):
    """
    Builds source options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    configdialog.add_combo(
        grid,
        _("Event display format"),
        1,
        "{}.source.event-format".format(space),
        EVENT_DISPLAY_MODES,
    )
    configdialog.add_combo(
        grid,
        _("Image display mode"),
        3,
        "{}.source.image-mode".format(space),
        IMAGE_DISPLAY_MODES,
    )
    config_tag_fields(configdialog, "{}.source".format(space), grid, 4)
    configdialog.add_text(
        grid, _("Metadata Display Fields"), 15, start=1, bold=True
    )
    config_metadata_attributes(
        grstate, "{}.source".format(space), grid, 16, start_col=1, number=4, obj_selector_type="Source"
    )
    return add_config_reset(configdialog, grstate, "{}.source".format(space), grid)


def build_repository_grid(configdialog, grstate, space):
    """
    Builds repository options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    config_tag_fields(
        configdialog, "{}.repository".format(space), grid, 1
    )
    configdialog.add_text(grid, _("Attributes"), 9, bold=True)
    configdialog.add_checkbox(
        grid,
        _("Show call number"),
        10,
        "{}.repository.show-call-number".format(space),
        tooltip=_(
            "Enabling this option will show the source call number at the repository if it is available."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _("Show media type"),
        11,
        "{}.repository.show-media-type".format(space),
        tooltip=_(
            "Enabling this option will show the source media type at the repository if it is available."
        ),
    )
    configdialog.add_checkbox(
        grid,
        _("Show repository type"),
        12,
        "{}.repository.show-repository-type".format(space),
        tooltip=_(
            "Enabling this option will show the repository type if it is available."
        ),
    )
    return add_config_reset(configdialog, grstate, "{}.repository".format(space), grid)


def build_place_grid(configdialog, grstate, space):
    """
    Builds place options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    config_tag_fields(configdialog, "{}.place".format(space), grid, 4)
    return add_config_reset(configdialog, grstate, "{}.place".format(space), grid)


def build_event_grid(configdialog, grstate, space):
    """
    Builds event options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    configdialog.add_combo(
        grid,
        _("Event display format"),
        1,
        "{}.event.event-format".format(space),
        EVENT_DISPLAY_MODES,
    )
    configdialog.add_combo(
        grid,
        _("Image display mode"),
        3,
        "{}.event.image-mode".format(space),
        IMAGE_DISPLAY_MODES,
    )
    config_tag_fields(configdialog, "{}.event".format(space), grid, 4)
    configdialog.add_text(
        grid, _("Metadata Display Fields"), 11, start=1, bold=True
    )
    config_metadata_attributes(
        grstate, "{}.event".format(space), grid, 12, start_col=1, number=4, obj_selector_type="Event"
    )
    return add_config_reset(configdialog, grstate, "{}.event".format(space), grid)


def build_family_grid(configdialog, grstate, space):
    """
    Builds family options section for the configuration dialog.
    """
    grid = create_grid()
    configdialog.add_text(grid, _("Display Options"), 0, bold=True)
    configdialog.add_combo(
        grid,
        _("Event display format"),
        1,
        "{}.family.event-format".format(space),
        EVENT_DISPLAY_MODES,
    )
    configdialog.add_checkbox(
        grid,
        _("Show age at death and if selected burial"),
        1,
        "{}.family.show-age".format(space),
        start=3,
    )
    configdialog.add_combo(
        grid,
        _("Sex display mode"),
        2,
        "{}.family.sex-mode".format(space),
        SEX_DISPLAY_MODES,
    )
    configdialog.add_combo(
        grid,
        _("Image display mode"),
        3,
        "{}.family.image-mode".format(space),
        IMAGE_DISPLAY_MODES,
    )
    config_tag_fields(configdialog, "{}.family".format(space), grid, 4)
    configdialog.add_text(grid, _("Fact Display Fields"), 8, bold=True)
    config_facts_fields(configdialog, grstate, space, "family", grid, 9)
    configdialog.add_text(
        grid, _("Metadata Display Fields"), 8, start=5, bold=True
    )
    config_metadata_attributes(grstate, "{}.family".format(space), grid, 9, start_col=5)
    return add_config_reset(configdialog, grstate, "{}.event".format(space), grid)
