dict_ = {'a': 6, 'b': 3, 'c': 10}
test_dict = {key:'Foo'if value%3==0 else  'Bar' if value%5==0 else "none"  for key,value in dict_.items()if value%3==0 or value%5==0}
print(test_dict)