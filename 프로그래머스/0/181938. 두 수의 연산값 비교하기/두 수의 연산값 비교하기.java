class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        if (2 * a * b > Integer.parseInt(a + "" + b)) {
            answer += 2 * a * b;
        } else {
            answer += Integer.parseInt(a + "" + b);
        }
        
        return answer;
    }
}