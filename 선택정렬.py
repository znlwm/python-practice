# 선택정렬
a= [1,5,6,1,2,4]

for i in range(len(a)):
    for j in range(i):
        if a[i] < a[j]:
            a[j],a[i]= a[i],a[j]
        
# print(a)

# 삽입정렬

a=[8,6,4,2,1,5,6,0]
for i in range(1,len(a)):
    for j in range(i,0,-1): # 인덱스i부터 1까지 1씩 감소하며 반복
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(a)

# 퀵정렬 - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터 위치 바꿈

array=[5,2,3,5,6,1,8,0]

def quick_sort(array, start, end):
    if start>=end: # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start +1
    right = end
    while(left<=right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right]>=array[pivot]):
            right-=1
        if(left>right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot]=array[pivot],array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right]= array[right], array[left]
            
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)
        
    quick_sort(array, 0 , len(array)-1)
    print(array)
    
    # 예제) 두 배열의 원소 교체
    # 두 개의 배열 A 와 B가 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두
    # 자연수이다.
    # 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와
    # 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꿔주는 것을 말한다.
    # 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
    # N,K 그릐고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 
    # 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램 작성