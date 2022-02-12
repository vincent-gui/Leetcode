//hashset 和hashmap 检查key 的方式不一样

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        HashSet<String> endSet = new HashSet<>(), seen = new HashSet<>();
        wordList.forEach(word -> endSet.add(word));

        if(!endSet.contains(endWord)){
            return 0;
        }
        int beginStep = 1;
        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        queue.add(new Pair(beginWord, beginStep)); 
        seen.add(beginWord);


        while(!queue.isEmpty()){
            Pair<String, Integer> pair = queue.remove(); //更合适的方法是不使用pair, 每次get queue.size() 和一个count 去track 到了第几层
            String curr = pair.getKey();
            int step =  pair.getValue();
            if (curr.equals(endWord)){
                return step;
            }
            for (int i = 0; i < curr.length(); i++){
                char[] letters = curr.toCharArray();
                for (char c = 'a'; c <= 'z'; c++){
                    letters[i] = c;
                    String newWord = new String(letters);
                    if(endSet.contains(newWord) && !seen.contains(newWord)){
                        seen.add(newWord);
                        queue.add(new Pair(newWord, step + 1));
                    }
                }
            }

        }
        return 0;

    }
}