#!/usr/bin/env python3

import importlib
import os


# automatically import any Python files in the models/ directory
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and not file.startswith("_"):
        model_name = file[: file.find(".py")]
        importlib.import_module("pytorch_translate.models." + model_name)
