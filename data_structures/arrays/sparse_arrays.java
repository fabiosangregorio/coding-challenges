package data_structures.arrays;

public class sparse_arrays {
  static int[] matchingStrings(String[] strings, String[] queries) {
    int[] matches = new int[queries.length];

    for(int i = 0; i < queries.length; i++) {
      String query = queries[i];
      for(String str: strings) {
        if(query.equals(str)) {
          matches[i] += 1;
        }
      }
    }
    
    return matches;
  }

  public static void main(String[] args) {
    String[] strings = { "aba", "baba", "aba", "xzxb" };
    String[] queries = { "aba", "xzxb", "ab" };
    int[] output = matchingStrings(strings, queries);
    for(int item: output) {
      System.out.println(item);
    }
  }
}
