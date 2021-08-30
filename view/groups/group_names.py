#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2021      Christopher Horn
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
NamesGrampsFrameGroup
"""

# ------------------------------------------------------------------------
#
# Plugin modules
#
# ------------------------------------------------------------------------
from ..frames.frame_name import NameGrampsFrame
from .group_list import GrampsFrameGroupList


# ------------------------------------------------------------------------
#
# NamesGrampsFrameGroup class
#
# ------------------------------------------------------------------------
class NamesGrampsFrameGroup(GrampsFrameGroupList):
    """
    The NamesGrampsFrameGroup class provides a container for managing
    all of the addresses a person or repository may have.
    """

    def __init__(self, grstate, groptions, obj):
        GrampsFrameGroupList.__init__(
            self, grstate, groptions, enable_drop=False
        )
        self.obj = obj
        self.obj_type = "Person"
        if not self.get_layout("tabbed"):
            self.hideable = self.get_layout("hideable")

        frame = NameGrampsFrame(
            grstate,
            groptions,
            obj,
            obj.get_primary_name(),
        )
        self.add_frame(frame)

        for name in obj.get_alternate_names():
            frame = NameGrampsFrame(grstate, groptions, obj, name)
            self.add_frame(frame)
        self.show_all()
