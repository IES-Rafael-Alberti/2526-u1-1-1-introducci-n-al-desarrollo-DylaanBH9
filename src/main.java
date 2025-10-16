import java.util.Scanner;

public class main{
  public static void main(String[] args){
    String nombre;
    int edad;
    int añoActual = 2025;
    int añoNacimiento;
    String lenguaje = "Java";
    Scanner entrada = new Scanner(System.in);
    System.out.printf("¿Cual es tu nombre?: ");
    nombre = entrada.nextLine();
    System.out.printf("¿En que año naciste?: ");
    edad = entrada.nextInt();
    System.out.printf("Hola %s, tienes %d años. Este programa está hecho en el lenguaje de programación: %s", nombre, edad, lenguaje);
    entrada.close();
}
}
