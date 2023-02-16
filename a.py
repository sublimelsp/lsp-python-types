import re
a = "Union['Definition', List['DefinitionLink'],"
return_type = re.sub(r"(\w+)", r'(lsp_types.\1)', a)
print(return_type)