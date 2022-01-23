global_var = "This is a global variable"
local_var = "This is a global variable with same variable name as local variable"

def local():
    local_var = "This is a local variable"
    print(local_var)

print(global_var)
print(local_var)
local()