import sublime
import sublime_plugin
import subprocess

class SublimePrettierCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selection = sublime.Region(0, self.view.size())
    selection_text = self.view.substr(selection)

    with open('/tmp/prettier-tmp', 'w') as fw:
      fw.write(selection_text)

    s = subprocess.Popen(["prettier", "--write", "/tmp/prettier-tmp"],
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    out, err = s.communicate()

    with open('/tmp/prettier-tmp', 'r') as fr:
      pretty_text = fr.read()

    self.view.replace(edit, selection, pretty_text)
