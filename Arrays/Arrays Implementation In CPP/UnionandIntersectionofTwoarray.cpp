#include<iostream>
using namespace std;
void printArray(int a[], int size){
    for (int i = 0; i < size; i++){
        cout<<a[i]<<" , ";
    }
}
void merge(int arr[], int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;
 
    // Create temp arrays
    int L[n1], R[n2];
 
    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    // Merge the temp arrays back into arr[l..r]
 
    // Initial index of first subarray
    int i = 0;
 
    // Initial index of second subarray
    int j = 0;
 
    // Initial index of merged subarray
    int k = l;
 
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of
    // L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of
    // R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
// l is for left index and r is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int arr[],int l,int r){
    if(l>=r){
        return;//returns recursively
    }
    int m = (l+r-1)/2;
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);
}
void printUnion(int arr1[], int arr2[], int m, int n) 
{ 
    int i = 0, j = 0;
    while (i < m && j < n) { 
        if (arr1[i] < arr2[j]) {
            cout << arr1[i++] << " ";
        }    
  
        else if (arr2[j] < arr1[i]) {
            cout << arr2[j++] << " "; 

        }
  
        else { 
            cout << arr2[j++] << " "; 
            i++; 
        } 
    } 
  
    /* Print remaining elements of the larger array */
    while (i < m) 
        cout << arr1[i++] << " "; 
  
    while (j < n) 
        cout << arr2[j++] << " ";

}
void printIntersection(int arr1[], int arr2[], int m, int n) 
{ 
    int i = 0, j = 0; 
    while (i < m && j < n) { 
        if (arr1[i] < arr2[j]) 
            i++; 
        else if (arr2[j] < arr1[i]) 
            j++; 
        else /* if arr1[i] == arr2[j] */
        { 
            cout << arr2[j] << " "; 
            i++; 
            j++; 
        } 
    }
}  
//This best approch to find Union and Intersection is to find it after doing Sorting 
int main(){
    int n1, n2;
    cin>>n1;
    int arr1[n1];
    for (int i=0; i<n1; i++){
        cin>>arr1[i];
    }
    cin>>n2;
    int arr2[n2];
    for (int i=0; i<n2; i++){
        cin>>arr2[i];
    }
    mergeSort(arr1, 0, n1-1);
    mergeSort(arr2, 0, n2);
    printUnion(arr1, arr2, n1, n2);
    cout<<endl;
    printIntersection(arr1, arr2, n1, n2);
    return 0;

}

/* This method can take O(N*M) time complaxity so it is not the effiecent way
int main(){
    int n1, n2;
    cin>>n1;
    int arr1[n1];
    for (int i=0; i<n1; i++){
        cin>>arr1[i];
    }
    cin>>n2;
    int arr2[n2];
    for (int i=0; i<n2; i++){
        cin>>arr2[i];
    }
    int U[n1+n2];
    for (int i = 0; i < n1; i++){
        U[i] = arr1[i];
    }
    int k = n1;
    for (int i = 0; i < n1; i++){
        for(int j = 0; j<n2; j++){
            if (arr1[i] != arr2[j]){
                U[k] = arr2[j];
                k++;
            }
        }
    }
    
printArray(U,n1+n2);
return 0;
}*/