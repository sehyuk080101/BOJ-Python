import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] dice = {a, b, c, d};
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num : dice) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        if (map.size() == 1) {
            int p = a;
            return 1111 * p;
        } else if (map.size() == 2) {
            List<Integer> keys = new ArrayList<>(map.keySet());
            int k1 = keys.get(0), k2 = keys.get(1);
            int c1 = map.get(k1), c2 = map.get(k2);
            if (c1 == 3 || c2 == 3) {
                int p = c1 == 3 ? k1 : k2;
                int q = c1 == 1 ? k1 : k2;
                return (int) Math.pow(10 * p + q, 2);
            } else {
                return (k1 + k2) * Math.abs(k1 - k2);
            }
        } else if (map.size() == 3) {
            int q = 0, r = 0;
            for (int key : map.keySet()) {
                if (map.get(key) == 2) continue;
                if (q == 0) q = key;
                else r = key;
            }
            return q * r;
        } else {
            return Arrays.stream(dice).min().getAsInt();
        }
    }
}
