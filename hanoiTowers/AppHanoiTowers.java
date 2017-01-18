package hanoiTowers;

/**
 * Created by gimin on 1/17/17.
 */
public class AppHanoiTowers {

    public static void main(String[] args) {
        int n = 12;
        Algorithm algo = new Algorithm();
        int moves =  algo.solveHanoiTowers(n, 'A', 'B', 'C');
        System.out.println("Done in " + moves + ", moves");
    }
}
