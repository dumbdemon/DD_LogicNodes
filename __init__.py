from comfy_api.latest import ComfyExtension, io  # type: ignore[import-not-found]
from .src.dd_logicnodes import logic_nodes


class DDLogicNodes(ComfyExtension):
    @staticmethod
    async def get_node_list() -> list[type[io.ComfyNode]]:
        return logic_nodes


async def comfy_entrypoint() -> ComfyExtension:
    return DDLogicNodes()
