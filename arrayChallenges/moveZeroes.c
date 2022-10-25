#include <stdio.h>

int optimizeLeadingZeroes(int* nums,int numsSize){
		for(int i=numsSize-1;i>0;i--){
				if (*(nums+i) != 0) {
						return i+1;
				}
		}
		return 0;
}

void moveZeroes(int* nums,int numsSize){
		int end,shift = 0;
		end = optimizeLeadingZeroes(nums,numsSize);
		printf("%d\n",end);
		for(int i=0;i<end;i++){
				if (*(nums + i) == 0){
						shift++;
				}
				else if (shift > 0){
						*(nums + i - shift) = *(nums + i);
						*(nums + i) = 0;
				}
				printf("\n%d\t%d\n",i,shift);
				for (int i=0;i<9;i++) {
						printf("%d\n",nums[i]);
				}
		}
}






int main() {
		int inums[9] = {1,2,0,4,5,6,7,8,0};
		moveZeroes(inums,9);
		return 0;
}

