package interview;

public class Cli {
    public String getGreeting() {
        return "Hello world!";
    }

    public static void main(String[] args) {
        System.out.println(new Cli().getGreeting());
    }
}
