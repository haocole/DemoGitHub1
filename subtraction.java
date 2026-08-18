
    import java.util.Scanner;
public class subtraction {
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Nhập hai số từ bàn phím
        System.out.print("Nhập số thứ nhất (a): ");
        double a = scanner.nextDouble();

        System.out.print("Nhập số thứ hai (b): ");
        double b = scanner.nextDouble();

        // Tính hiệu hai số
        double hieu = a - b;

        // In kết quả ra màn hình
        System.out.printf("Hiệu của hai số (%.2f - %.2f) là: %.2f\n", a, b, hieu);

        scanner.close();
    
    }
    }

