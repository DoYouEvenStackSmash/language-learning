
'''
  a simple reference python program

  python3 sample_prog.py a b c
'''
import sys
print("hello world")

'''
  string indexing
  printing substrings
'''
def generic_behavior():
  print(f"{'-'*25}","\ngeneric_behavior")
  numString = "12345"
  
  # python iteration [1:3] is str[1] + str[2]. does not include second element
  print(numString[1:3])


'''
  performs operations on various types
    type checking 
    casting arbitrary to a string
    list operations
    multiple return values
'''
def some_function(variable_name, some_counter):
  print(f"{'-'*25}","\nsome_function()")
  
  # check type of variable, cast string if necessary
  if type(variable_name) != str:
    variable_name = str(variable_name)
  
  aString = variable_name

  list_of_lists = []
  
  # python for loop uses a range operator: range(int)

  for i in range(len(aString)):
    
    some_counter += i
    
    list_of_lists.append([])  # append a single empty list to the lisst of lists
    
    list_of_lists[-1].append(aString[i]) # index -1: last element of the list
    list_of_lists[-1].append(aString[len(aString) - i - 1])

  # return multiple values
  return list_of_lists, some_counter


'''
  reads arguments from commandline
    enumerate items in an iterable
'''
def stdin_string():
  print(f"{'-'*25}","\nstdin_string()")
  
  # enumerate returns a int_counter, iterator pair thing. 
  for index, element in enumerate(sys.argv):
    print("arg", f'{index}' , end = " = ")
    print(element)


'''
  several dictionary operations
    iterate over elements
    dictionary to set
    create new elements in dictionary
'''
def dictionary_ops():
  print(f"{'-'*25}","\ndictionary_ops()")
  
  arg_dictionary = {'x':1, 'y':2} # constant time access {key : value} pairs
  
  if 'z' not in arg_dictionary:  #check if an element is in a dictionary
    arg_dictionary['z'] = 3
  
  for k,v in arg_dictionary.items():  # items gets the key = k, value = v
    print(f"{k} : {v}")
    
    # create arbitrary new type elements in a dict() by dict[key] = value
    arg_dictionary[k] = {k:v}
  
  print(arg_dictionary)
  # creates a set of just the dictionary keys
  s = set(arg_dictionary)
  
  # adding an element to a set
  s.update('AAAAA')
  
  print(s)
  

'''
  python one-liners :)
'''
def lambda_fxn():
  print(f"{'-'*25}", "\nlambda_fxn()")
  sum_nums = lambda a,b: a + b
  
  print(sum_nums(10, 20))

def main():
  stdin_string()
  
  some_counter = 4
  
  # multiple values can be assigned in the same line
  arg1, arg2 = 12345, some_counter
  return_val_1, return_val_2 = some_function(arg1, arg2) 

    
  # fstring can print different types in the same print statement
  print(f'{return_val_1}, {return_val_2}')
  dictionary_ops()

  lambda_fxn()

# functions outside of some scope are just called wherever
generic_behavior()

# which is why we might call main down here
main()
