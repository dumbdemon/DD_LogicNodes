from comfy_api.latest import io


LogicGates = "DD Logic Nodes/Logic Gates"


class NotGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDNotGate",
            display_name="DD Not Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("boolean", default=True),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, boolean) -> io.NodeOutput:
        return io.NodeOutput(not boolean)


class OrGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDOrGate",
            display_name="DD Or Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        return io.NodeOutput(expression1 or expression2)


class AndGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDAndGate",
            display_name="DD And Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=True),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        return io.NodeOutput(expression1 and expression2)


class XorGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDIfXorGate",
            display_name="DD XOR Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(False)
        if not expression1 and not expression2:
            return io.NodeOutput(False)
        return io.NodeOutput(True)


class NorGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDIfNorGate",
            display_name="DD NOR Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=False),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        return io.NodeOutput(not expression1 and not expression2)


class NandGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDifNandGate",
            display_name="DD NAND Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        return io.NodeOutput(not (expression1 and expression2))


class XnorGate(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDifXnorGate",
            display_name="DD XNOR Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=True),
            ],
            outputs=[
                io.Boolean.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(True)
        if not expression1 and not expression2:
            return io.NodeOutput(True)
        return io.NodeOutput(False)
