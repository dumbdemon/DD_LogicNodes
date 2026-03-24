from comfy_api.latest import ComfyExtension, io
from .src.dd_logicnodes.logicGates import (
    NotGate,
    OrGate,
    AndGate,
    NorGate,
    XorGate,
    NandGate,
    XnorGate,
)
from .src.dd_logicnodes.logicGetters import (
    IfAnyGet,
    OrGet,
    AndGet,
    NorGet,
    XorGet,
    NandGet,
    XnorGet,
)
from .src.dd_logicnodes.logicHelpers import Rerouter


class DDLogicNodes(ComfyExtension):
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            IfAnyGet,
            OrGet,
            AndGet,
            NorGet,
            XorGet,
            NandGet,
            XnorGet,
            NotGate,
            OrGate,
            AndGate,
            NorGate,
            XorGate,
            NandGate,
            XnorGate,
            Rerouter,
        ]


async def comfy_entrypoint() -> ComfyExtension:
    return DDLogicNodes()
