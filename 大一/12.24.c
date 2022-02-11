/*#include<stdio.h>
void display(int *j,int n);
void main()
{
	int num[]={1,2,3,4};
	display(num,4);
}
void display(int *j,int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		printf("第%d个元素为%d\n",i+1,*j);
		j++;
	}
}*/

/*#include<stdio.h>
void main()
{
	int i=8;
	printf("i第地址：i=%u\n",&i);
	printf("i的值：i=%d",i);
}*/
/*
#include<stdio.h>
#define PI 3.14
void area(int,float*,float*);
void main()
{
	int radius;
	float areas,meter;
	printf("banjing:");
	scanf("%d",&radius);
	area(radius,&areas,&meter);
	printf("面积=%.2f\n",areas);
	printf("周长=%.2f\n",meter);
}
void area(int r,float*a,float*m)
{
	*a=PI*r*r;
	*m=PI*2*r;
}
*/
/*
#include<stdio.h>
main()
{
	int x=10,y=5,*px,*py;
	px=&x;
	py=&y;
	printf("*px=%d,*py=%d",*px,*py);
}*/

/*#include<stdio.h>
void swap(int*p1,int*p2)
{
	int p;
	p=*p1;
	*p1=*p2;
	*p2=p;
}
void main()
{
	int a,b,*pt1,*pt2;
	scanf("%d,%d",&a,&b);
	pt1=&a;
	pt2=&b;
	if(a<b)
		swap(pt1,pt2);
	printf("%d,%d\n",*pt1,*pt2);
}*/

/*#include<stdio.h>
void swap(int*p1,int*p2);
main()
{
	int a,b;
	printf("please enter two int:");
	scanf("%d%d",&a,&b);
	swap(&a,&b);
	printf("after exchange:%d%d",a,b);
}
void swap(int*a,int*b)
{
	int p;
	p=*a;
	*a=*b;
	*b=p;
}*/

/*
#include<stdio.h>
int*min(int*,int* y);
void main()
{
	int i=1,j=2;
	int *m;
	m=min(&i,&j);
	printf("最小值：%d\n",*m);
}
int* min(int* x,int* y)
{
	int* z;
	z=(*x<*y)?x:y;
	return z;
}*/

/*#include<stdio.h>
void main()
{
	int a,b,c,i;
	for(i=100;i<1000;i++)
	{
		a=i%10;
		b=i/10%10;
		c=i/100;
		if(i=a*a*a+b*b*b+c*c*c)
			printf("%d\n",i);
	}
}*/
/*
#include<stdio.h>
main()
{
	int i,j,k,n;
	printf("水仙花数是：");
	for(n=100;n<1000;n++)
	{
		i=n/100;
		j=n/10%10;
		k=n%10;
		if(i*100+j*10+k==i*i*i+j*j*j+k*k*k)
		{
			printf("% -5d",n);
		}
	}
}*/
                                                                                   





