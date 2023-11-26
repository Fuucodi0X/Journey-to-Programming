# Simple Calculator

# Ask the operation
operator = input("Define an operator: ")
# Get operands
oprands = input("List as many operand as you want(separated by space daa!): ").split()
# Convert form string to float
nums = [float(oprand) for oprand in oprands]


value = nums[0]
for i in range(1,len(nums)):
    # checking each operation
    if operator == '+':
        value += nums[i]
    elif operator == '-':
        value -= nums[i]
    elif operator == '*':
        value *= nums[i]
    elif operator == '**':
        value **= nums[i]
    elif operator == '/':
        value /= nums[i]
    else:
        print("Invalid operator use + - * / **")
    


print(value)