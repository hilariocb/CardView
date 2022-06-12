#
# Gramps - a GTK+/GNOME based genealogy program
#
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
NotesCardGroup
"""

# ------------------------------------------------------------------------
#
# Gramps Modules
#
# ------------------------------------------------------------------------
from gramps.gen.const import GRAMPS_LOCALE as glocale

# ------------------------------------------------------------------------
#
# Plugin Modules
#
# ------------------------------------------------------------------------
from ..common.common_utils import get_object_type
from ..cards import NoteCard
from .group_list import CardGroupList

_ = glocale.translation.sgettext


# ------------------------------------------------------------------------
#
# NotesCardGroup Class
#
# ------------------------------------------------------------------------
class NotesCardGroup(CardGroupList):
    """
    The NotesCardGroup class provides a container for managing all
    of the notes associated with an object.
    """

    def __init__(self, grstate, groptions, obj):
        CardGroupList.__init__(
            self, grstate, groptions, obj, enable_drop=False
        )
        if not self.group_base.has_notes:
            return
        if self.group_base.is_primary:
            groptions.set_backlink(
                (self.group_base.obj_type, self.group_base.obj.handle)
            )
        maximum = grstate.config.get("group.note.max-per-group")
        notes = [(self.group_base.obj_lang, x) for x in obj.note_list]
        if grstate.config.get("group.note.include-child-objects"):
            notes = self.get_child_object_notes(notes)

        notes = notes[:maximum]
        for (obj_lang, handle) in notes:
            note = self.fetch("Note", handle)
            card = NoteCard(grstate, groptions, note, reference=obj_lang)
            card.set_size_request(220, -1)
            self.add_card(card)
        self.show_all()

    def get_child_object_notes(self, notes):
        """
        Get notes from child objects.
        """
        if self.group_base.has_notes:
            for obj in self.group_base.obj.get_note_child_list():
                obj_lang = get_object_type(obj, lang=True)
                for handle in obj.note_list:
                    if handle not in notes:
                        notes.append((obj_lang, handle))
        return notes

    def save_new_object(self, handle, insert_row):
        """
        Add new note to the list.
        """
        note = self.fetch("Note", handle)
        message = " ".join(
            (
                _("Added"),
                _("Note"),
                note.gramps_id,
                _("to"),
                self.group_base.obj_lang,
                self.group_base.obj.gramps_id,
            )
        )
        self.group_base.obj.add_note(handle)
        self.group_base.commit(self.grstate, message)
