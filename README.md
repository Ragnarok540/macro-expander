# macro-expander

``macroexp.py`` is a simple Python script that can be used to
transform text files using macro rules in JSON files.

## Macro Rules Example

```json
{
    "a": "the",
    "test": "expanded"
}
```

## Input File

```
this is a test file

this
is
a
test
file
```

## Output File

```
this is the expanded file

this
is
the
expanded
file
```

# Usage

```sh
# single file
python3 macroexp.py test.txt macro_rules_a.json

# directory
python3 macroexp.py test macro_rules_a.json .txt
```
