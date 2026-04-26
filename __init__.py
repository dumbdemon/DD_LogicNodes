from comfy_api.latest import ComfyExtension, io  # type: ignore[import-not-found]
from .src.dd_logicnodes.logicGates import (  # zuban: ignore[misc]
    NotGate,
    OrGate,
    AndGate,
    NorGate,
    XorGate,
    NandGate,
    XnorGate,
)
from .src.dd_logicnodes.logicGetters import (  # zuban: ignore[misc]
    IfAnyGet,
    OrGet,
    AndGet,
    NorGet,
    XorGet,
    NandGet,
    XnorGet,
    IfEither,
    ChangeSource,
)
from .src.dd_logicnodes.logicHelpers import Rerouter  # zuban: ignore[misc]


class DDLogicNodes(ComfyExtension):
    @staticmethod
    async def get_node_list() -> list[type[io.ComfyNode]]:
        return [
            IfAnyGet,
            OrGet,
            AndGet,
            NorGet,
            XorGet,
            NandGet,
            XnorGet,
            IfEither,
            NotGate,
            OrGate,
            AndGate,
            NorGate,
            XorGate,
            NandGate,
            XnorGate,
            Rerouter,
            ChangeSource,
        ]


async def comfy_entrypoint() -> ComfyExtension:
    return DDLogicNodes()
