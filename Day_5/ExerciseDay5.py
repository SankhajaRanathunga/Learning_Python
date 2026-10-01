

empty_list=[]
print(len(empty_list))



numbers=[2,4,5,8,4,7,3,7,9]
print(len(numbers))
first_num=numbers[0]
mid=numbers[len(numbers)//2]
last=numbers[-1]
print(first_num)
print(mid)
print(last)



mixed_data_type=["saka",12,5.10,"good","uk"]
print(mixed_data_type)



it_companies=["Facebool","Google","microsoft","Apple","Ibm","Oracle","Amazon"]
fc=it_companies[0]
mc=it_companies[len(it_companies)//2]
lc=it_companies[-1]
print(fc)
print(mc)
print(lc)
print(it_companies)
print(len(it_companies))
it_companies[0]="SaKaFlow"
print(it_companies)
it_companies.append("slt")
print(it_companies)
it_companies.insert(5,"glow")
print(it_companies)
it_companies[0]=it_companies[0].upper()
print(it_companies)
resul="#; ".join(it_companies)
print(resul)
does_exist="glow"in it_companies
print(does_exist)
does_exist="nibm"in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first_3c=it_companies[0:3]
print(first_3c)
last_3c=it_companies[-4:-1]
print(last_3c)
mid_c=len(it_companies)//2
print(it_companies[mid_c:mid_c+1])

it_companies.pop(0)
print(it_companies)


mid=len(it_companies)//2
it_companies.pop(mid)
print(mid)
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)

f_end=["html","css","js","react","redux"]
b_end=["node,Express","mongodb"]
fullstack =f_end +b_end
print(fullstack)
fullstack.append("python")
fullstack.append("sql")
print(fullstack)


ages=[19,22,19,24,20,25,26,24,25,24]
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
n=len(ages)
if n%2==0:
    median=(ages[n//2-1]+ages[n//2])/2
else:
    median=ages[n//2]
print("median age",median)