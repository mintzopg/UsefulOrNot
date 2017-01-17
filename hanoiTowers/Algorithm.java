package hanoiTowers;

/**
 * Created by gimin on 1/17/17.
 */
public class Algorithm {
    public int solveHanoiTowers(int n, char first, char middle, char last) {
        int count = 0;

        if (n > 0) { // do 2 recursive calls
            count = solveHanoiTowers(n - 1, first, last, middle);
            System.out.println("Plate " + n + " from " + first + " rod, to " + last + " rod.");
            count++;
            count += solveHanoiTowers(n - 1, middle, first, last);
        }
        return count;
    }
}
