package data_structures.arrays;

public class array_2d {
  static int hourglassSum(int[][] matr) {
    int HS_SIZE = 3;
    int maxSum = Integer.MIN_VALUE;

    int maxRow = matr.length - HS_SIZE + 1;
    for(int row = 0; row < maxRow; row++) {
      int maxCol = matr[row].length - HS_SIZE + 1;
      for(int col = 0; col < maxCol; col++) {
        int hsSum = matr[row][col]
          + matr[row][col + 1]
          + matr[row][col + 2]
          + matr[row + 1][col + 1]
          + matr[row + 2][col]
          + matr[row + 2][col + 1]
          + matr[row + 2][col + 2];
        
        if(hsSum > maxSum) maxSum = hsSum;
      }
    }

    return maxSum;
  }
  
  public static void main(String[] args) {
    int[][] inputData = {
      {-9, -9, -9, 1, 1, 1},
      {0, -9, 0, 4, 3, 2},
      {-9, -9, -9, 1, 2, 3},
      {0, 0, 8, 6, 6, 0},
      {0, 0, 0, -2, 0, 0},
      {0, 0, 1, 2, 4, 0},
    };

    System.out.println(hourglassSum(inputData));
  }
}