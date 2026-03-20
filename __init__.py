from comfy_api.latest import ComfyExtension, io
from .src.dd_logicnodes.nodes import (
    IfAnyGet,
    OrGet,
    AndGet,
    NorGet,
    XorGet,
    NandGet,
    XnorGet,
    IfNot,
    OrGate,
    AndGate,
    NorGate,
    XorGate,
    NandGate,
    XnorGate,
)


UE_VERSION = "7.7"
__all__ = []


async def comfy_entrypoint() -> ComfyExtension:
    class DDLogicNodes(ComfyExtension):
        async def get_node_list(self) -> list[type[io.ComfyNode]]:
            return [IfAnyGet, OrGet, AndGet, NorGet, XorGet, NandGet, XnorGet, IfNot, OrGate, AndGate, NorGate, XorGate, NandGate, XnorGate]

    return DDLogicNodes()
