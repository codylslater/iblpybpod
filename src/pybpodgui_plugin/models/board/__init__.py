import pyforms_generic_editor.settings as conf

from pybpodgui_plugin.models.board.board_uibusy import BoardUIBusy

Board = type(
    'Board',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.board.Board') + [BoardUIBusy]),
    {}
)
