#include <stdio.h>
float nums;
float a;
float b;
float c;
float s;
int main(void){
printf("How many fibonacci numbers do you want?\n");
if (0 == scanf("%f", &nums)) {
nums = 0;
scanf("%*s");
}
printf("\n");
a = 0;
b = 1;
while (nums>0){
printf("%.2f\n", (float)(a));
c = a+b;
a = b;
b = c;
nums = nums-1;
}
a = 0;
while (a<1){
printf("Enter number of scores: \n");
if (0 == scanf("%f", &a)) {
a = 0;
scanf("%*s");
}
}
b = 0;
s = 0;
printf("Enter one value at a time: \n");
while (b<a){
if (0 == scanf("%f", &c)) {
c = 0;
scanf("%*s");
}
s = s+c;
b = b+1;
}
printf("Average: \n");
printf("%.2f\n", (float)(s/a));
return 0;
}
