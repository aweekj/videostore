package videostore;

public class Main {
    public static void main(String[] args) {
        Movie m1 = new Movie("Interstella", Movie.REGULAR);
        Movie m2 = new Movie("Arrival", Movie.NEW_RELEASE);
        Movie m3 = new Movie("Moana", Movie.CHILDREN);
        Movie m4 = new Movie("LaLaLand", Movie.NEW_RELEASE);

        Customer c = new Customer("Jamie");
        c.addRental(new Rental(m1, 3));
        c.addRental(new Rental(m2, 4));
        c.addRental(new Rental(m3, 5));
        c.addRental(new Rental(m4, 6));
        System.out.println(c.statement());
        System.out.println(c.htmlStatement());
    }
}
