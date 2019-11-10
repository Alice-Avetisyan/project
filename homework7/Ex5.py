company_names = ['Google', 'Yahoo', 'Adidas', 'Warner Brothers']
# if argumnet in string

def ends_with_s(company_names):
    new_list = [name for name in company_names if name[-1] == 's']
    print(new_list)

def contains_double(company_names, double_letter='oo'):
    new_list = [name for name in company_names if double_letter in name] # name.contains('oo')
    print(new_list)

ends_with_s(company_names)
contains_double(company_names)