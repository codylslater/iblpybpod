import pyforms_generic_editor.settings as conf
from pyforms_generic_editor.models.projects.projects_dockwindow import ProjectsDockWindow as GenericProjects

Projects = type(
    'Projects',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.projects.Projects') + [GenericProjects]),
    {}
)
