/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int l = 1;
        

        while (l <= n) {
            int mid = l + (n - l)/ 2;
            int response = guess(mid);
            switch(response) {
                case 0 -> {
                    return mid;
                }
                case 1 -> {
                    l = mid + 1;
                }
                case -1 -> {
                    n = mid - 1;
                }
            }
        }

        return 0;
    }
}