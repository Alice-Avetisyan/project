#  import testpackage.moduletest.hello  --> this one doesn't work for some reason
from testpackage.moduletest import hello
from newpackage.newpmodule import calculate_sum
from newpackage.nestedpackage.nestedmodule import set_name

hello()  # importing function from testpackage folder (package 1)
calculate_sum(10, 20)  # importing function from newpackage folder (package 2)
set_name()  # importing function from nestedpackage folder (package 1 from package 2)


