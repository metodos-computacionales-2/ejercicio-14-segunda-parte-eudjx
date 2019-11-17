#include <iostream>
#include <cmath>

double euler(double h)
{
h=0.01;
double f0=1.0;
double f1=0.0;
double k=50.0;
double m=2.0;
double y=0.8;

for  (double t=0; t<10;t+=h)

{
double x1=f0;
double x2=f1;

f0=f0+h*x2;
f1=f1-(h*(k/m)*x1);
std::cout<<t<<"  "<<f0<<"  "<<f1<<std::endl;
}
}
int main()
{
std::cout<<euler(0.01)<<std::endl;
}
