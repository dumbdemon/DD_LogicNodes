# wildcard trick is taken from pythongossss's
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any_typ = AnyType("*")


class IfNot:
    CATEGORY = "DD Logic Nodes"

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"boolean": ("BOOLEAN", {"default": False})}}

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "invertBoolean"

    def invertBoolean(self, boolean: bool):
        return (not boolean,)


class IfAnyGet:
    CATEGORY = "DD Logic Nodes"

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
    RETURN_NAMES = ("?",)
    FUNCTION = "ifAnyThenGet"

    def ifAnyThenGet(self, ANY, on_true, on_false):
        return (on_true if ANY else on_false,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {"IfNot": IfNot, "IfAnyGetAorB": IfAnyGet}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {"IfNot": "DD If Not", "IfAnyGetAorB": "DD If Any"}
