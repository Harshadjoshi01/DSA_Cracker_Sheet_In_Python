#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++){   //Making an array
        cin>>arr[i];
    }
    int temp = 0;
    int start = 0;
    for (int i = 0; i < n-1; i++){
        temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
    }
    for(int i = 0; i < n; i++){
        cout<<arr[i]<<" ";
    }
    return 0;

}