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

        # check for a declaration
        declaration_groups = re.findall("(\w+([:\w<>,\s*&]+)?)\s([\w:]+)\(((?:[\w\s:*&<>]+,?\s?)*)\);", line_content)
        if len(declaration_groups) > 0:
            self.nvim.out_write("Found Declaration!\n")
            return

        # check for a definition
        definition_groups = re.findall("(\w+([:\w<>,\s*&]+)?)\s([\w:]+)\(((?:[\w\s:*&<>]+,?\s?)*)\)\n*{", line_content)
        if len(definition_groups) > 0:
            self.nvim.out_write("Found Definiton!\n")
            return

        self.nvim.out_write("Nothing found!\n")
