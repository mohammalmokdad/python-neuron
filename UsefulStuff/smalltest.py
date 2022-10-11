import numpy as np

size=3
rng = np.random.default_rng()
nums=rng.integers(-30,31,size)
print(nums)
answer=np.empty(len(nums))
for i in np.arange(0,len(nums),1):
    print(i)
    mask=np.ones(len(nums),dtype=bool)
    mask[i]=False
    print(mask)
    masked=nums[mask]
    print(masked)
    answer[i]=np.product(masked)

print(answer)