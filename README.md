# DD-LogicNodes

A collection of Logic Nodes that I think are missing in core ComfyUI.

## Incomplete Yet Complete

This currently has 14 nodes.

### Logic

- DD If Not
  - Returns a flipped boolean.
- DD Or Gate
  - Returns __true__ if either expression is true.
- DD And Getter
  - Returns __true__ ___only___ if __both__ ezpressions are true.
- DD XOR Getter
  - Returns __true__ ___only___ if __one__ expression is true.
- DD NOR Getter
  - Returns __true__ ___only___ if __both__ ezpressions are false.
- DD NAND Getter
  - Returns __true__ except when __both__  expressions are true.
- DD XNOR Getter
  - Returns __true__ if __both__ expresions are true or if __both__ expresions are false.

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

### Logic Helpers

- DD Rerouter
  - Allows you to change where something is routed.
