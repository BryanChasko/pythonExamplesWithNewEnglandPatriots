```
  +-[ patriots python examples ]----------------------------+
  |  python concepts through the 2004 new england patriots  |
  |  functions . loops . oop . regex . file i/o . testing   |
  +---------------------------------------------------------+
```

python programming concepts with a new england patriots theme. mirrors harvard cs50's
python curriculum (david malan) but uses patriots data instead of harry potter examples.
covers functions, variables, conditionals, loops, exceptions, libraries, tests,
file i/o, regular expressions, and object-oriented programming.

2004 world champion data throughout -- the greatest team ever assembled.

---

## prerequisites

```bash
# install uv if not present
curl -LsSf https://astral.sh/uv/install.sh | sh

# create venv and install deps
uv venv && uv sync

# run any file
uv run python basic_python_concepts/basic_function_tom_brady_versus_mac_jones_calculator.py

# run all tests
uv run pytest
```

---

## structure

```
basic_python_concepts/       -- functions, loops, exceptions, libraries, tests, file i/o, regex
beginner_python_concepts/    -- variables, simple i/o, hello world patterns
object_oriented_programming/ -- classes, inheritance, operator overloading
python_regex/                -- regex patterns with patriots data
datasets/                    -- 2004 patriots rosters, box scores, statlines
```

---

## topics covered

| topic | file |
|-------|------|
| functions | basic_function_tom_brady_versus_mac_jones_calculator.py |
| exceptions | basic_function_exception_logging_hello_world_input_wr_name.py |
| loops + dicts | basic_loops_dictionaries_patriots_legends.py |
| libraries | basic_packages_cowsay_what_does_the_foxboro_fox_say.py |
| file i/o | basic_example_working_with_files_players.py |
| testing | basic_test_calculator.py |
| regex | python_regex/ |
| oop | object_oriented_programming/ |
| command line args | basic_command_line_arguments_goat.py |
| statistics | libraries_2_statistics_2023_patriots_qb_shuffle.py |

---

## rust mirror

[rustExamplesWithNewEnglandPatriots](https://github.com/BryanChasko/rustExamplesWithNewEnglandPatriots) -- same
topics mapped to rust concepts (ownership, traits, iterators, pattern matching, error handling).

---

style guide: https://github.com/BryanChasko/heraldstack-mcp/blob/main/STYLE_GUIDE.md
