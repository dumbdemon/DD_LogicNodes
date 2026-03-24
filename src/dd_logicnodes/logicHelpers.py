from comfy_api.latest import io


Helpers = "DD Logic Nodes/Helper Nodes"


class Rerouter(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("source")
        return io.Schema(
            node_id="DDRerouter",
            display_name="DD Rerouter",
            category=Helpers,
            inputs=[
                io.MatchType.Input("source", template=template),
                io.Boolean.Input(
                    id="switch_route",
                    display_name="Switch Route",
                    default=True,
                    label_on="Route A",
                    label_off="Route B",
                ),
            ],
            outputs=[
                io.MatchType.Output(display_name="Route A", template=template),
                io.MatchType.Output(display_name="Route B", template=template),
            ],
            hidden=[io.Hidden.unique_id],
        )

    @classmethod
    def blocker(cls, value, block=False):
        from comfy_execution.graph_utils import ExecutionBlocker

        return ExecutionBlocker(None) if block else value

    @classmethod
    def execute(cls, source, switch_route) -> io.NodeOutput:
        routeA = cls.blocker(source, not switch_route)
        routeB = cls.blocker(source, switch_route)
        return io.NodeOutput(routeA, routeB)
