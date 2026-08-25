from comfy_api.latest import io  # type: ignore[import-not-found]


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

class Contains(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("obj", allowed_types=[io.String, io.Int, io.Float])
        template_autogrow = io.Autogrow.TemplatePrefix(
            input=io.MatchType.Input("check_value", template=template),
            prefix="check_value",
        )
        return io.Schema(
            node_id="DDContainsThis",
            display_name="DD Contains",
            category=LogicGates,
            inputs=[
                io.MatchType.Input("to_check", template=template),
                io.Autogrow.Input("check_what", template=template_autogrow),
                io.Boolean.Input(
                    "case_sensitive",
                    display_name="Case Sensitive",
                    default=False,
                    label_on="Sensitive",
                    label_off="Insensitive",
                ),
            ],
            outputs=[
                io.Boolean.Output("if_contains"),
            ],
        )
    
    @classmethod
    def execute(cls, to_check: ANY, check_what: io.Autogrow.Type, case_sensitive: bool) -> io.NodeOutput:
        check_this = f"{to_check}"
        for this in check_what.values():
            for_this = f"{this}"
            if case_sensitive:
                if for_this in check_this:
                    return io.NodeOutput(True)
            else:
                if for_this.casefold() in check_this.casefold():
                    return io.NodeOutput(True)
        return io.NodeOutput(False)
