package videostore;

import org.junit.Test;

import static org.junit.Assert.*;

public class MainTest {
    @Test
    public void testCustomer() {
        Customer c = new Customer("Jamie");
        assertNotNull(c);
    }

    @Test
    public void testStatement() throws Exception {
        Movie m1 = new Movie("Interstella", Movie.REGULAR);
        Movie m2 = new Movie("Arrival", Movie.NEW_RELEASE);
        Movie m3 = new Movie("Moana", Movie.CHILDREN);
        Movie m4 = new Movie("LaLaLand", Movie.NEW_RELEASE);

        Customer c = new Customer("Jamie");
        c.addRental(new Rental(m1, 3));
        c.addRental(new Rental(m2, 4));
        c.addRental(new Rental(m3, 5));
        c.addRental(new Rental(m4, 6));
        String statementResult = c.statement();
        System.out.println(statementResult);
        assertEquals("Rental Record for Jamie\n" +
                "\tInterstella\t3.5\n" +
                "\tArrival\t12.0\n" +
                "\tMoana\t4.5\n" +
                "\tLaLaLand\t18.0\n" +
                "You owed 38.0\n" +
                "You earned 6 frequent renter points\n", statementResult);
    }

    @Test
    public void testHtmlStatement() throws Exception {
        Movie m1 = new Movie("Interstella", Movie.REGULAR);
        Movie m2 = new Movie("Arrival", Movie.NEW_RELEASE);
        Movie m3 = new Movie("Moana", Movie.CHILDREN);
        Movie m4 = new Movie("LaLaLand", Movie.NEW_RELEASE);

        Customer c = new Customer("Jamie");
        c.addRental(new Rental(m1, 3));
        c.addRental(new Rental(m2, 4));
        c.addRental(new Rental(m3, 5));
        c.addRental(new Rental(m4, 6));
        String statementResult = c.htmlStatement();
        System.out.println(statementResult);
        assertEquals("<h1><em>Rental Record for Jamie</em><h1><p>\n" +
                "\tInterstella: 3.5<br>\n" +
                "\tArrival: 12.0<br>\n" +
                "\tMoana: 4.5<br>\n" +
                "\tLaLaLand: 18.0<br>\n" +
                "<p> You owed <em>38.0</em><p>\n" +
                "You earned <em>6</em> frequent renter points<p>\n", statementResult);
    }

}