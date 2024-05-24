__all__ = ("PythonAnalyser",)

from loguru import logger

from ..analyser import Analyser
from ..analysis import Analysis
from ..container import ProjectContainer
from ..project import Project
from .functions import collect_functions
from .loops import collect_loops
from .statements import collect_statements


class PythonAnalyser(Analyser):
    def analyse(self, project: Project) -> Analysis:
        logger.debug(f"analysing Python project: {project}")
        with project.provision() as container:
            return self._analyse_container(container)

    def _analyse_container(self, container: ProjectContainer) -> Analysis:
        functions = collect_functions(container)
        statements = collect_statements(container)
        loops = collect_loops(container)
        insertions = statements.insertions()
        return Analysis(project=container.project,
                        functions=functions,
                        statements=statements,
                        insertions=insertions,
                        loops=loops)
