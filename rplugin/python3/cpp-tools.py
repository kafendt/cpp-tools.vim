import neovim
import re

@neovim.plugin
class CPPTools(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('CPPCreateFunctionDefinitonOrDeclaration', range='', nargs='*', sync=True)
    def create_function_definiton(self, range='', nargs='*', sync=False):
        # get current line content
        line_content = self.nvim.current.line

        # check if there is a function declaration/definiton in the current line
        function_groups = re.findall("(\w+([:\w<>,\s*&]+)?)\s([\w:]+)\(((?:[\w\s:*&<>]+,?\s?)*)\)", line_content)
        if len(function_groups) > 0:
            # check for a declaration (line ends with a ;)
            if line_content.endswith(";"):
                self.nvim.out_write("Found Declaration!\n")
                return
            # check for a definition (this line ends with or next line starts with a {)
            if line_content.endswith("{"):
                self.nvim.out_write("Found Definiton!\n")
                return
            next_line_content = self.nvim.funcs.getline(self.nvim.funcs.line('.') + 1)
            if "{" in next_line_content:
                self.nvim.out_write("Found Definiton!\n")
                return
        else:
            self.nvim.out_write("Nothing found!\n")
            return
