# DD-LogicNodes

A collection of Logic Nodes that I think are missing in core ComfyUI.

## Incomplete Yet Complete

This currently has 18 nodes.

### Logic

- DD If Not
  - Returns a flipped boolean.
- DD Or Gate
  - Returns __true__ if either expression is true.
- DD And Gate
  - Returns __true__ ___only___ if __both__ ezpressions are true.
- DD XOR Gate
  - Returns __true__ ___only___ if __one__ expression is true.
- DD NOR Gate
  - Returns __true__ ___only___ if __both__ ezpressions are false.
- DD NAND Gate
  - Returns __true__ except when __both__  expressions are true.
- DD XNOR Gate
  - Returns __true__ if __both__ expresions are true or if __both__ expresions are false.
- DD Contains
  - Returns __true__ if any of the source has any of the attached items (Strings, Ints, of Floats).

### Logical Getters

- DD If Any Getter
  - Returns `on_true` if any value is passed through.
- DD Or Getter
  - Returns `on_true` if the expression is true.
- DD And Getter
  - Returns `on_true` ___only___ if __both__ ezpressions are true.
- DD XOR Getter
  - Returns `on_true` ___only___ if __one__ expression is true.
- DD NOR Getter
  - Returns `on_true` ___only___ if __both__ ezpressions are false.
- DD NAND Getter
  - Returns `on_true` except when __both__  expressions are true.
- DD XNOR Getter
  - Returns `on_true` if __both__ expresions are true or if __both__ expresions are false.
- DD Either
  - Returns `if_any` if it has an input; otherwise, it returns `ANY`.
- DD Either Chioce
  - Returns `on_true` if ___true___.

### Logic Helpers

- DD Rerouter
  - Allows you to change where something is routed.
