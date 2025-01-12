import java.util.Scanner;

public class Temperature {

    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the temperature value: ");
        double temperature = scanner.nextDouble();

        System.out.println("Enter the original unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ");
        char originalUnit = scanner.next().charAt(0);

        switch (Character.toUpperCase(originalUnit)) {
            case 'C':
                convertFromCelsius(temperature);
                break;
            case 'F':
                convertFromFahrenheit(temperature);
                break;
            case 'K':
                convertFromKelvin(temperature);
                break;
            default:
                System.out.println("Invalid unit of measurement. Please enter C, F, or K.");
        }
    }

    public static void convertFromCelsius(double celsius) {
        double fahrenheit = (celsius * 9/5) + 32;
        double kelvin = celsius + 273.15;
        System.out.printf("Celsius: %.2f\nFahrenheit: %.2f\nKelvin: %.2f\n", celsius, fahrenheit, kelvin);
    }

    public static void convertFromFahrenheit(double fahrenheit) {
        double celsius = (fahrenheit - 32) * 5/9;
        double kelvin = (fahrenheit - 32) * 5/9 + 273.15;
        System.out.printf("Fahrenheit: %.2f\nCelsius: %.2f\nKelvin: %.2f\n", fahrenheit, celsius, kelvin);
    }

    public static void convertFromKelvin(double kelvin) {
        double celsius = kelvin - 273.15;
        double fahrenheit = (kelvin - 273.15) * 9/5 + 32;
        System.out.printf("Kelvin: %.2f\nCelsius: %.2f\nFahrenheit: %.2f\n", kelvin, celsius, fahrenheit);
    }
}
