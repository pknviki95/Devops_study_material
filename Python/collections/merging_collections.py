#-----------------------------------------------------------------
#   Merging of collections
#[*var1,*var2],(*var1,*var2),{*var1,*var2},{*key1:val1,*key2:val2}
#-----------------------------------------------------------------

# Merging of set values

s1={10,20,'viki'} 
s2={40,50,'guru'} 

s3={*s1,*s2}
print(s3)

# Merging of list values

l1=[1,2,4,5,6]
l2=['viki',2,5,7]

l3=[*l1,*l2]
print(l3)

# Merging of tuples

t1=(1,2,4,5,6,'viki')
t2=(2,3,6,7,89)

t3=(*t1,*t2)
print(t3)

# Merging of Dict

dict1={1:'viki',2:'guru'}
dict2={3:'siva', 4:'ram'}

dict3={*dict1,*dict2}   #It picks key element in dictionary
print(dict3)


dict4={**dict1,**dict2}   #it picks both key:value element in dictionary
print(dict4)
