class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        
        if (eq.equals("=")) {
            if ((ineq.equals(">") && n >= m) || (ineq.equals("<") && n <= m)) {
                answer++;
            }
        } else {
            if ((ineq.equals(">") && n > m) || (ineq.equals("<") && n < m)) {
                answer++;
            }
        }
        
        return answer;
    }
}