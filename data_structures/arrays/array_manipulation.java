package data_structures.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class array_manipulation {
  /** Naive solution, fails due to long execution time */
  // static long arrayManipulation(int n, int[][] queries) {
  // long[] array = new long[n];

  // for (int[] query : queries) {
  // int a = query[0] - 1;
  // int b = query[1] - 1;
  // int k = query[2];
  // for (int i = a; i <= b; i++) {
  // array[i] += k;
  // }
  // }

  // for(long item: array) {
  // System.out.println(item);
  // }
  // return max(array);
  // }

  /** Optimized solution, fails due to long execution time */

  // static long arrayManipulation(int n, int[][] queries) {
  // ArrayList<int[]> queriesList = new ArrayList<>(Arrays.asList(queries));
  // long max = 0;

  // Arrays.sort(queries, new Comparator<int[]>() {
  // @Override
  // public int compare(int[] q1, int[] q2) {
  // int a1 = q1[0];
  // int a2 = q2[0];
  // int aComp = Integer.compare(a1, a2);
  // if (aComp != 0)
  // return aComp;

  // int b1 = q1[1];
  // int b2 = q2[1];
  // return Integer.compare(b1, b2);
  // }
  // });

  // for (int i = 0; i < n; i++) {
  // long sum = 0;
  // for (int j = 0; j < queriesList.size(); j++) {
  // int[] query = queriesList.get(j);
  // int a = query[0] - 1;
  // int b = query[1] - 1;
  // int k = query[2];
  // // Current range
  // if (a <= i && b >= i)
  // sum += k;
  // // Past range, useless
  // else if (a < i && b < i) {
  // queriesList.remove(j);
  // j--;
  // } else
  // // Future range
  // break;
  // }
  // if (sum > max)
  // max = sum;
  // }

  // return max;
  // }

  static long arrayManipulation(int n, int[][] queries) {
    long[] array = new long[n + 1];

    for (int[] query : queries) {
      int a = query[0] - 1;
      int b = query[1];
      int k = query[2];
      array[a] += k;
      array[b] -= k;
    }

    long maxValue = 0;
    long currValue = 0;
    for (long item : array) {
      currValue += item;
      if (currValue > maxValue)
        maxValue = currValue;
    }

    return maxValue;
  }

  public static void main(String[] args) {
    int[][] queries = { { 1, 2, 100 }, { 2, 5, 100 }, { 3, 4, 100 } };
    // int[][] queries = { { 1, 5, 3 }, { 4, 8, 7 }, { 6, 9, 1 } };
    int n = 10;
    System.out.println(arrayManipulation(n, queries));
  }
}
