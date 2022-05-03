/* This is the bruet force mehtod approch towards this problem and 
It can take O(n^2) when it will ask for the nth minimum value */


#include<iostream>
using namespace std;

int main(){
    int n, k;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++){   //Making an array
        cin>>arr[i];
    }
    cout<<"which smallest element to find >> "<<endl;
    cin>>k;
    int temp = 0;
    int u = 0;
    int l = 0;
    int r = n-1;
    int minimum = 0;
    while(k>0){
        minimum = arr[0];
        for (int i = 1; i <= r; i++){
            if (arr[i] < minimum ){
                minimum = arr[i];
                u = i;
            }
        }
        temp = arr[r];
        arr[r] = minimum;
        arr[u] = temp;
        r--;
        k--;
        
        
    }
    cout<<"Your minimum is >> "<<minimum<<endl;
    return 0;
}