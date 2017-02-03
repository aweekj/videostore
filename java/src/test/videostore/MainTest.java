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
}