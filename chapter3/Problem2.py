letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
replaced=letter.replace("<|Name|>", "Harry").replace("<|Date|>", "24 September 2050")
print(replaced)
