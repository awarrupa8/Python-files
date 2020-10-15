# Python code to reverse a string  
# using loop 
  
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 

def reverse_string(s):
  reverse=''
  for  i in range(len(s)-1,0,-1):
    reverse=reverse+i
  return reverse
s=input("Enter any string: ")
print("Reversed string: ",reverse_string(s))
