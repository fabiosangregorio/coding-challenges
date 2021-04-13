package data_structures.arrays;

import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

public class dynamic_array {
  public static List<Integer> dynamicArray(int n, List<List<Integer>> queries) {
    Vector<ArrayList<Integer>> matrix = get2DVector(n);
    int lastAnswer = 0;
    ArrayList<Integer> result = new ArrayList<>();
    
    for(List<Integer> query: queries) {
      int queryType = query.get(0);
      int x = query.get(1);
      int y = query.get(2);

      int index = (x ^ lastAnswer) % n;
      if(queryType == 1) {
        matrix.get(index).add(y);
      }
      else if (queryType == 2) {
        ArrayList<Integer> row = matrix.get(index);
        int value = row.get(y % row.size());
        lastAnswer = value;
        result.add(value);
      }
    }

    return result;
  }

  public static Vector<ArrayList<Integer>> get2DVector(int n) {
    Vector<ArrayList<Integer>> matrix = new Vector<>(n);
    for(int i = 0; i < n; i++) {
      matrix.add(i, new ArrayList<Integer>());
    }
    return matrix;
  }


  public static void main(String[] args) {
    int n = 2;
    int[][] queries = {
      {1, 0, 5},
      {1, 1, 7}, 
      {1, 0, 3}, 
      {2, 1, 0}, 
      {2, 1, 1}
    };

   List<Integer> result = dynamicArray(n, queries);

   for(int i: result) System.out.println(i);
  }
}