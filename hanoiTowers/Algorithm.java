package hanoiTowers;

/**
 * Created by gimin on 1/17/17.
 */
public class Algorithm {
    public int solveHanoiTowers(int n, char source, char destination, char auxilliary) {
        int count = 0;

        if (n > 0) { // do 2 recursive calls
            count = solveHanoiTowers(n - 1, source, auxilliary, destination);
            System.out.println("Plate " + n + " from " + source + " rod, to " + auxilliary + " rod.");
            count++;
            count += solveHanoiTowers(n - 1, destination, source, auxilliary);
        }
        return count;
    }
}
