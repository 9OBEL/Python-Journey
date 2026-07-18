# Pin-Extractor

A simple, efficient Python tool designed to extract "secret" numeric PINs from poems.

## How it works
The `pin_extractor` function iterates through a list of poems. For each line in a poem, it extracts the word at the index corresponding to the line number (0-indexed) and calculates its length. These lengths are concatenated to form the final PIN.

*   If a line does not have a word at the required index, the algorithm assigns a `0`.

## Example
Given a poem:
```text
There
once
was
a
dragon
