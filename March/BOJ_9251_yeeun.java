import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstStr = br.readLine();
        String secondStr = br.readLine();
        int firsthLength = firstStr.length();
        int secondLength = secondStr.length();
        int[][] dp = new int[firsthLength+1][secondLength+1];

        for (int i=1; i<=firsthLength; i++) {
            for (int j=1; j<=secondLength; j++) {
                if (firstStr.charAt(i-1) == secondStr.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        System.out.println(dp[firsthLength][secondLength]);
    }
}