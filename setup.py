from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='doomsayer',
    description="Send out Hipchat notification when spot instance is marked for termination.",
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)

import feedparser
import markdown
import jinja2
import requests
import yaml


class Preprocessors:
    """
    Built-in context preprocessors.
    Context preprocessors are functions that receive the context used to
    render the templates, and enriches it with additional information.
    The original context is obtained by parsing ``config.yml``, and
    anything else needed just be added with context preprocessors.
    """

    @staticmethod
    def navbar_add_info(context):
        """
        Items in the main navigation bar can be direct links, or dropdowns with
        subitems. This context preprocessor adds a boolean field
        ``has_subitems`` that tells which one of them every element is. It
        also adds a ``slug`` field to be used as a CSS id.
        """
        for i, item in enumerate(context["navbar"]):
            context["navbar"][i] = dict(
                item,
                has_subitems=isinstance(item["target"], list),
                slug=(item["name"].replace(" ", "-").lower()),
            )
        return context
