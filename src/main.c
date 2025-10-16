#include <stdio.h>

int main(){
  int añoNacimiento;
  int añoActual = 2025;
  int edad;
  char nombre[50];
  char lenguaje[] = "C";
  char relleno[50];
  printf("¿Cual es tu nombre?: ");
  scanf("%s", nombre);
  scanf("%s", relleno);
  printf("¿En que año naciste?: ");
  scanf("%d", &añoNacimiento); 
  edad = añoActual - añoNacimiento;
  printf("Hola %s, tienes %d años. Este programa está hecho en el lenguaje de programación: %s", nombre, edad, lenguaje);
  return 0;
}
