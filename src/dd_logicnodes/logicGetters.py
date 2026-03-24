from comfy.comfy_types.node_typing import IO
from comfy_api.latest import io


Getters = "DD Logic Nodes/Getters"
MISSING = object()


class IfAnyGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDIfAnyGet",
            display_name="DD If Any Getter",
            category=Getters,
            inputs=[
                io.Custom(IO.ANY).Input("ANY", optional=True),
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, ANY=None, on_true=None, on_false=None):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        return None

    @classmethod
    def execute(cls, ANY=None, on_true=None, on_false=None) -> io.NodeOutput:
        return io.NodeOutput(on_true if ANY else on_false)


class OrGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDOrGetter",
            display_name="DD Or Getter",
            category=Getters,
            inputs=[
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
                io.Boolean.Input("expression", default=True),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, on_true=None, on_false=None, expression=True):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        if expression and on_true is None:
            return ["on_true"]
        if not expression and on_false is None:
            return ["on_false"]
        return None

    @classmethod
    def execute(cls, on_true, on_false, expression) -> io.NodeOutput:
        return io.NodeOutput(on_true if expression else on_false)


class AndGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDAndGetter",
            display_name="DD And Getter",
            category=Getters,
            inputs=[
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=True),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, on_true, on_false, expression1, expression2):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        if (expression1 and expression2) and on_true is None:
            return ["on_true"]
        if not (expression1 and expression2) and on_false is None:
            return ["on_false"]
        return None

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return io.NodeOutput(on_true)
        return io.NodeOutput(on_false)


class XorGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDIfXorGet",
            display_name="DD XOR Getter",
            category=Getters,
            inputs=[
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, on_true, on_false, expression1, expression2):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        if (expression1 and expression2) and on_false is None:
            return ["on_false"]
        if (not expression1 and not expression2) and on_false is None:
            return ["on_false"]
        if (expression1 or expression2) and on_true is None:
            return ["on_true"]
        return None

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return io.NodeOutput(on_false)
        if not expression1 and not expression2:
            return io.NodeOutput(on_false)
        return io.NodeOutput(on_true)


class NorGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDIfNorGet",
            display_name="DD NOR Getter",
            category=Getters,
            inputs=[
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
                io.Boolean.Input("expression1", default=False),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, on_true, on_false, expression1, expression2):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        if (expression1 and expression2) and on_false is None:
            return ["on_false"]
        if (not expression1 and not expression2) and on_true is None:
            return ["on_true"]
        if (expression1 or expression2) and on_false is None:
            return ["on_false"]
        return None

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool):
        if not expression1 and not expression2:
            return io.NodeOutput(on_true)
        return io.NodeOutput(on_false)


class XnorGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDifXnorGet",
            display_name="DD XNOR Getter",
            category=Getters,
            inputs=[
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=True),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, on_true, on_false, expression1, expression2):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        if (expression1 and expression2) and on_true is None:
            return ["on_true"]
        if (not expression1 and not expression2) and on_true is None:
            return ["on_true"]
        if (expression1 or expression2) and on_false is None:
            return ["on_false"]
        return None

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return io.NodeOutput(on_true)
        if not expression1 and not expression2:
            return io.NodeOutput(on_true)
        return io.NodeOutput(on_false)


class NandGet(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        template = io.MatchType.Template("switch")
        return io.Schema(
            node_id="DDifNandGet",
            display_name="DD NAND Getter",
            category=Getters,
            inputs=[
                io.MatchType.Input("on_true", template=template, lazy=True),
                io.MatchType.Input("on_false", template=template, lazy=True),
                io.Boolean.Input("expression1", default=True),
                io.Boolean.Input("expression2", default=False),
            ],
            outputs=[
                io.MatchType.Output(display_name="*", template=template),
            ],
        )

    @classmethod
    def check_lazy_status(cls, on_true, on_false, expression1, expression2):
        if on_false is MISSING:
            return ["on_true"]
        if on_true is MISSING:
            return ["on_false"]
        if (expression1 and expression2) and on_false is None:
            return ["on_false"]
        if (not expression1 and not expression2) and on_true is None:
            return ["on_true"]
        if (expression1 or expression2) and on_true is None:
            return ["on_true"]
        return None

    @classmethod
    def execute(cls, on_true, on_false, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return io.NodeOutput(on_false)
        return io.NodeOutput(on_true)
