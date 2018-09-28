#include <stdio.h>
#include <stdlib.h>


unsigned long int factorial(int n)
{
unsigned long int r=1;
for (int i=1; i<=n; r *= i++) { }
  return r;
}

int main(int argc, char * argv[] ) 
{
  int num = atoi(argv[1]); 
unsigned long int calculado = factorial(num); printf("Factorial de %d \ es %llu \n", num, calculado); 

}

