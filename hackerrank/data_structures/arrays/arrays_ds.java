package data_structures.arrays;

public class arrays_ds {
  static int[] reverseArray(int[] array) {
    int n = array.length;
    int last = n - 1;
    int middle = Math.floorDiv(n, 2);

    for(int left = 0; left < middle; left++) {
      int right = last - left;
      int temp = array[left];
      array[left] = array[right];
      array[right] = temp;
    }
    return array;
  }
  
  public static void main(String[] args) {
    int[] inputData = {1,4,3,2};
    int[] output = reverseArray(inputData);
    for(int item: output) {
      System.out.println(item);
    }
  }
}