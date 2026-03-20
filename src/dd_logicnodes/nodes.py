from comfy.comfy_types.node_typing import IO
from comfy_api.latest import io


anything = io.Custom(IO.ANY)
Getters = "DD Logic Nodes/Getters"
LogicGates = "DD Logic Nodes/Logic Gates"


# Getters
class IfAnyGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDIfAnyGet",
            display_name="DD If Any Getter",
            category=Getters,
            inputs=[
                anything.Input("ANY"),
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, ANY=None, on_true=None, on_false=None):
        if ANY and on_true is None:
            return ["on_true"]
        if not ANY and on_false is None:
            return ["on_false"]

    @classmethod
    def execute(cls, ANY, on_true, on_false) -> io.NodeOutput:
        return io.NodeOutput(on_true if ANY else on_false)


class OrGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDOrGetter",
            display_name="DD Or Getter",
            category=Getters,
            inputs=[
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
                io.Boolean.Input("BOOLEAN", default=True),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression=True):
        if expression and on_true is None:
            return ["on_true"]
        if not expression and on_false is None:
            return ["on_false"]

    @classmethod
    def execute(cls, on_true, on_false, expression) -> io.NodeOutput:
        return io.NodeOutput(on_true if expression else on_false)


class AndGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDAndGetter",
            display_name="DD And Getter",
            category=Getters,
            inputs=[
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=True),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression1=True, expression2=True):
        if (expression1 and expression2) and on_true is None:
            return ["on_true"]
        if not (expression1 and expression2) and on_false is None:
            return ["on_false"]

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(on_true)
        else:
            return io.NodeOutput(on_false)


class XorGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDIfXorGet",
            display_name="DD XOR Getter",
            category=Getters,
            inputs=[
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression1=True, expression2=True):
        if ((expression1 and expression2) or (not expression1 and not expression2)) and on_true is None:
            return ["on_false"]
        if not ((expression1 and expression2) or (not expression1 and not expression2)) and on_false is None:
            return ["on_true"]

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(on_false)
        elif not expression1 and not expression2:
            return io.NodeOutput(on_false)
        else:
            return io.NodeOutput(on_true)


class NorGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDIfNorGet",
            display_name="DD NOR Getter",
            category=Getters,
            inputs=[
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
                io.Boolean.Input("expression1", default=False),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression1=True, expression2=True):
        if (not expression1 and not expression2) and on_true is None:
            return ["on_true"]
        if not not expression1 and not expression2 and on_false is None:
            return ["on_false"]

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool) -> io.NodeOutput:
        if not expression1 and not expression2:
            return io.NodeOutput(on_true)
        else:
            return io.NodeOutput(on_false)


class XnorGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDifXnorGet",
            display_name="DD XNOR Getter",
            category=Getters,
            inputs=[
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=True),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression1=True, expression2=True):
        if ((expression1 and expression2) or (not expression1 and not expression2)) and on_true is None:
            return ["on_true"]
        if not ((expression1 and expression2) or (not expression1 and not expression2)) and on_false is None:
            return ["on_false"]

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(on_true)
        elif not expression1 and not expression2:
            return io.NodeOutput(on_true)
        else:
            return io.NodeOutput(on_false)


class NandGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDifNandGet",
            display_name="DD NAND Getter",
            category=Getters,
            inputs=[
                anything.Input("on_true", lazy=True),
                anything.Input("on_false", lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def validate_inputs(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression1=True, expression2=True):
        if not (expression1 and expression2) and on_true is None:
            return ["on_true"]
        if (expression1 and expression2) and on_false is None:
            return ["on_false"]

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(on_false)
        else:
            return io.NodeOutput(on_true)


class IfNot(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="DDNotGate",
            display_name="DD Not Gate",
            category=LogicGates,
            inputs=[
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                anything.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, boolean) -> io.NodeOutput:
        return io.NodeOutput(not boolean)


# Logic Gates
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
                anything.Output("*"),
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
                anything.Output("*"),
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
                anything.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(False)
        elif not expression1 and not expression2:
            return io.NodeOutput(False)
        else:
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
                anything.Output("*"),
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
                anything.Output("*"),
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
                anything.Output("*"),
            ],
        )

    @classmethod
    def execute(cls, expression1: bool, expression2: bool) -> io.NodeOutput:
        if expression1 and expression2:
            return io.NodeOutput(True)
        elif not expression1 and not expression2:
            return io.NodeOutput(True)
        return io.NodeOutput(False)
