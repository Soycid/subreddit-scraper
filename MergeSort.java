public class MergeSort {
  public static int[] merge(int[] a, int[] b) {
    int i = 0; int j = 0;
    int[] out = new int[a.length+b.length];
    for (int x = 0; x<out.length; x++){
        int p = Integer.MAX_VALUE; int q = Integer.MAX_VALUE;
        if(i < a.length){
            p = a[i];}
        if(j < b.length){
            q = b[j];}
        if(p < q){
            out[x] = p;
            i++;}
        else{
            out[x] = q;
            j++;}
    }
    return out;
    }

  public static void main(String[] args) {
    int[] a = new int[]{ 1,2,3,5};
    int[] b = new int[]{ 4,5,6,9};
    int[] c = merge(a,b);
    for (int x : c){
    System.out.println(x);}
  }
}