# wildcard trick is taken from pythongossss's
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any_typ = AnyType("*")


# Getters
class IfAnyGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ANY": (any_typ,),
                "on_true": (any_typ,),
                "on_false": (any_typ,),
            }
        }

    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        if input_types["on_true"] is not input_types["on_false"]:
            return 'Typing of "on_true" and "on_false" do not match.'
        return True

    RETURN_TYPES = (any_typ,)
    FUNCTION = "ifAnyThenGet"

    def ifAnyThenGet(self, ANY: AnyType, on_true: AnyType, on_false: AnyType):
        return (on_true if ANY else on_false,)


class OrGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any_typ,),
                "on_false": (any_typ,),
                "expression": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = (any_typ,)
    FUNCTION = "orGet"

    def orGet(self, on_true: AnyType, on_false: AnyType, expression: bool):
        return (on_true if expression else on_false,)


class AndGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any_typ,),
                "on_false": (any_typ,),
                "expression1": ("BOOLEAN", {"default": True}),
                "expression2": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = (any_typ,)
    FUNCTION = "andGet"

    def andGet(self, on_true: AnyType, on_false: AnyType, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return (on_true,)
        else:
            return (on_false,)


class XorGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any_typ,),
                "on_false": (any_typ,),
                "expression1": ("BOOLEAN", {"default": True}),
                "expression2": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = (any_typ,)
    FUNCTION = "xorGet"

    def xorGet(self, on_true: AnyType, on_false: AnyType, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return (on_false,)
        elif not expression1 and not expression2:
            return (on_false,)
        else:
            return (on_true,)


class NorGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any_typ,),
                "on_false": (any_typ,),
                "expression1": ("BOOLEAN", {"default": False}),
                "expression2": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = (any_typ,)
    FUNCTION = "norGet"

    def norGet(self, on_true: AnyType, on_false: AnyType, expression1: bool, expression2: bool):
        if not expression1 and not expression2:
            return (on_true,)
        else:
            return (on_false,)


class XnorGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any_typ,),
                "on_false": (any_typ,),
                "expression1": ("BOOLEAN", {"default": True}),
                "expression2": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = (any_typ,)
    FUNCTION = "xnorGet"

    def xnorGet(self, on_true: AnyType, on_false: AnyType, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return (on_true,)
        elif not expression1 and not expression2:
            return (on_true,)
        else:
            return (on_false,)


class NandGet:
    CATEGORY = "DD Logic Nodes/Getters"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any_typ,),
                "on_false": (any_typ,),
                "expression1": ("BOOLEAN", {"default": False}),
                "expression2": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = (any_typ,)
    FUNCTION = "nandGet"

    def nandGet(self, on_true: AnyType, on_false: AnyType, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return (on_false,)
        else:
            return (on_true,)


class IfNot:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"boolean": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "invertBoolean"

    def invertBoolean(self, boolean: bool):
        return (not boolean,)


# Logic Gates
class OrGate:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"expression1": ("BOOLEAN", {"default": True}), "expression2": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "orGate"

    def orGate(self, expression1: bool, expression2: bool):
        return (expression1 or expression2,)


class AndGate:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"expression1": ("BOOLEAN", {"default": True}), "expression2": ("BOOLEAN", {"default": True})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "andGate"

    def andGate(self, expression1: bool, expression2: bool):
        return (expression1 and expression2,)


class XorGate:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"expression1": ("BOOLEAN", {"default": True}), "expression2": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "xorGate"

    def xorGate(self, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return (False,)
        elif not expression1 and not expression2:
            return (False,)
        else:
            return (True,)


class NorGate:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"expression1": ("BOOLEAN", {"default": False}), "expression2": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "norGate"

    def norGate(self, expression1: bool, expression2: bool):
        return (not expression1 and not expression2,)


class NandGate:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"expression1": ("BOOLEAN", {"default": False}), "expression2": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "nandGate"

    def nandGate(self, expression1: bool, expression2: bool):
        return (not (expression1 and expression2),)


class XnorGate:
    CATEGORY = "DD Logic Nodes/Logic Gates"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"expression1": ("BOOLEAN", {"default": False}), "expression2": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "Gate"

    def orGate(self, expression1: bool, expression2: bool):
        if expression1 and expression2:
            return (True,)
        elif not expression1 and not expression2:
            return (True,)
        return (False,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "DDIfAnyGet": IfAnyGet,
    "DDOrGetter": OrGet,
    "DDAndGetter": AndGet,
    "DDIfXorGet": XorGet,
    "DDIfNorGet": NorGet,
    "DDifNandGet": NandGet,
    "DDifXnorGet": XnorGet,
    "DDNotGate": IfNot,
    "DDOrGate": OrGate,
    "DDAndGate": AndGate,
    "DDIfXorGate": XorGate,
    "DDIfNorGate": NorGate,
    "DDifNandGate": NandGate,
    "DDifXnorGate": XnorGate,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "DDIfAnyGet": "DD If Any Getter",
    "DDOrGetter": "DD Or Getter",
    "DDAndGetter": "DD And Getter",
    "DDIfXorGet": "DD XOR Getter",
    "DDIfNorGet": "DD NOR Getter",
    "DDifNandGet": "DD NAND Getter",
    "DDifXnorGet": "DD XNOR Getter",
    "DDNotGate": "DD Not Gate",
    "DDOrGate": "DD Or Gate",
    "DDAndGate": "DD And Gate",
    "DDIfXorGate": "DD XOR Gate",
    "DDIfNorGate": "DD NOR Gate",
    "DDifNandGate": "DD NAND Gate",
    "DDifXnorGate": "DD XNOR Gate",
}
