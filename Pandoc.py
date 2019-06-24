import os

import sublime
import sublime_plugin


# PDF_BASE_PATH = "/home/jankincai/bolean/pdf/pro_comment/"
# MD_BASE_PATH = "/home/jankincai/bolean/docs/pro_comment/"


# def run_pandoc():

#     for directory, dirs, files in os.walk(MD_BASE_PATH):
#         for file in files:
#             if ".md" in file:
#                 path = os.path.join(directory, file)

#                 pdf = file.replace(".md", ".pdf")

#                 cmd = f'pandoc {path} -o {PDF_BASE_PATH}{pdf} --latex-engine=xelatex -V mainfont="Noto Sans CJK JP"'

#                 print(cmd)
#                 os.system(cmd)

PLUGIN_NAME = "Pandoc"


class PandocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
