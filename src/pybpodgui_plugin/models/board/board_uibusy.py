import logging

from PyQt5.QtGui import QIcon

import pybpodgui_plugin.resources as pybpod_conf
import pyforms_generic_editor.resources as pyforms_conf
from pybpodgui_plugin.models.board.board_dockwindow import BoardDockWindow

logger = logging.getLogger(__name__)


class BoardUIBusy(BoardDockWindow):
    """
    Perform operations related with UI reloading
    """

    def __init__(self, project):
        super(BoardUIBusy, self).__init__(project)

    def update_ui(self):
        """
        update ui now
        """
        if not hasattr(self, 'node'):
            return

        logger.debug('Board [{0}] status: {1}'.format(self.name, self.status))

        if self.status > BoardUIBusy.STATUS_READY:
            self.node.setIcon(0, QIcon(pyforms_conf.PLAY_SMALL_ICON))
        else:
            self.node.setIcon(0, QIcon(pybpod_conf.BOARD_SMALL_ICON))

    ##########################################################################
    ####### PROPERTIES #######################################################
    ##########################################################################

    @property
    def status(self):
        return BoardDockWindow.status.fget(self)

    @status.setter
    def status(self, value):
        BoardDockWindow.status.fset(self, value)
        self.project.update_ui()

    ##########################################################################
    ####### FUNCTIONS ########################################################
    ##########################################################################
