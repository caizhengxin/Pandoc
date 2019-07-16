import os
import glob

import sublime
import sublime_plugin

PLUGIN_NAME = "Pandoc"


# output_suffix = settings.get("output_suffix", ".pdf")
# latex_engine = settings.get("latex_engine", "xelatex")
# mainfont = settings.get("mainfont", "Noto Sans CJK JP")


def Settings():
    """
    动态获取配置文件
    """

    return sublime.load_settings("Pandoc.sublime-settings")


def View():
    """
    Get current active window view
    """

    return Window().active_view()


def Window():
    """
    Window
    """

    return sublime.active_window()


def pandoc(spath, output_suffix=None):
    """
    转换函数

    :param spath: 原文件路径
    """

    settings = Settings()

    output_suffix = output_suffix or settings.get("output_suffix", ".pdf")
    latex_engine = settings.get("latex_engine", "xelatex")
    mainfont = settings.get("mainfont", "Noto Sans CJK JP")

    path, suffix = os.path.splitext(spath)
    opath = "{}{}".format(path, output_suffix)

    cmd = "pandoc {} -o {} --latex-engine={} -V mainfont='{}'".format(
        spath,
        opath,
        latex_engine,
        mainfont,
    )

    os.system(cmd)

    return cmd


def pandocs(path, input_suffix, output_suffix=None):
    """
    转换函数

    :param path: 文件路径
    :param input_suffix: 输入文件后缀格式
    :param output_suffix: 输出文件后缀格式
    """

    if os.path.isfile(path):
        pandoc(path, output_suffix)
    else:
        for path in glob.glob("{}/*{}".format(path, input_suffix)):
            pandoc(path, output_suffix)


class PandocCommand(sublime_plugin.TextCommand):
    """
    PandocCommand
    """

    def run(self, edit, paths=[], *args, **kwargs):
        """
        """

        spath = self.view.file_name()
        pandoc(spath)


class PandocToPdfCommand(sublime_plugin.WindowCommand):
    """
    Pandoc to PDF
    """

    def run(self, paths=[], *args, **kwargs):

        pandocs(paths and paths[0], ".md", ".pdf")


class PandocToHtmlCommand(sublime_plugin.WindowCommand):
    """
    Pandoc to PDF
    """

    def run(self, paths=[], *args, **kwargs):

        pandocs(paths and paths[0], ".md", ".html")
